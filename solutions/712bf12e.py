"""Simulates the movement (towards top or right) of entities (value 2) through a grid with empty spaces (value 0)
and blockers (value 5).

Concept:
Entities move according to specific rules: first try to move upward, and if blocked,
try to move right. Continue movement until getting stuck or hitting the top edge of the grid.

Transformation Steps:
1. Identify all entities (value 2) in the grid
2. For each entity, simulate movement according to the rules:
   a. First try to move up one cell if empty (value 0)
   b. If blocked above (value 5), try to move right if empty
   c. If blocked in both directions, entity stops moving
3. Continue movement until entity reaches top boundary or gets stuck

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_712bf12e as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "712bf12e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
