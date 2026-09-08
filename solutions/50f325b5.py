"""Concepts: Pattern growth, template matching, multi-directional filling.

Transformation steps:
1. Identify all positions with value 8 and normalize their coordinates.
2. For each possible placement in the grid, check if the normalized template fits and is surrounded by value 3.
3. If so, fill the template region with 8.
4. Repeat the process after rotating and transposing the grid to cover all directions.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_50f325b5 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "50f325b5"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
