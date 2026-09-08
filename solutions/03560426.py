"""Stack colored blocks from bottom to the left edge, keeping the same order.

Concepts:
- Pattern extraction: Identifying connected regions (ractangular-blocks) of same color
- Block arrangement: Stacking blocks with overlapping corners
- Spatial reorganization: Placing blocks in a stair-like pattern

Transformation Steps:
1. Identify distinct colors from the bottom row of input grid
2. For each color, extract its bounding box from the input grid
3. Arrange these blocks starting from top-left, with each subsequent block
   overlapping at corners in a diagonal stair pattern

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_03560426 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "03560426"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
