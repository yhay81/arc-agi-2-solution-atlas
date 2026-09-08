# ARC-AGI-2 Solution Atlas

An executable and verifiable atlas of solutions for the public ARC-AGI-2 task collection.

This repository is being developed privately. It will be released after every included solution has a clear provenance, a reproducible verification result, and a license review.

## What each task will contain

- a short human-readable rule;
- a small Python `solve(grid)` implementation;
- exact results for every provided input/output pair;
- assumptions, ambiguities, and known counterexamples;
- synthetic variations that test the same rule;
- a record of whether the solution was derived before or after inspecting the provided test output.

## Completion target

The first release targets all 1,120 unique public ARC-AGI-2 tasks. Inclusion requires exact agreement on every provided example. This is a corpus-verification standard, not a claim of performance on unseen tasks.

## Repository plan

| Area | Purpose |
|---|---|
| `solutions/` | One reviewed solution package per task |
| `arc_atlas/` | Small shared grid and object operations |
| `synthetic/` | Generators and derived task families |
| `catalog/` | Searchable metadata and aggregate statistics |
| `tests/` | Reproducible execution and schema checks |
| `site/` | Generated visual atlas for readers |
| `docs/` | Methodology, provenance, evaluation, and release notes |

The experimental workbench remains separate. Only reviewed artifacts are promoted into this repository.

## Development

The primary runtime is Python 3.12, matching the current Kaggle Notebook image. Tool versions are
locked with `uv.lock`.

```bash
uv sync --locked --dev
uv run ruff format --check .
uv run ruff check .
uv run ty check
uv run pytest --cov
uv run arc-atlas verify
```

The release gate additionally requires the complete public corpus:

```bash
uv run arc-atlas verify --expected-tasks 1120
```

The verifier discovers every `solutions/<task-id>/` package, loads its `solve(grid)` function, and
checks every provided `train` and `test` output cell-for-cell. Solver exceptions, malformed grids,
missing outputs, empty corpora, and task-count mismatches fail verification.
