"""Concepts: Grid cleaning, fill (colored) the closest corner with identified value (color)

Steps:
1. Create a blank output grid filled with 6 (Grid cleaning)
2. Find the position of value 2.
3. Calculate distances from this position to all four corners.
4. Identify the closest corner.
5. Fill a 2x2 block in that corner with value 2.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_87ab05b8 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "87ab05b8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
