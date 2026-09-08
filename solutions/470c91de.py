"""Move colored blocks diagonally based on the position of the marker (color 8).

Concept:
    - Extract colored blocks from the input grid.
    - Detect marker positions (color 8) at a block's corner.
    - Move the entire block one step diagonally in the direction of the marker.

Transformation Steps:
    1. Identify the background value (most frequent in the grid).
    2. For each unique value (excluding background and marker 8):
        a. Find the minimal bounding block carrying the value (color).
        b. In the block, find the marker (color 8) position.
        c. Move the block one step diagonally based on the marker's position and remove the marker.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_470c91de as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "470c91de"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
