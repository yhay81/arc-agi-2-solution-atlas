"""Concepts: vertical symmetry (up-down flip), value replacement based on symmetry

Transformation steps:
1. Loop through each cell in the grid.
2. If value is 0, retain as 0.
3. If value is 8:
    - Check vertically mirrored cell (i.e., up-down symmetric).
    - If mirrored cell also contains 8, change to 2.
    - Otherwise, change to 5.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_a8610ef7 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "a8610ef7"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
