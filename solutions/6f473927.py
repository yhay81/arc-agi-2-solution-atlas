"""Concepts: Grid transformation (negative of the positive photograph) with flipping and stacking.

Transformation steps:
1. Identify positions of zero and non-zero values in the input grid.
2. Replace zeros with 8 and non-zero values with 0 in a copy of the input grid.
3. Flip the modified grid horizontally.
4. Depending on the position of non-zero values:
   - If non-zero values are on the left in input, stack the flipped grid to the left of the original grid.
   - If non-zero values are on the right in input, stack the flipped grid to the right of the original grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_6f473927 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "6f473927"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
