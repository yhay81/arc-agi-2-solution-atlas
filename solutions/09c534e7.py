"""For each connected nonzero region, fill its interior (cells fully surrounded by nonzero values)
with the least frequent nonzero color in that region.

Concepts:
- Connected component analysis
- Interior detection via 8-neighborhood
- Frequency analysis within a region

Transformation Steps:
1. Find all connected groups of nonzero cells.
2. For each group, determine the least frequent nonzero color.
3. Identify interior positions (not on border, all 8 neighbors nonzero).
4. Fill interior positions with the chosen color.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_09c534e7 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "09c534e7"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
