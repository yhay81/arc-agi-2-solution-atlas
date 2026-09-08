"""Concepts: horizontally shift connected non-zero blocks (connectivity=4)
          to the right until they hit either the grid boundary
          or another non-zero block.

Transformation steps:
1. Identify connected non-zero blocks for each unique value.
2. Process blocks in order of their rightmost column (rightmost first).
3. For each block, compute the maximum feasible right shift.
4. Clear original positions and place the block at its shifted location.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_5ffb2104 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "5ffb2104"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
