"""Concepts: Bounding box detection, Subgrid extraction, Unique value identification,
Anchor-based positioning, Canonical mapping (normalization to 2x2 grid

Transformation steps:
1. Find the bounding box of all cells with value 8.
2. Extract the block within this bounding box.
3. Identify all unique values in the block that are not 8.
4. For each unique value, find its top-left position in the block.
5. Place each value in the corresponding corner of a 2x2 output grid:
   - Top-left, Top-right, Bottom-left, Bottom-right.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_19bb5feb as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "19bb5feb"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
