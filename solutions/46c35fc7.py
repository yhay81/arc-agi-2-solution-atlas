"""Concepts: Connected component extraction, block rotation, selective masking.

Transformation steps:
1. Identify non-background regions using connected components.
2. For each 3x3 block, mask and rotate corners and edges separately.
3. Combine rotated blocks and restore the center value.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_46c35fc7 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "46c35fc7"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
