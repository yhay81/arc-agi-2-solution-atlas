"""Expand each cell by the number of distinct input colors."""

from arc_agi_2_atlas.types import Grid


def solve(grid: Grid) -> Grid:
    """Replace each cell with a k by k block, where k is the color count."""
    factor = len({cell for row in grid for cell in row})
    return [[cell for cell in row for _ in range(factor)] for row in grid for _ in range(factor)]
