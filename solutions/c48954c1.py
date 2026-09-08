"""Unfolding Symmetric Pattern
Creates a symmetric pattern by mirroring the input grid in multiple directions.

Concepts:
- Reflective symmetry: Creates horizontal and vertical reflections of the input grid
- Tiling: Combines the original grid with its reflections to create a larger pattern
- Self-similarity: Generates a fractal-like structure with the input repeated in a pattern

Transformation steps:
1. Create a horizontal reflection of the input grid (left-right flip)
2. Construct a middle row by placing the original grid between two of its horizontal reflections
3. Create vertical reflections (top-bottom flips) of this middle row
4. Stack these three rows (reflection, original middle row, reflection) to create a 3x3 tile pattern

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_c48954c1 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "c48954c1"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
