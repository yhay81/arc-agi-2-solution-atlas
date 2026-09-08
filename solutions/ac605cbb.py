"""Concept:
- color (value) based grid transformation (drawing lines)
- analysing intersections of newly drawn lines and drawing diagonals from there

Transformation Steps:
    1. Identify non-background colors (assuming background is 0).
    2. For each non-background color, locate its position and draw line patterns with color 5 according to the color value.
    3. If the two 5 line intesect, means: For each cell with color 5 that has non-zero neighbors in all four directions (up, down, left, right),
    then draw a diagonal line of color 4 extending to the grid edge.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_ac605cbb as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "ac605cbb"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
