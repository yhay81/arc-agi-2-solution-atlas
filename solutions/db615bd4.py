"""Identifies a frame in the grid, extracts colored blocks outside the frame,
solidifies them (makes all cells the same color), and arranges them inside
the frame in the order they appear, either vertically or horizontally based
on the frame's aspect ratio.

Concept:
- The grid contains a frame (most frequent color after backgrounds), blocks
  of other colors outside the frame, and backgrounds.
- Blocks are solidified to their dominant color and placed inside the frame
  in a stacked arrangement, preserving their order of appearance.

Transformation Steps:
1. Identify background colors (most and second most frequent) and frame color (third most frequent).
2. Locate the frame's bounding box and complete it in the output grid.
3. Clear the inside of the frame.
4. Collect blocks outside the frame, solidify them, and remove them from the input.
5. Stack the blocks vertically or horizontally (based on frame height > width) with separators.
6. Center the stacked arrangement inside the frame.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_db615bd4 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "db615bd4"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
