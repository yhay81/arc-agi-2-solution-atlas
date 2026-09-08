"""Concepts: axis (column) to devide grid in two halves, Two halves of a grid, addition of grid, conditional replacement of value

Transformation steps:
1. Find the column containing the value 4; this acts as the axis to split the grid.
2. Split the grid into left_half (left of the axis) and right_half (right of the axis).
3. Add the two halves together
4. If the sum of the two halves is 0, then output 0, else output 2

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_e133d23d as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "e133d23d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
