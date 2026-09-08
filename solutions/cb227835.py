"""Identifies two 8s in the input grid that are closest to opposite corners,
then connects them with lines of 3s to form a boundary structure.

Concepts:
- Pattern recognition: Identifying 8s positioned near opposite corners
- Boundary creation: Connecting corner elements with straight lines to form a boundary structure.
- Grid transformation: Converting elements along line to value (color) 3

Transformation Steps:
1. Find all positions containing value 8 in the input grid
2. Identify if 8s are positioned along main diagonal (top-left to bottom-right)
   or anti-diagonal (top-right to bottom-left)
3. Draw lines of 3s connecting the 8s:
   a. Along diagonal paths between the 8s
   b. Vertically/ horizontally from 8s to form a boundary structure.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_cb227835 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "cb227835"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
