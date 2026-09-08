"""Extracts two connected nonzero blocks from the grid, compares them,
and outputs the minimal bounding subgrid highlighting differences.

Steps:
1. Identify connected nonzero components using `group_connected_positions`.
2. Extract bounding blocks for each component.
3. Compute elementwise difference between the two blocks.
4. Extract the minimal subgrid containing differences.
5. Return a grid filled with marker value (8) for differing positions.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_2037f2c7 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "2037f2c7"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
