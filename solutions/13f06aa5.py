"""Concepts: Source firing objects to the grid wall, Directional propagation, unique value extension,

Transformation steps:
1. Identify unique values (appearing once) in the grid.
2. For each, extend its value in the direction of adjacent background cells (up, down, left, right).
3. Fill edge and corner cells according to overlap rules.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_13f06aa5 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "13f06aa5"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
