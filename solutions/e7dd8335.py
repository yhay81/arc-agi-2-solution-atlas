"""Concepts: Shape identification and color transformation for vertical mirror symmetry.

Transformation steps:
1. Identify all positions containing value 1 in the grid
2. Determine the bounding box of the shape formed by these positions
3. Calculate the vertical midpoint of the shape
4. Replace all values below the midpoint with color 2, creating a mirror image (two-tone) effect

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_e7dd8335 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "e7dd8335"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
