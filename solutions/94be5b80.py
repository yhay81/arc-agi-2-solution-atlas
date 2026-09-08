"""Concept:
Align and stack identical-shaped objects vertically in a grid
based on a reference ordering.

Transformation Logic:
1. Identify connected components of non-zero values using connected component analysis.
2. Find the component that contains all unique non-zero values.
   - This component is used as the "reference order" of objects.
   - Remove this reference component from the grid.
3. Identify the other component(s) that only contain a subset of the values.
4. Reorder these subset components to match the reference order.
5. Stack missing objects above and/or below the subset so the final arrangement
   reproduces the full ordered stack vertically.

Effect:
- The grid is transformed so that all identical-shaped objects appear stacked
  on top of each other in the correct order, as dictated by the reference.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_94be5b80 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "94be5b80"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
