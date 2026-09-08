"""Concepts: Region growth, without changing topology, the direction of marks until they are hit.

Transformation steps:
1. Identify connected components of 3s.
2. Extend the grid of 3s outward in the direction of every mark 6 until it is hit.
3. Ensure all interior rows and columns containing 3s are fully expanded.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_baf41dbf as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "baf41dbf"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
