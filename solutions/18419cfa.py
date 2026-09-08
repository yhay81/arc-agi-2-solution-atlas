"""Concepts:
- Detect connected components of value 8 that form mirror frames.
- For each component, determine mirror orientation by 8's distribution.
- Create the mirror image by flipping and combining with the original.

Steps:
1. Convert input to numpy array.
2. Find all positions containing value 8.
3. Group connected positions of 8s (mirror frames).
4. For each group:
    - Determine orientation (horizontal/vertical) by 8's distribution.
    - Apply the appropriate flip (horizontal/vertical).
    - Combine original and flipped block using maximum values to fill the empty places of 0s.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_18419cfa as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "18419cfa"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
