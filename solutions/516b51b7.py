"""Find rectangles of connected 1s and convert them into nested frames with alternating values.

Concepts:
- Rectangle detection: Identify boundaries of connected 1s in input grid
- Frame generation: Create concentric frames with alternating value pattern
- Pattern application: Apply values 1->2->3->2 from outside to inside

Transformation steps:
1. Convert input to numpy array
2. Find positions of all 1s in the grid
3. Group connected 1s into rectangles
4. For each rectangle:
   a. Determine boundaries (min/max row/column)
   b. Calculate how many nested frames fit inside
   c. Fill frames from outside to inside with pattern [1,2,3,2]
5. Return the transformed grid

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_516b51b7 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "516b51b7"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
