"""Identify vertical blocks separated by background columns.
For each block, fill its background cells with the unique color from the next block (cyclically).

Concept:
- block partitioning
- changing background color in each block to the non-background color of the next block (establishing a cyclic relationship between blocks).

Transformation Steps:
    1. Detect background color (most frequent value).
    2. Find columns that are entirely background (partition columns).
    3. Split the grid into blocks between partition columns.
    4. For each block, fill its background cells with the unique color from the next block.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_c4d1a9ae as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "c4d1a9ae"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
