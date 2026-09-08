"""Clears grass (color 5) in rows/columns based on grass cutters (color 0) at the edges,
then repositions the grass cutters at the opposite edges.

Concept:
When a grass cutter (value 0) is placed at an edge of the grid, it clears all grass in
the corresponding row or column and then moves to the opposite edge.

Transformation Steps:
1. Identify grass cutters (color 0) at the edges of the grid
2. For each grass cutter:
   a. If at top/bottom edge, clear the entire column (replace with background color)
   b. If at left/right edge, clear the entire row (replace with background color)
3. Reposition each grass cutter to the opposite edge:
   a. From top -> bottom, bottom -> top
   b. From left -> right, right -> left

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_b25e450b as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "b25e450b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
