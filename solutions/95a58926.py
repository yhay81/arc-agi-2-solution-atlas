"""Transform a grid by removing noise and creating a regular partitioning pattern.

Concepts:
- Pattern cleaning: Remove noise cells while preserving structural elements
- Grid partitioning: Create regular grid divisions with horizontal and vertical lines
- Intersection marking: Place special markers at line intersections

Transformation steps:
1. Remove noise cells (non 0 and non 5) from the grid
2. Determine the size of partitioning blocks by finding first line marker
3. Create regular horizontal and vertical partition lines
4. Place noise value markers at line intersections

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_95a58926 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "95a58926"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
