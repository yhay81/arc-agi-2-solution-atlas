"""Concepts: Frame (pad) every non-zero block with value (color) and thickness illustrated in the block.

Steps:
1. Find and group connected non-zero positions.
2. For each group:
    - Extract the block defined by the group.
    - Find non-4 elements and their value.
    - Add a frame around the block with thickness equal to the count of non-4 elements.
    - Place the framed block back into the output grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_52fd389e as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "52fd389e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
