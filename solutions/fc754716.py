"""Find center color (value) in the input grid and create a frame around it of the same color.

Concepts:
- Center identification: Locating the center cell of a grid
- Value extraction: Retrieving the color/value from the center position
- Frame creation: Using the extracted value to create a border around the entire grid
- Value replacement: Setting the center position to 0 (background)

Transformation Steps:
1. Extract the value from the center cell of the input grid
2. Replace the center cell value with 0
3. Create a frame/border around the entire grid using the center value

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_fc754716 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "fc754716"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
