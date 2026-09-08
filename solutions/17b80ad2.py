"""Fills columns upward from bottom markers (color 5), changing color when a non-zero cell is encountered.

Concept:
    - Markers are given in the bottom row with color 5.
    - For each marker column, fill upwards with the current color.
    - When a non-zero color is encountered, update the fill color to that value.

Transformation Steps:
    1. For each column, if the bottom cell is a marker (5), fill upwards.
    2. At each step, if the input cell is zero, fill with the current color.
    3. If a non-zero cell is encountered, update the current color to that value and continue.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_17b80ad2 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "17b80ad2"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
