"""Transform shapes by moving rectangles to stick ends and filling gaps.

Concepts:
- Connected component analysis
- Rectangle detection and extraction
- Directional movement based on stick position
- Gap filling in transformed shapes

Transformation steps:
1. Find all non-zero connected components (they will be overlapping rectangles with and without sticks)
2. For each component:
    a. Extract bounding box
    b. If contains gaps (stick), identify stick direction
    c. Move rectangle part to stick end
3. Fill any occurred gaps in the rectangles in output

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_c6e1b8da as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "c6e1b8da"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
