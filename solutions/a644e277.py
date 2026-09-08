"""Concepts:
- Region extraction based on dominant and secondary values
- Subgrid cropping using row/column frequency analysis

Transformation steps:
1. Identify the background value (most frequent) and the marked value (second most frequent) in the grid.
2. Find all the rows dominated by the marked value
3. Find all the columns dominated by the marked value
4. For each intersection of these rows and columns, check if the cell contains the background value.
5. Collect all such row and column indices to define the bounding box.
6. Crop the input grid to the rectangle defined by these rows and columns.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_a644e277 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "a644e277"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
