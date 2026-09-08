"""Concepts: color flipping, grid partitioning, and connected component analysis.

Transformation steps:
1. Initialize output with background (8).
2. Flip non-background colors.
3. Split into top and bottom halves around the vertical midpoint of non-background cells.
4. Shift the top half horizontally until top+bottom form more than one connected component.
5. Return the last valid connected configuration.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_fc4aaf52 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "fc4aaf52"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
