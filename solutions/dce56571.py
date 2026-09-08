"""Count non-background cells in the input grid and draw a centered horizontal line of that color and size in the middle row of the output grid
initialized with the background color.

Concept:
- frequency (number of occurrences) analysis
- count non-background cells
- draw centered horizontal line of that color and size in middle row

Transformation Steps:
    1. Identify the background color and the non-background color.
    2. Count the number of non-background colored cells.
    3. Create the output grid with the background color.
    4. Create a horizontal line of the non-background color in the middle row.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_dce56571 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "dce56571"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
