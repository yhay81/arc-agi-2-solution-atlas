"""Concepts: 2D grid manipulation, mirroring, Pattern filling

Transformation steps:
1. Split the input grid into left and right halves.
2. Find all positions of the color '2' in the left half.
3. Identify the last column position of '2' in the left half.
4. Create a copy of the left half input grid for output.
5. For each row with '2' in the last column, fill all cells to the right with '2'.
6. Mirror the left half to create the right half.
7. Combine the left and right halves to form the output grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_5ad8a7c0 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "5ad8a7c0"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
