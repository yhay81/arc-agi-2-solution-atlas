# ARC-AGI-2 Solution Atlas

An executable atlas for all 1,120 tasks in the public
[ARC-AGI-2](https://github.com/arcprize/ARC-AGI-2) dataset. Each task has a Python
`solve(grid)` implementation, an English rule note, and machine-readable evidence about how the
implementation was accepted.

The atlas contains executable solutions and English rule notes for all 1,120 tasks. The solutions
exactly reproduce all 4,834 reviewed training and test pairs. Exact agreement with the provided
examples does not prove that an inferred rule is unique or that it generalizes to unseen inputs.

## Verify the atlas

Python 3.12.14 and [uv 0.12.12](https://docs.astral.sh/uv/) are required.
The atlas has no external runtime dependencies. Solutions use Python's standard library only.

```bash
uv run --locked --no-dev python -m scripts.verify --expected-tasks 1120
```

Expected result:

```text
tasks=1120 pairs=4834 passed=4834 failed=0
```

The verifier can also be called from Python within a source checkout:

```python
from pathlib import Path

from scripts.verify import verify_corpus

result = verify_corpus(Path("solutions"), Path("data"))
assert result.passed
```

The verifier imports and executes solution modules. Run it only with source you trust; it is not a
sandbox.

## Repository contents

| Path | Contents |
|---|---|
| `solutions/<task_id>.py` | One `solve(grid)` implementation per task |
| `notes/<task_id>.json` | English rule, steps, parameters, observations, and limitations |
| `data/{training,evaluation}/` | Pinned public ARC-AGI-2 task data, unchanged |
| `data/corrections/` | Complete reviewed task documents that override the same upstream task ID |
| `metadata/label_corrections.json` | Machine-readable cell-level provenance for those documents |
| `scripts/verify.py` | Corpus verifier, data loader, grid validation, and CLI |
| `site/` | Static atlas source |
| `tests/` and `scripts/` | Quality, provenance, and build tooling |

Each note records an English title and summary, transformation steps, concepts, one observation per
training pair, and only task-specific parameters or limitations. The compact schema and evidence
field are enforced by the test suite.

## Evidence

All 1,120 task modules are directly executable; filenames provide task identity and the modules do
not repeat documentation or provenance constants. They import neither NumPy nor SciPy. Modules that
need array-style operations import the shared audited pure-Python compatibility module instead of
embedding duplicate implementations. Notes hold concepts, rule descriptions, and validation scope,
while `metadata/solutions.json` holds authoritative counts and SHA-256 manifests.

No label claims performance on hidden or out-of-distribution tasks.

## Quality gate

Run the complete gate before changing or releasing the corpus:

```bash
uv sync --locked --dev
uv run --locked ruff format --check .
uv run --locked ruff check .
uv run --locked ty check tests scripts
uv run --locked pytest -q
uv run --locked python scripts/check_upstream.py
uv run --locked python -m scripts.verify --expected-tasks 1120
```

`tests/test_generalization.py` supplements corpus replay with synthetic contrast cases. These vary
canvas dimensions, object placement, and structural repetition for rules where those properties
are not semantically fixed. Add a synthetic case whenever a solver is generalized beyond the
dimensions or coordinates present in the provided task pairs.

Build the static atlas with:

```bash
uv run --locked python -m scripts.build_site
```

Generated files are written to `.site-build/`.

## Data and license

The upstream directories are pinned byte-for-byte to ARC-AGI-2 commit
`f3283f727488ad98fe575ea6a5ac981e4a188e49`. Their digest, task counts, and pair count are recorded in
`metadata/upstream.json` and checked by `scripts/check_upstream.py`.

Two corrected documents contain 11 reviewed output-cell changes: three in `b74ca5d1`, documented by
[ARC-AGI-2 pull request #16](https://github.com/arcprize/ARC-AGI-2/pull/16), and eight in `963c33f8`,
documented in the
[ARC Prize discussion](https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-2/discussion/731040).
Keeping complete corrected documents in a separate directory makes both views easy to inspect and
keeps solution code focused only on the inferred transformations.

Original atlas code and documentation are licensed under the Apache License 2.0. The ARC-AGI-2 data
uses the same license. See `LICENSE` for the terms.

See `CONTRIBUTING.md` for contribution requirements.
