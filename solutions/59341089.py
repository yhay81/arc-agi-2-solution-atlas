"""Concepts: Flip grid, repeat parts, stack grids

Transformation steps:
1. Flip the input grid left to right.
2. Concatenate the flipped grid and the original grid horizontally and get the output part.
3. Horizontally stack the output part with itself to form the final output grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_59341089 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "59341089"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
