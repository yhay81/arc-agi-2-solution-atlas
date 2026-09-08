"""Concepts: Source is emitting substance (2)

Transformation steps:
1. Find connected blocks of 1s that form sources
2. Fill their interior with 2s (substance)
3. Detect the opening (cell with most frequent background value).
4. Extend 2s as a stream of substance from the opening outward till the grid boundary is reached.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_292dd178 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "292dd178"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
