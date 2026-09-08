"""Executable re-arc DSL program for ARC-AGI-2 task 7f4411dc.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO_BY_TWO,
    F,
    T,
    apply,
    argmin,
    asobject,
    canvas,
    color,
    identity,
    lbind,
    mapply,
    matcher,
    mostcommon,
    objects,
    occurrences,
    paint,
    palette,
    shape,
    shift,
    totuple,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "7f4411dc"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = totuple(x0)
    x2 = apply(color, x1)
    x3 = mostcommon(x2)
    x4 = canvas(x3, TWO_BY_TWO)
    x5 = asobject(x4)
    x6 = palette(grid)
    x7 = matcher(identity, x3)
    x8 = argmin(x6, x7)
    x9 = shape(grid)
    x10 = canvas(x8, x9)
    x11 = lbind(shift, x5)
    x12 = occurrences(grid, x5)
    x13 = mapply(x11, x12)
    x14 = paint(x10, x13)
    return x14


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
