"""Place the most frequent value from the top block and put it in the center of the last row.

Concepts:
- Grid partitioning
- Frequency analysis
- Value placement

Transformation Steps:
1. Partition the input grid into top and bottom blocks using the middle row of 5s as a separator.
2. Find the most frequent value in the top block.
3. Place this value in the center cell of the last row of the output grid.
4. Return the modified output grid.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_27a77e38 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "27a77e38"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
