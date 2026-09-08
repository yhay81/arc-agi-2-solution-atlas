"""Concepts: Two halves of a grid, addition of grid, conditional replacement of value

Transformation steps:
1. Split the grid into top_half and bottom_half
2. Add the two halves together
3. If the sum of the two halves is 0, then output 4, else output 0

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_e345f17b as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "e345f17b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
