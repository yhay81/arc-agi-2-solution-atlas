"""Concept:
Identify the non-8  (non-background) value in the grid and extend it from its position to the closest corner,
filling a rectangular region.

Steps:
1. Find the unique non-8 (non-background) value in the grid.
2. Locate the position of this value.
3. Determine which corner is closest to this position.
4. Fill a rectangular region from the value's position to the closest corner with this value.
5. Return the modified grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_4a1cacc2 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "4a1cacc2"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
