"""Gather identical values (color) to the top-left and bottom-right corners from adjacent quadrants.

Concepts:
- Grid partitioning
- value gathering

Transformation Steps:
1. Identify the unique non-background value in the top-left and bottom-right 3x3 blocks.
2. For the top-left 3x3 block:
   - Move any matching value from the adjacent top-right, bottom-left, and bottom-right quadrants to the border of the top-left block,
   replacing its original position with the background color.
3. For the bottom-right 3x3 block:
   - Move any matching value from the adjacent top-right, bottom-left, and top-left quadrants to the border of the bottom-right block,
   replacing its original position with the background color.
4. Return the transformed grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_f28a3cbb as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "f28a3cbb"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
