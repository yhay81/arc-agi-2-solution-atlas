"""Find a column containing all 2s and create a binary output grid based on merging
the regions separated by this column.

Concepts:
- Column-based partitioning: Identifying a dividing column with value 2
- Region merging: Combining data from separate regions of the grid
- Binary transformation: Converting to 1s where either region had non-zero values

Transformation Steps:
1. Identify the column where all values equal 2 (partition column)
2. Split the grid into left and right parts, excluding the partition column
3. Add corresponding elements from both parts
4. Create a binary output where any non-zero sum becomes 1

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_195ba7dc as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "195ba7dc"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
