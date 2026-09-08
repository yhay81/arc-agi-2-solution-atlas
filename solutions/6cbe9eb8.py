"""Concepts:
- Detect and extract rectangular frames (may be given in parts) or rectangular filled region.
- Put these frames/filled regions into each other like russian dolls.

Steps:
1. Identify unique values in the input grid.
2. For each unique value, determine if it forms a rectangular frame or a filled rectangle.
3. Sort the identified frames/filled rectangles by size (area).
4. Create an output grid that nests the largest rectangle first, followed by smaller ones
   in a top-left aligned manner.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_6cbe9eb8 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "6cbe9eb8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
