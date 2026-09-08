"""Concepts: Connected component matching based on their shapes.

Fill the color (value) in the left part based from the right part by matching shapes.

Transformation steps:
2. Split the grid into left and right parts.
3. Extract connected components from the right part with their values and normalize their positions.
4. Match shapes and transfer values from the right part to corresponding empty spaces in the left part.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_93b4f4b3 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "93b4f4b3"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
