"""Centers blocks of 1s within squares defined by corners marked with 2s.

Concepts:
- Grid pattern centering
- Bounding box computation
- Shape repositioning

Transformation Steps:
1. Identify squares defined by 2s at their corners
2. Find a sub-block of 1s within each square
3. Center these blocks within their respective squares

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_20981f0e as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "20981f0e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
