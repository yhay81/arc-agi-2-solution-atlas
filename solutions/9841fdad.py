"""Concepts:
- Identify columns with unique values that act as separators.
- Extract a reference block and a placeholder block separated by these columns.
- Find patterns in the reference block and apply corresponding transformations
  to the placeholder block based on their positions and dimensions.

Steps:
1. Find columns with unique values (separators).
2. Extract reference block and placeholder block.
3. Find connected components of non-1 values in the reference block.
4. For each component:
    - If it's a square:
        - If near left boundary, copy it to left side of placeholder block.
        - If near right boundary, copy it to right side of placeholder block.
    - If it's wider than tall, extend it across the placeholder block with same height.
5. Update the output grid with the modified placeholder block.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_9841fdad as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "9841fdad"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
