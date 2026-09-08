"""Create a summary grid showing the number of connected components for each value (color).

Concepts:
- Connected component analysis: Group adjacent cells with same value
- Component counting: Track number of distinct connected regions per value
- Create a summary grid showing the number of connected components for each value (color).

Transformation steps:
1. Find all non-zero values in the input grid
2. For each value, count its connected components
3. Sort values by number of components (descending)
4. Create output grid where:
   - Each row represents a unique value as per the sorted list
   - Row length equals max number of components for that value
   - Values are right-aligned based on component count

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_2753e76c as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "2753e76c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
