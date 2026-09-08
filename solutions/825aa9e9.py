"""Concepts:
- Identify connected components above a stopper row.
- Gravity: Drop each component downward until it lands on either a row above the stopper value
  or another identical component.

Steps:
1. Find stopper value from bottom row (other than background value 7).
2. Collect connected components (excluding 7 and stopper).
3. Process components from bottom to top.
4. Drop each component until it meets stopper or same value.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_825aa9e9 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "825aa9e9"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
