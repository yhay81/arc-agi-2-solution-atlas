"""Concept:
Color nested rectangles with the color of their containing rectangle.

Steps:
1. Identify all rectangles in the grid by their outlines.
2. Create a copy of the grid and remove interior of all rectangles.
3. Find the outermost rectangles that remain after this process.
4. For each outermost rectangle, color all interior rectangles with its color.
5. Return the modified grid with colored nested rectangles.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_7d1f7ee8 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "7d1f7ee8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
