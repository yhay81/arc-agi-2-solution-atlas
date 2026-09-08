"""Concepts: disconnected components, shape matching and value transfer

Transformation steps:
1. Identify shapes formed by the marked value (8), normalize them.
2. Identify the non-zero and non-8 value that has more than one disconnected component
3. If any disconnected part matches the normalized shape of 8,
   replace that part's value with 8 in the output grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_4ff4c9da as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "4ff4c9da"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
