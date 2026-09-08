"""Concept:
Transform an input grid by identifying straight lines and non-line objects, then:
- Create an output grid with background color 7
- Place non-line objects at the line endpoints
- Connect all centers of non-line objects with lines

Transformation Steps:
1. Identify background color (hard coded here as 7) and initialize empty output grid
2. Classify objects in the input grid as either lines or non-line objects
3. Extract line endpoints and non-line object patterns
4. Place non-line objects at the line endpoints in the output grid
5. Draw lines connecting all non-line object centers
6. Return the transformed output grid

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_c6141b15 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "c6141b15"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
