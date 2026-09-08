"""Concepts:
- Identify blocks in the grid (areas not containing value 8).
- Extract the smallest meaningful sub-pattern within each block.
- Repeat this sub-pattern to fill the entire block.

Steps:
2. Find and group connected non-8 positions in the grid
3. For each group:
    - Extract the block defined by the group.
    - Find the smallest sub-pattern (non-zero elements) within the block.
    - Tile the sub-pattern to fill the entire block.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_a57f2f04 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "a57f2f04"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
