"""Concepts:
    - Frame detection
    - Diagonal 2x2 block placement

Transformation: Replace the two corner-adjacent numbers outside a 5-frame with 2x2 blocks of the same values placed in the frame's diagonally.

Transformation steps:
1. Identify the outer frame of '5's in the grid.
2. Detect the nonzero values just outside each corner of the frame.
3. Place 2x2 squares of these values inside the frame along the diagonal that passes through the corner where the value was detected.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_94414823 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "94414823"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
