"""Paint the left-right symmetric non-background part in color 1.

Concept:
    - Identify the background color (most frequent).
    - For each non-background cell, if its horizontal mirror is also non-background, paint both positions with color 1.

Steps:
    1. Find the background and non-background colors.
    2. For each non-background cell, check its horizontal symmetric cell.
    3. If both are non-background, set both to color 1.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_ce039d91 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "ce039d91"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
