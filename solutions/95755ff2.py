"""Diamond-fill: take non-zero border values (except 2) and propagate them
inward along diamond-shaped columns/rows until they hit another value
or the diamond boundary.

Concept
- Diamond frame recognition: Detect the diamond-shaped frame of 2s in the grid. (optional)
- Border seeding: Take border values (non-zero, not 2) from the outermost rows/columns.
- Value propagation: Spread these border values inward along rows/columns, constrained by the diamond boundary.
- Selective filling: Only fill empty (0) cells inside the diamond, preserving existing values (including the 2 frame).

Transformation Steps

1. Identify the diamond-shaped frame made of 2s. (optional)
2. Collect non-zero, non-2 values from the grid's top, bottom, left, and right borders.
3. For each collected border value:
    - If from top/bottom -> propagate vertically inside the diamond.
    - If from left/right -> propagate horizontally inside the diamond.
4.Stop propagation when hitting another non-zero cell or the diamond's edge.
5. Return the updated grid with filled values inside the diamond.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_95755ff2 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "95755ff2"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
