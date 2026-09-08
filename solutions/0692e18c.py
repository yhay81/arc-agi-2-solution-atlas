"""Concepts: fractal copy, color inversion, indicator cells

Transformation steps:
1. Build a color-inverted copy of the input (nonzero becomes 0, 0 becomes the sprite color).
2. Scale the canvas by the input size.
3. Where the input cell is nonzero, paste the inverted sprite into that block.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.llm_task_solutions import solve_0692e18c as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "0692e18c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
