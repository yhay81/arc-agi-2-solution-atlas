"""Finds pattern bounded by frame of 5s and/or grid boundaries
draws a border of 5s around each matching pattern.

Concepts:
- Pattern detection: pattern bounded by frame of 5s and/or grid boundaries
- Pattern matching: Finding occurrences of patterns within a grid
- Border creation: Drawing borders around identified patterns

Transformation Steps:
1. Finds pattern bounded by frame of 5s and/or grid boundaries
    - Find all positions containing 5s
    - Group connected 5s together
    - Identify the largest group of connected 5s as the frame
    - Identify the pattern within this frame
2. Search for all occurrences of this pattern in the grid
3. Draw a border of 5s around each pattern occurrence

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_e2092e0c as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "e2092e0c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
