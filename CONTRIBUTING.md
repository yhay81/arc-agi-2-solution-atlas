# Contributing

Contributions should preserve the independence, evidence, and quality requirements in `README.md`.

Before opening a pull request, run:

```bash
uv sync --locked --dev
uv run --locked ruff format --check .
uv run --locked ruff check .
uv run --locked ty check tests scripts
uv run --locked pytest -q
uv run --locked python scripts/check_upstream.py
uv run --locked python -m scripts.verify --expected-tasks 1120
```

Do not add output lookup tables or code copied from third-party ARC solver repositories. Include a
human-readable rule note and provenance statement for every new solution. Solution modules may
import Python standard-library modules only; do not add NumPy, SciPy, other repository modules,
or third-party imports. Every solution module must expose exactly one unannotated entry point with
the signature `def solve(grid)`.

When replacing an example-specific dimension, coordinate, or lookup with a structural rule, add a
synthetic contrast case to `tests/test_generalization.py`. The case should vary the removed
assumption and test the inferred relation directly; replaying another provided pair is insufficient.
