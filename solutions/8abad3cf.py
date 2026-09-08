"""Arranges non-background colors as squares in a horizontal row, sized by the square root of their frequency,
with background separators, and flips the result vertically to match the expected orientation (so that they touch the bottom).

Concept:
- The grid contains a background color (most frequent) and other colors representing elements.
- Each non-background color is represented as a square block, where the side length is the integer square root of its count.
- Blocks are placed side by side with background separators, and the entire arrangement is flipped upside down.

Transformation Steps:
1. Identify unique colors and their frequencies in the input grid.
2. Sort colors by frequency in ascending order.
3. Determine the background color as the most frequent.
4. For each non-background color, compute its block size as the integer square root of its count.
5. Create a new grid with height equal to the largest block size and width as the sum of block sizes plus separators.
6. Place each block in the grid with background spacing between them.
7. Flip the grid vertically to achieve the final orientation (so that they touch the bottom).

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_8abad3cf as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "8abad3cf"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
