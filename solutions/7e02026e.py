"""Find and fill '+' shaped free spaces (all 0s) with 3s

Concepts:
- Pattern detection
- Region filling

Transformation Steps:
1. Scan the grid for '+' shaped regions where all five cells are free (with 0s).
   The '+' shape consists of:
   - Center: (r+1, c+1)
   - Top: (r, c+1)
   - Bottom: (r+2, c+1)
   - Left: (r+1, c)
   - Right: (r+1, c+2)
2. For each such region, fill the entire '+' shape with 3s.
3. Return the modified grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_7e02026e as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "7e02026e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
