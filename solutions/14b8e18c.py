"""Concepts:
- Identify square compartments formed by non-background values.
- For each square compartment, mark its corners with value 2.

Steps:
1. Find the non-background value (value different from 7).
2. Group connected positions containing this value.
3. For each group:
    - Determine if it forms a square compartment.
    - If it's a square with consistent border values, mark its corners with 2.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_14b8e18c as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "14b8e18c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
