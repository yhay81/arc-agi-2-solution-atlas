"""Concepts: duplication, rotation, and stacking of blocks.

Transformation steps:
1. Duplicate the input grid to form a larger block (bottom-right).
2. Rotate this block to create top-right, top-left, and bottom-left blocks.
3. Assemble the four blocks into a new grid by stacking and concatenation.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_cf5fd0ad as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "cf5fd0ad"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
