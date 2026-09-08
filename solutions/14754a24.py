"""Concepts: Cross (+) shape detection and completion.

Transformation steps:
1. Identify positions with value 4 and group them into connected components (8-connectivity).
2. For each component, determine possible 3x3 boxes that can contain the cross shape.
3. Identify missing positions in the cross shape and fill them with value 2 if the surrounding positions are valid (value 5).

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_14754a24 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "14754a24"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
