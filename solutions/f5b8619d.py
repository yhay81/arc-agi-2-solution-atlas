"""Executable re-arc DSL program for ARC-AGI-2 task f5b8619d.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    fgpartition,
    hconcat,
    mapply,
    toindices,
    underfill,
    vconcat,
    vfrontier,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "f5b8619d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = mapply(toindices, x0)
    x2 = mapply(vfrontier, x1)
    x3 = underfill(grid, EIGHT, x2)
    x4 = hconcat(x3, x3)
    x5 = vconcat(x4, x4)
    return x5


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
