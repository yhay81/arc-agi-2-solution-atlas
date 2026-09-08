"""Concepts: Counting and marking based on cell values.

Steps:
1. Count the number of cells with value 8 and value 2.
2. Compute the difference (num_5s = num_8s - num_2s).
3. Fill the last 'num_5s' rows in the second-to-last column with 5.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_37ce87bb as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "37ce87bb"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
