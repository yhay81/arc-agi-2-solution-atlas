"""Identify connected groups of non-zero values, remove solid blocks,
preserve hollow blocks, trim empty rows/columns, and stack the remaining blocks.

Concept:
- Connected non-zero regions are either solid (fully filled) or hollow (partially filled).
- Solid blocks are removed; hollow blocks are extracted and stacked vertically or horizontally
  based on the grid's aspect ratio.

Transformation Steps:
1. Identify all connected groups of non-zero positions in the input grid.
2. For each group, remove it if it forms a solid block (all cells non-zero).
3. Trim the output grid by removing rows and columns that are entirely zero.
4. Divide the trimmed grid into sections (assuming 4x4 blocks) and extract the bounding box of non-zero positions in each section.
5. Stack the extracted blocks vertically if the grid is taller than wide, or horizontally otherwise.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_a680ac02 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "a680ac02"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
