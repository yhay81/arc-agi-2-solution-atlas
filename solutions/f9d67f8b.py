"""Concepts: mirror symmetry detection and masked value filling based on mirror symmetry and rotation.

Transformation steps:
1. Detect vertical and horizontal mirror symmetry axes (if they exist).
2. Fill cells with the mask value (9) using their mirror counterparts along the symmetry axes.
3. If any mask values remain, apply rotation to fill them.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- ArunSehrawat/arc-agi2-solutions, distributed under the MIT License.
"""

import numpy as np

from arc_agi_2_atlas.providers.our_task_solutions import solve_f9d67f8b as _provider_solve
from arc_agi_2_atlas.types import Grid

TASK_ID = "f9d67f8b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("numpy", "arc-agi2-solutions")


def solve(grid: Grid) -> Grid:
    """Run the attributed provider program and normalize its output."""
    return np.asarray(_provider_solve(np.asarray(grid))).tolist()
