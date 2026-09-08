"""Concepts: constant row/column, tiling, alignment

Transformation steps:
1. Find the fully constant row or column in the input.
2. Tile the input three times along the perpendicular axis.
3. Place that strip in the block whose index matches the constant line.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.llm_task_solutions import solve_15696249 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "15696249"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
