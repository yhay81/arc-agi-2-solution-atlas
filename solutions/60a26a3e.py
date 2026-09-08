"""Concepts: object of certain shape and it center detection, line filling, connecte component.

Transformation steps:
1. Find all positions with value 2 and group them into connected components (8-connectivity).
2. For each component, compute its center.
3. For all centers sharing the same row, fill horizontal lines between them with value 1 (excluding endpoints).
4. For all centers sharing the same column, fill vertical lines between them with value 1 (excluding endpoints).

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_60a26a3e as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "60a26a3e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
