"""Rearranges grid blocks based on their content of value 2 from right to left, top to bottom row-wise.

Concepts:
- Block detection: Identifies grid partitions separated by rows of zeros
- Content analysis: Counts occurrences of value 2 in each block
- Spatial reorganization: Rearranges blocks by descending count in right-to-left order

Transformation steps:
1. Identify grid partitioning by detecting rows of zeros
2. Extract individual blocks from the partitioned grid
3. Count occurrences of value 2 in each block
4. In the output grid, rearrange blocks in descending order of value 2 count from right to left, top to bottom row-wise

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_dc2aa30b as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "dc2aa30b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
