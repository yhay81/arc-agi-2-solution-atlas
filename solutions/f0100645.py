"""Concepts: Stack parts on leftmost and rightmost sides based on their value (color).

Aligns horizontally separated connected components on the leftmost and rightmost sides
by shifting the nearest disconnected part toward the extreme part until they touch.

Trasformation steps:
1. Identify the unique values in the leftmost and rightmost columns.
2. For each side, while multiple connected components exist for that side's value:
   - Shift the closest non-extreme component horizontally until it touches the extreme component.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_f0100645 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "f0100645"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
