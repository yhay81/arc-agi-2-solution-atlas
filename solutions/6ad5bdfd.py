"""Concepts: Shift connected non-zero blocks (connectivity=4) horizontally or vertically
until they hit the grid boundary or another non-zero block.

Transformation steps:
1. Identify the direction to move (based on a row or column of 2s at the grid edge).
2. Find all connected non-zero blocks for each unique value.
3. Process blocks in the correct order for the direction.
4. For each block, compute the maximum feasible shift.
5. Clear original positions and place the block at its shifted location.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_6ad5bdfd as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "6ad5bdfd"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
