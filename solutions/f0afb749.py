"""Concepts: value expansion, diagonal patterning

Transformation: Expand each non-zero cell to a 2x2 block, then extend diagonally with 2x2 [[1,0], [0,1]] patterns.

Transformation steps:
1. Identify all non-background (non-zero) values and their positions (r, c) in the input grid.
2. Create an output grid of size (2*nrows, 2*ncols) filled with zeros.
3. For each non-background value v:
   a. Place a 2x2 block filled with v at position (2*r, 2*c).
   b. From the center of that block, move along both diagonal directions:
      - (-1, -1), (-2, -2), ... upward-left
      - (+1, +1), (+2, +2), ... downward-right
     At each such position, place the fixed pattern [[1, 0], [0, 1]] (without overwriting existing non-zero values).

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_f0afb749 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "f0afb749"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
