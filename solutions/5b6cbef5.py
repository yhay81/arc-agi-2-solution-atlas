"""Create a larger grid by tiling the input grid based on non-zero cells. (similar to Koch curve)

Concept:
- non-zero cell analysis
- tiling with input grid

Transformation Steps:
    1. Initialize a large output grid of size (nrows**2, ncols**2).
    2. For each non-zero cell in the input grid, copy the entire input grid into the corresponding tile in the output grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_5b6cbef5 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "5b6cbef5"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
