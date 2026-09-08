"""Concept:
    The function extracts the largest connected group of non-background cells from each block of the input grid,
    where blocks are separated by columns of all zeros.
    It then places these groups into a compact output grid, shifting left if needed to avoid overlap.

Transformation Steps:
    1. Identify columns in the input grid that are entirely zeros to use as block separators.
    2. Set the output grid size based on the first partitioning column.
    3. For each block between partitioning columns:
        a. Find all non-background cell positions.
        b. Group these positions by 4-connectivity.
        c. Select the largest group.
        d. Place the group in the output grid at its original positions if free space (with background color 8) is available;
        otherwise, shift left by one column and place.
    4. Return the resulting compact output grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_337b420f as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "337b420f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
