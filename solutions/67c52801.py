"""Rearranges colored blocks from the top part to the bottom part by matching their widths to available (background) spaces.

Concept:
    - Identify colored blocks in the upper part of the grid.
    - Identify contiguous background spaces in the bottom two rows.
    - Place each colored block into a matching-width background space, rotating if necessary.

Steps:
    1. Identify the background color (most frequent).
    2. Find contiguous background spaces in the bottom two rows.
    3. Extract colored blocks from the top rows.
    4. Sort background spaces and blocks by width (descending).
    5. Place each block into a matching-width space, rotating if needed.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_67c52801 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "67c52801"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
