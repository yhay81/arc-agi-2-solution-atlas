"""Concepts: Extraction of minimal block with least non-1 values.

Transformation steps:
1. Identify all connected non-zero blocks in the grid.
2. For each block, extract its bounding box.
3. Count the number of cells in the box that are not 1.
4. Return the block with the minimal count of non-1 cells.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_7bb29440 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "7bb29440"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
