"""Transform grid by extracting inner content and swapping corner and adjacent values.

Concepts:
- Grid transformation: Extracting inner region while preserving corners
- Pattern manipulation: Moving values between specific positions
- Corner preservation: Maintaining original corner values

Transformation Steps:
1. Extract the inner block of the grid (all but outer border)
2. For each corner position, copy its value to the adjacent cross position
3. Replace corner values with those from the original grid

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_ca8de6ea as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "ca8de6ea"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
