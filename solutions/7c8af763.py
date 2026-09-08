"""Concepts: leakage from the neighboring values (colors) into the empty compartments
- Find connected components of zeros in the grid, these are empty compartments.
- For each component, examine neighboring values.
- Fill the zero regions with the most common neighboring value out of 1 and 2.

Steps:
1. Find all positions containing zero.
2. Group connected zero positions.
3. For each group:
    - Determine the boundary of the zero region.
    - Collect all neighboring values around the boundary.
    - Count occurrences of values 1 and 2 among neighbors.
    - Fill the zero region with the more frequent value out of 1 and 2.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_7c8af763 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "7c8af763"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
