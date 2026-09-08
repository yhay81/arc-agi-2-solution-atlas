"""Concepts: barrier-based sliding, directional movement toward barrier.

Transformation: Slide all non-zero, non-8 values toward the nearest side of a continuous 8-barrier until adjacent,
with any barrier gaps letting them fall off the grid.

Transformation steps:
1. Identify whether the barrier (8s) is vertical or horizontal.
2. For each marked value (≠0, ≠8), slide it toward the nearest side of the barrier
   in its row/column until adjacent to an 8, stopping early if blocked by the grid edge
   or falling off through barrier gaps.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_f83cb3f6 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "f83cb3f6"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
