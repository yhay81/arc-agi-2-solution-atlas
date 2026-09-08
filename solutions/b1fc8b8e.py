"""Concepts: topology, pattern recognition, pattern extraction, spatial reasoning

# In the input grid, 8s are either making four 2x2 square or four flipped L shapes.
# if they are squares, then number of 8s will be 4*4 = 16
# if they are flipped L, then number of 8s will be 3*4 = 12
# based on that we can form a 5x5 output grid with four squares or flipped L shapes at the corners.

Transformation steps:
1. Initialize a 5x5 output grid with zeros.
2. Count the number of 8s in the input grid.
3. If there are 16 8s, they form four squares at the four corners of the output grid.
   If there are 12 8s, they form four flipped L shapes at the four corners of the output grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_b1fc8b8e as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "b1fc8b8e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
