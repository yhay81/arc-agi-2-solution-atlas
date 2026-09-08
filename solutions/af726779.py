"""Creating inverted triangles of alternating colors (7 and 6).

Concept:
For each row containing a specific value (top_value), identify pairs of adjacent occurrences
and place another value (bottom_value) two rows below in the middle column between those pairs.
This process is repeated alternating between two different values.

Transformation Steps:
1. Scan the grid from bottom to top to find rows containing the target value (top_value)
2. Identify pairs of adjacent occurrences of this value in the row
3. For each pair, place another value (bottom_value) two rows below in the middle column
4. Alternate this process between two different values (7->6 and 6->7)

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_af726779 as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "af726779"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
