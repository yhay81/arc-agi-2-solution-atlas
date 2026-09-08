"""Arrange same-color objects by their position in the input grid.
Each connected group of a color is stacked from bottom to top, left to right, in order of their first column appearance.

Concept:
- arranging same color objects
- sorting by spatial properties: first column appearance from left to right


Steps:
    1. Identify background color (most frequent).
    2. For each non-background color, sort by first column of appearance.
    3. For each color, find connected groups and sort them by their leftmost column.
    4. Place each group as a block in the output grid, stacking vertically and shifting right for each color.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_4acc7107 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "4acc7107"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
