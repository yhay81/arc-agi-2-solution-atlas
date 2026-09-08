"""Concepts: Connected component analysis, mathematical property detection, component labeling.

Steps:
1. Find all connected groups of cells with value 5 (using 8-connectivity).
2. For each group:
   - If its size is a power of an integer (a^b, a > 1, b > 1) or exactly 2, set those cells to 2.
   - Otherwise, set those cells to 8.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_1d61978c as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "1d61978c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
