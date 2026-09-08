"""Concepts:
- Use value 2 at the top and left edges as position markers.
- Divide the grid into four quadrants based on these markers.
- Rearrange the quadrants by rotating them to create the output_grid

Steps:
1. Remove the first row and column (border).
2. Find the positions of markers (value 2) to determine quadrant sizes.
3. Split the grid into four quadrants.
4. Rearrange the quadrants in a new configuration.
5. Return the rearranged grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_79cce52d as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "79cce52d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
