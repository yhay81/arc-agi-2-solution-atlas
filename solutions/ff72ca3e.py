"""Concepts: BFS region growth, obstacle blocking.

Breadth-First Search (BFS) - it's a graph traversal algorithm.
In simple terms:
You start at a point (like your 4 cell).
You visit all the neighbors at distance 1 first,
Then all neighbors at distance 2,
And so on - layer by layer.

It's like dropping a pebble in water - the ripples expand outward evenly,

Transformation steps:
1. For each cell containing the value 4, expand outward.
2. Mark expansion cells with the value 2 until a cell containing 5 is reached, which blocks further growth.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_ff72ca3e as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "ff72ca3e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
