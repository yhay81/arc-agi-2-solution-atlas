"""Concepts:
- Connected component detection (flood fill)
- Symmetry-based reflection and value assignment

Transformation steps:
1. Find all connected components of cells with value 3.
2. For each component, determine if the "extra" cell is along a row or column edge.
3. Reflect the component across the axis opposite the extra cell, with an extra gap.
4. Assign value 8 for row-based reflections, and 1 for column-based reflections.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_dc2e9a9d as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "dc2e9a9d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
