"""Concepts: full row/column, unique divider color

Transformation steps:
1. Find a row that is a single nonzero color across its full width, or a column that is a single nonzero color across its full height.
2. Return that color as a 1x1 grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.llm_task_solutions import solve_1a2e2828 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "1a2e2828"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
