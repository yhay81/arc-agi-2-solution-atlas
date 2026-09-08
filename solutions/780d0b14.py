"""Executable re-arc DSL program for ARC-AGI-2 task 780d0b14.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_ONE,
    F,
    T,
    apply,
    astuple,
    canvas,
    color,
    compose,
    compress,
    fill,
    fork,
    frontiers,
    hconcat,
    merge,
    objects,
    other,
    paint,
    palette,
    rbind,
    shape,
    ulcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "780d0b14"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = merge(x0)
    x2 = color(x1)
    x3 = merge(x0)
    x4 = fill(grid, NEG_ONE, x3)
    x5 = shape(grid)
    x6 = canvas(NEG_ONE, x5)
    x7 = hconcat(x4, x6)
    x8 = objects(x7, F, F, T)
    x9 = rbind(other, x2)
    x10 = compose(x9, palette)
    x11 = fork(astuple, x10, ulcorner)
    x12 = apply(x11, x8)
    x13 = merge(x8)
    x14 = fill(grid, x2, x13)
    x15 = paint(x14, x12)
    x16 = compress(x15)
    return x16


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
