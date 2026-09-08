"""Concepts: The Galton board - filling columns based on a reference row and a pivot point.

Transformation steps:
1. Identify a pivot column using the value 8 in the bottom row
2. Count the number of 8s in the pivot column to determine fill depth
3. Use the top row as a reference for values (colors) to fill into columns
4. Fill values from the bottom up based on distance from pivot
5. Replace the top reference row with background value 5

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_bae5c565 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "bae5c565"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
