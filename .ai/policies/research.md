# Research Policy

Research is required before a decision when a material claim is:

- uncertain or outside verified project knowledge;
- recent, fast-changing, or version-dependent;
- security-, privacy-, legal-, reliability-, or cost-sensitive;
- about an external API, service, platform, dependency, limit, or compatibility;
- disputed by available evidence; or
- costly or difficult to reverse if wrong.

## Source order

Use applicable official documentation, specifications, standards, vendor
status/pricing pages, release notes, source repositories, or other official
primary evidence. Secondary sources may help find or challenge official
evidence, but cannot satisfy the gate or be the sole basis for a triggered
material decision. For project behavior, direct observation and executable
repository evidence are primary; verify external interfaces against their
official source.

Check publication/update date, version, environment, and applicability. Do not
silently generalize from a different version or plan.

## Evidence record

Add a concise entry to [`../project/research-log.md`](../project/research-log.md)
using the [research template](../templates/research.md). Preserve:

- question and decision it informs;
- conclusion in plain language;
- source title, stable link or repository reference, publisher, access date, and
  relevant version;
- the smallest useful supporting fact (paraphrased where possible);
- confidence, contradictions, and remaining uncertainty; and
- an expiry/recheck trigger for volatile facts.

Do not paste raw pages, long transcripts, search-result dumps, sensitive
material, or unsupported AI-generated claims. If official evidence is absent,
say so and choose a reversible experiment, explicit assumption, or owner
decision rather than inventing certainty.

## Research gate

The researcher hands off a recommendation, alternatives considered, and
uncertainty. The architect or decision owner remains accountable for the
decision. A triggered decision cannot be accepted until applicable official
evidence has been checked. If no official source exists or is accessible, log
that absence and defer the material decision or use a reversible experiment
that does not cross the decision boundary. Recheck evidence before a release
when its expiry trigger has fired.
