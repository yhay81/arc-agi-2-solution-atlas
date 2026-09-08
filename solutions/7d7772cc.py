"""Detects a bracket-shaped frame (any 90° rotation) extending fully along the grid boundary
moving special values toward the frame or opposite edge if match is found or not.

Concepts:
- Frame detection: Identifies bracket-like frames using grid boundaries
- Value classification: Distinguishes between background, frame, and special values
- Spatial transformation: move toward the frame or opposite edge if match is found or not.

Transformation steps:
1. Identify the frame value, its inner and outer background values
2. Find the boundary coordinates of the frame
3. For each direction (top, bottom, left, right):
   - If a special value appears once in a row/column, move it to the frame edge
   - If multiple special values appear, move them to the grid edge

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_7d7772cc as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "7d7772cc"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
