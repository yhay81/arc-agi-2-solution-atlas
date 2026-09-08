"""Concepts: Two halves of a grid, Double controlled gate logic using two halves of a grid

Transformation steps:
1. Split the grid into top_half and bottom_half
Looing at training examples, we see that:
 - there are two halves of a grid, each have two unique values (0, 4) and (9, 0).
 - the following mapping
2. For each cell in the top_half, pair it with the corresponding cell in the bottom_half.
3. Use a mapping to determine the output value for each cell based on the pair:
   - (0, 0) -> 0
   - (0, 4) -> 6
   - (9, 0) -> 6
   - (9, 4) -> 0
4. Construct the output grid using these mapped values.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_31d5ba1a as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "31d5ba1a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
