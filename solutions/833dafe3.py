"""Concepts: dihedral kaleidoscope, rotation, reflection

Transformation steps:
1. Place rot180(input) in the top-left quadrant.
2. Place flipud(input) top-right, fliplr(input) bottom-left, and the original bottom-right.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.llm_task_solutions import solve_833dafe3 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "833dafe3"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
