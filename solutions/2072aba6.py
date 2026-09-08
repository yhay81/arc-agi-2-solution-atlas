"""Concepts:

Transformation steps:
1. Initialize an output grid of size (2xnrows, 2xncols) filled with zeros.
   - This will be twice the size of the input grid.
2. For each cell in the input grid,
   - if it contains non-zero value 5, replace the corresponding block in the output grid with 2x2 non-zero block [[1, 2], [2, 1]].

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_2072aba6 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "2072aba6"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
