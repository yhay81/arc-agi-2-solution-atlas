"""Identifies and returns the unique connected component from the input grid.

Concepts:
- Connected component analysis
- Pattern uniqueness detection
- Shape extraction

Transformation Steps:
1. Find non-zero positions and group them into connected components
2. Extract each component as a rectangular block
3. Return the block with a unique pattern

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_cd3c21df as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "cd3c21df"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
