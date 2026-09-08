"""Concepts: Gift wrapping with ribbons - coloring rows and columns like tying ribbons on gift boxes.

Transformation steps:
1. Identify connected regions of value 3 (ribbon flowers).
2. For each region, compute its center point (flower middle).
3. From each center, extend its value horizontally, then vertically.
4. Stop extension when another flower (3) is encountered or at grid boundary.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_f8be4b64 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "f8be4b64"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
