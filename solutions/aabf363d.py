"""Executable re-arc DSL program for ARC-AGI-2 task aabf363d.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.re_arc_dsl import (
    argmax,
    compose,
    fork,
    height,
    lbind,
    leastcolor,
    multiply,
    ofcolor,
    other,
    palette,
    remove,
    replace,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "aabf363d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fork(multiply, height, width)
    x1 = lbind(ofcolor, grid)
    x2 = palette(grid)
    x3 = compose(x0, x1)
    x4 = argmax(x2, x3)
    x5 = leastcolor(grid)
    x6 = palette(grid)
    x7 = remove(x4, x6)
    x8 = other(x7, x5)
    x9 = replace(grid, x5, x4)
    x10 = replace(x9, x8, x5)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
