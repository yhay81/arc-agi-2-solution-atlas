"""Connects two same-color blocks by drawing a diagonal line between their nearest corners.

Concept:
    - For each non-background color, find all connected groups (expecting exactly two).
    - If there are exactly two groups, connect their bounding box corners with a diagonal line.

Transformation Steps:
    1. Identify background and non-background colors.
    2. For each non-background color, find connected groups (blocks)
    3. If there are exactly two blocks, compute their bounding box corners.
    4. Draw a diagonal line between the appropriate corners.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_342ae2ed as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "342ae2ed"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
