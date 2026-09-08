"""Concepts: grid partitioning with connectors.

Steps:
1. Find the first row and column fully filled with 8s (block size).
2. Partition the grid into blocks of this size.
3. Identify blocks containing 2 or 3.
4. Connect same-valued blocks horizontally/vertically by filling paths.
5. Overlaps of 2 and 3 become 6.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_e760a62e as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "e760a62e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
