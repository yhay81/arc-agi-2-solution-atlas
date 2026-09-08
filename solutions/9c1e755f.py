"""Concepts: Block replication using guide row or column of a particular value (5).

Steps:
1. Identify connected blocks of non-zero cells, the process each block independently.
2. For each block, detect whether 5s form a boundary row or column.
3. Extract the interior piece (non-0, non-5 values).
4. Replicate the piece across the block in the direction suggested by the 5s.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_9c1e755f as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "9c1e755f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
