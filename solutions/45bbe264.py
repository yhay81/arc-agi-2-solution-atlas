"""Concepts:
- Expand non-zero values along their rows and columns.
- Place value 2 at the intersections of expanded rows and columns.

Steps:
1. Find all non-zero positions.
2. For each non-zero position, extend its value along its row and column.
3. Place value 2 at intersections between the expanded rows and columns.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_45bbe264 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "45bbe264"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
