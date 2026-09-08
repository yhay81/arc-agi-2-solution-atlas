"""Create concentric square frames of non-background colors from outer to inner,
in the order of frequency of color in the input grid.

Concepts:
- Frequency analysis: Identify the most frequent color (background) and order other colors by frequency.
- Frame drawing: Draw square frames for each non-background color, from outermost to innermost.
- Grid resizing: Output grid size depends on the number of unique non-background colors.

Transformation Steps:
1. Identify the most frequent color in the input grid (background color).
2. Determine the unique non-background colors and their frequencies.
3. Create an output grid sized to fit all frames (size = 2 * num_non_background_colors - 1).
4. Draw concentric square frames for each non-background color in descending order of frequency.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_5587a8d0 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "5587a8d0"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
