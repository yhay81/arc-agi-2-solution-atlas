"""Patern matching and 3x3 block fitting.

Concepts:
- Component extraction: Identifies connected regions of non-zero values
- Block prioritization: Uses the largest block as the base grid for output
- Pattern fitting: Places smaller blocks in the output grid if patterns match (positions of 0s in the output grid match positions of 2s in the block)
- Rotation matching: Rotates blocks to fit into available spaces

Steps:
1. Identify all connected non-zero components in the input grid
2. Find the largest component to use as the base output grid
3. Extract all other components as blocks to be placed
4. Sort blocks by number of 2's they contain (descending)
5. Place each block in available spaces where they fit/match (positions of 0s in output match positions of 2s in block)

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_97a05b5b as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "97a05b5b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
