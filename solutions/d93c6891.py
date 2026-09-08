"""Concepts: Filling 7-blocks using available 5s attached in the direction opposite to the wall of 0s.

Transformation steps:
1. Extract connected components, ignoring 0s and 4s.
2. For each component:
   - Identify bounding box of 7-blocks and count attached 5s.
   - Fill the 7-block with 5s in the direction opposite to the wall of 0s.
   - Change original 5s to 4s.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_d93c6891 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "d93c6891"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
