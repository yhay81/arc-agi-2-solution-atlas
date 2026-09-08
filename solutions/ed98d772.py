"""Concepts: Rotate grid, concatenate or stack grids

Transformation steps:
1. Generate the 90-degree, 180-degree, 270-degree rotated versions of the input grid.
2. Concatenate the original grid with the 90-degree rotated version (the top half)
3. Concatenate the 180-degree rotated version with the 270-degree rotated version (the bottom half).
4. Concatenate the top and bottom halves to form the final output grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_ed98d772 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "ed98d772"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
