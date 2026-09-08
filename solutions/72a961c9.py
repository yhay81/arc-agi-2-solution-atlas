"""Concepts: Build columns (towers) of different heights above certain values (2 and 8).

Transformation steps:
1. Identify all positions of the value 8 in the input grid.
   - Replace the two rows above each position with 1s.
   - Set the value at three rows above to 8.
2. Identify all positions of the value 2 in the input grid.
   - Replace the three rows above each position with 1s.
   - Set the value at four rows above to 2.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_72a961c9 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "72a961c9"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
