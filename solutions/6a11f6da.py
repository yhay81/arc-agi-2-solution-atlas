"""Concepts: grid partitioning into three parts, merged by overlapping.
Non-zero values overwrite zeros sequentially.

Steps:
1. Split input grid into 3 equal vertical sections.
2. Rearrange sections in order: last -> first -> second.
3. Build output by filling zeros with values from each section in sequence.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_6a11f6da as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "6a11f6da"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
