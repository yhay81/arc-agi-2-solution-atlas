"""Concepts:
- grid rotation, scaling, and pattern matching,
- color (fill value) in placeholder pattern as per given reference

Steps:
1. Extract reference pattern (non-zero, non-8 values).
2. Extract placeholder pattern (pattern of 8s).
3. Reduce placeholder by removing duplicate rows and columns.
4. Find correct orientation by rotating reference pattern.
5. Replace placeholders with scaled reference pattern.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_103eff5b as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "103eff5b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
