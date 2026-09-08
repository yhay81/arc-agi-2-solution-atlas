"""Concepts: Value mapping and neighborhood transformation.

Transformation steps:
1. Identify unique values in the grid that appear more than once, excluding zeros.
2. Extract a mapping grid from top-left corner of the input grid.
3. Replace values in the neighboring cells based on the mapping.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_305b1341 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "305b1341"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
