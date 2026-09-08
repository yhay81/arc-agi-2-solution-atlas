"""Concepts: Grid partitioning into rule part (top) and work part (bottom), rule: vale to 3x3 block mapping, in-place replacement.

 Transformation Summary
 a. The input grid is divided into two parts:
    - Top part (before the first full row of 6s):
      This part provides mapping rules: each rule consists of a 1x1 value and its corresponding 3x3 block (pattern).
    - Bottom part (after the row of 6s): This is where the replacement happens.
       Each 1x1 value is replaced with its corresponding 3x3 block, as defined in the top part.
 b. The replacement happens in-place in the bottom grid:
    - At each cell in the bottom part: if the value is one of the mapping values, replace it with the corresponding 3x3 block centered at that cell.
    - The output grid is constructed with these replaced blocks (note: blocks can overwrite each other; latest ones persist).

Transformation steps:
1. Find the dividing row (partition row full of 6s). The background is represented by 7s.
2. Extract rule part (top) and work part (bottom)
3. Get 3 pairs of 3x3 block and value from the rule part.
4. For each cell in the bottom part of the grid, if it matches a mapped value, replace it with the corresponding 3x3 block centered at that cell.
5. Construct the output grid with these replacements, ensuring to fill in the background (7s) where no replacements occur.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_20fb2937 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "20fb2937"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
