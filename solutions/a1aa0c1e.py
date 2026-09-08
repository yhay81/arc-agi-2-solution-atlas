"""Summarize heights of non-zero values (excluding 0, 5, 9) in the grid.

Concepts:
- Pattern detection: Identify specific values and their locations
- Bounding box calculation: Find boundaries of value regions
- Value filtering: Exclude specific numbers from analysis
- Position tracking: Record minimum row positions for ordering

Transformation steps:
1. Extract unique values (excluding 0, 5, 9)
2. Create output grid based on unique value count
3. For each value:
    a. Find positions and bounding box
    b. Calculate minimum row position
    c. Order values by minimum row position
4. Fill output grid based on ordered values
5. Add special handling for value 5

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_a1aa0c1e as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "a1aa0c1e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
