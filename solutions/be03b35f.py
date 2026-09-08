"""Concepts: 2x2 grid extraction, 2D 90 degree rotation, pattern matching

Transformation steps:
1. Extract 2x2 grids from three corners: top-left, top-right, and bottom-left
2. Select TL as the base and generate its 90, 180, and 270 degree rotations
3. Find which rotations match TR and BL
4. The unmatched rotation is the output

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_be03b35f as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "be03b35f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
