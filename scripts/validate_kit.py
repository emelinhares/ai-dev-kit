#!/usr/bin/env python3
"""Dependency-free structural checks for the AI Development Kit."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    ".ai/AGENTS.md",
    ".ai/README.md",
    ".ai/guardrails/safety.md",
    ".ai/policies/research.md",
    ".ai/practices/token_economy.md",
    ".ai/practices/tdd.md",
    ".ai/practices/definition-of-done.md",
    ".ai/practices/project-adoption.md",
    ".ai/practices/subagent-orchestration.md",
    ".ai/project/glossary.md",
    ".ai/project/state.json",
    ".ai/project/decisions.md",
    ".ai/project/assumptions.md",
    ".ai/project/scope.md",
    ".ai/project/health-report.md",
    ".ai/project/research-log.md",
    ".ai/roles/product-translator.md",
    ".ai/roles/discovery.md",
    ".ai/roles/mapper.md",
    ".ai/roles/planner.md",
    ".ai/roles/architect.md",
    ".ai/roles/researcher.md",
    ".ai/roles/executor.md",
    ".ai/roles/auditor.md",
    ".ai/roles/documentation-curator.md",
    ".ai/roles/release-manager.md",
    ".ai/templates/project-intake.md",
    ".ai/templates/feature.md",
    ".ai/templates/bug.md",
    ".ai/templates/discovery.md",
    ".ai/templates/research.md",
    ".ai/templates/release.md",
    ".ai/templates/adoption/project-mapping.md",
    ".ai/templates/adoption/health-report.md",
    ".ai/templates/adoption/access-map.md",
    ".ai/templates/adoption/environment-map.md",
    ".ai/templates/adoption/operational-runbook.md",
    ".ai/templates/adoption/access-request.md",
    "docs/README.md",
    "docs/product/README.md",
    "docs/engineering/README.md",
    "docs/engineering/architecture.md",
    "docs/engineering/adopting-projects.md",
    "docs/decisions/README.md",
    "docs/decisions/0000-template.md",
    "docs/runbooks/README.md",
)

STATE_KEYS = {
    "schema_version",
    "project",
    "mode",
    "status",
    "phase",
    "active_role",
    "last_updated",
    "current_outcome",
    "next_action",
    "blocked_by",
    "approvals_pending",
}

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
PRIVATE_KEY_HEADER = re.compile(r"-----BEGIN (?:[A-Z0-9]+ )?PRIVATE KEY-----")
SENSITIVE_NAMES = {
    ".env",
    "id_rsa",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
    "credentials.json",
    "service-account.json",
}
SENSITIVE_SUFFIXES = {".key", ".p12", ".pfx"}
IGNORED_PARTS = {".git", "node_modules", "dist", "build", "__pycache__"}


def repository_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and not any(part in IGNORED_PARTS for part in path.parts)
    ]


def check_required(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def check_state(errors: list[str]) -> None:
    state_path = ROOT / ".ai/project/state.json"
    if not state_path.is_file():
        return
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid .ai/project/state.json: {exc}")
        return
    missing = sorted(STATE_KEYS - set(state))
    if missing:
        errors.append(f"state.json missing keys: {', '.join(missing)}")
    if state.get("mode") not in {"NEW_PRODUCT", "ADOPT_PROJECT"}:
        errors.append("state.json mode must be NEW_PRODUCT or ADOPT_PROJECT")


def link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]
    if (
        not target
        or target.startswith(("#", "/", "http://", "https://", "mailto:"))
    ):
        return None
    return unquote(target.split("#", 1)[0].split("?", 1)[0])


def check_links(files: list[Path], errors: list[str]) -> None:
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"cannot read {path.relative_to(ROOT)}: {exc}")
            continue
        for match in MARKDOWN_LINK.finditer(content):
            target = link_target(match.group(1))
            if target is None:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                location = content.count("\n", 0, match.start()) + 1
                errors.append(
                    f"broken link: {path.relative_to(ROOT)}:{location} -> {target}"
                )


def check_sensitive_material(files: list[Path], errors: list[str]) -> None:
    for path in files:
        relative = path.relative_to(ROOT)
        lower_name = path.name.lower()
        if lower_name in SENSITIVE_NAMES or path.suffix.lower() in SENSITIVE_SUFFIXES:
            errors.append(f"sensitive-looking file must not be stored: {relative}")
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            errors.append(f"cannot scan {relative}: {exc}")
            continue
        if PRIVATE_KEY_HEADER.search(content):
            errors.append(f"private key material detected: {relative}")


def main() -> int:
    errors: list[str] = []
    files = repository_files()
    check_required(errors)
    check_state(errors)
    check_links(files, errors)
    check_sensitive_material(files, errors)

    if errors:
        print("AI Development Kit validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "AI Development Kit validation passed "
        f"({len(REQUIRED_FILES)} required files, "
        f"{sum(path.suffix.lower() == '.md' for path in files)} Markdown files)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
