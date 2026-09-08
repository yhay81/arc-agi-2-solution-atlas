"""Concepts: ring detection, interior filling

Steps:
1. Identify connected rings of 2s.
2. Compute bounding box and radius of each ring.
3. Fill the enclosed interior with a value based on radius,
   while preserving the original center cell as it carries 2.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_00dbd492 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "00dbd492"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
