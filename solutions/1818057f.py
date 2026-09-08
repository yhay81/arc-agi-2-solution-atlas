"""Concepts: compositional grid transformation, typed operations

Transformation:
- Scan the grid for 4-coloured plus motifs and recolour each detected plus (centre and arms) to 8.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used for acceptance verification.

Source:
- arc-abstractions, distributed under the MIT License.
"""

# ruff: noqa

from __future__ import annotations

from typing import Callable, List, Sequence, Tuple, TypeVar

Grid = List[List[int]]
T = TypeVar("T")


def fold_repaint(canvas: Grid, items: Sequence[T], update: Callable[[Grid, T], Grid]) -> Grid:
    acc = canvas
    for x in items:
        acc = update(acc, x)
    return acc


def isPlus(g: Grid, position: Tuple[int, int]) -> bool:
    r, c = position
    h = len(g)
    w = len(g[0]) if h else 0
    if not (0 < r < h - 1 and 0 < c < w - 1):
        return False
    if g[r][c] != 4:
        return False
    return g[r - 1][c] == 4 and g[r + 1][c] == 4 and g[r][c - 1] == 4 and g[r][c + 1] == 4


def repaintPlus(canvas: Grid, position: Tuple[int, int]) -> Grid:
    r, c = position
    # Copy-on-write to keep purity.
    out = [row[:] for row in canvas]
    out[r][c] = 8
    out[r - 1][c] = 8
    out[r + 1][c] = 8
    out[r][c - 1] = 8
    out[r][c + 1] = 8
    return out


def solve_1818057f(grid: Grid) -> Grid:
    candidates = [(r, c) for r in range(1, len(grid) - 1) for c in range(1, len(grid[0]) - 1)]

    def repaint(canvas: Grid, position: Tuple[int, int]) -> Grid:
        if isPlus(grid, position):
            return repaintPlus(canvas, position)
        return canvas

    return fold_repaint(grid, candidates, repaint)


p = solve_1818057f

TASK_ID = "1818057f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("compositional-operations", "arc-abstractions")

solve = solve_1818057f
