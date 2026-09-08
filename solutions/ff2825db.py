"""Draws two frames using the most frequent nonzero value in the interior of the grid:
- An inner frame around the bounding box of the most frequent value in the interior.
- An outer frame (excluding the first row) using the same value.

Concepts:
- Frequency analysis in a subgrid
- Bounding box detection
- Frame drawing

Transformation Steps:
1. Extract the interior (excluding first two rows and first/last columns).
2. Find the most frequent nonzero value in the interior.
3. Find the bounding box of this value in the interior.
4. Clear the interior region totally.
5. Draw an inner frame around the bounding box using the detected value.
6. Draw an outer frame (excluding the first row) using the same value.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_ff2825db as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "ff2825db"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
