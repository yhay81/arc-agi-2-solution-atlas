"""Transform nested rectangular frames by reversing their color values.

Concepts:
- Connected component analysis: Group adjacent non-zero cells, each group is made of nested rectangular frames
- Pattern recognition: Identify nested rectangular frames colors (values)
- Color transformation: Reverse the order of colors from outer to inner frame

Transformation steps:
1. Find connected components of non-zero values
2. For each component:
    a. Extract the rectangular block containing the component
    b. Identify unique colors from outer to inner frame
    c. Reverse the color ordering and apply to frames

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_8dae5dfc as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "8dae5dfc"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
