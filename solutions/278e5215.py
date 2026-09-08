"""Concept: Subgrid extraction and column-wise filling based on a reference block.

Transformation Steps:
1. Extract the bounding box containing all 5s (defines the output region).
2. Identify the minimal block of non-5, non-0 values (used for fill colors).
3. Use the bottom row of this block as the background reference.
4. For each column in the cropped 5-region, fill with the common value from the corresponding column in the block,
5. Replace all positions of 0s inside the cropped 5-region with the background value.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_278e5215 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "278e5215"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
