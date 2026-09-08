"""Concepts: fit key into its lock by matching patterns and number (color)

Transformation steps:
1. Identify left 'key' region and right 'lock' region by distinct numbers.
2. Slide/extend the key shape horizontally and vertically until it perfectly fills the lock cavity.
3. Replace overlaps so the joined pattern has no gaps.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_fe45cba4 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "fe45cba4"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
