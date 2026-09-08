"""From the corners, select the blocks of the same color that occurs the most.
Moves the colored blocks from their corner positions toward opposite corners.

Concept:
    - Identify the background color as the most frequent color.
    - Among non-background colors, select the one with the highest number of connected groups.
    - For each connected group of that color, erase it from its original position and move the block toward the opposite corner.

Steps:
    1. Determine background color and non-background colors.
    2. Find the non-background color with the most connected groups.
    3. For each group of that color, erase the block and place it in the opposite corner if it fits.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_22208ba4 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "22208ba4"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
