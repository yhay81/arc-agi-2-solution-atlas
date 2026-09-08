"""Removes noise (replacing 5's with 0's), detects square patterns in a grid separated by rows/columns of zeros,
and transforms these squares by either filling them with the most common value or replacing them with a reference pattern.

Concepts:
- Noise removal: Remove noise values (5's) from the grid
- Pattern detection: Find complete patterns in grid subsections (squares)
- Pattern transformation: Apply transformation rules to grid subsections (squares)

Transformation steps:
1. Remove noise by replacing 5's with 0's. grid is partitioned into squares by rows and columns of 0s
2. Identify square size using first all-zero row
3. Find a reference pattern from the square with non-zero values
4. Apply pattern transformation rules to each square (subsection):
   - If square contains the most frequent value from pattern, fill with that value
   - If square has no values matching the most frequent value, replace with pattern

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_6350f1f4 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "6350f1f4"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
