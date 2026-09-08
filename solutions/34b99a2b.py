"""Concepts: symmetry, XOR gate, scalar multiplication

Transformation steps:
1. Identify the column of 4s that divides the grid into two equal-size parts.
2. XOR the occupancy of the left and right parts.
3. Multiply the result by 2.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.llm_task_solutions import solve_34b99a2b as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "34b99a2b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
