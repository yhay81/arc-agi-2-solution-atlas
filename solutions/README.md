# Task solutions

Every module in this directory contains a self-contained `solve(grid)` implementation derived from
the official ARC-AGI-2 task examples without consulting or translating third-party solution
implementations. A solution may import third-party Python libraries declared in `pyproject.toml`, but
it must not call another task solver or a shared task-transform engine.

If a future upstream snapshot adds a task, leave it absent until a training-derived rule is ready.
Do not add input hashes, pair-specific output tables, or other replay mechanisms merely to make
provided-pair verification pass.

`metadata/solutions.json` records provenance groups, unresolved IDs, the upstream commit and digest,
and a SHA-256 manifest of every active solution so a clean checkout can be audited reproducibly.
