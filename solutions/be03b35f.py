from itertools import pairwise


def _split_panels(array, color):
    separator_rows = [row for row in range(len(array)) if all(v == color for v in array[row])]
    separator_cols = [
        col
        for col in range(len(array[0]))
        if all(array[r][col] == color for r in range(len(array)))
    ]

    def intervals(size: int, separators: list[int]) -> list[tuple[int, int]]:
        edges = [-1, *separators, size]
        return [(left + 1, right) for left, right in pairwise(edges) if right > left + 1]

    row_intervals = intervals(len(array), separator_rows)
    col_intervals = intervals(len(array[0]), separator_cols)
    if len(row_intervals) * len(col_intervals) < 2:
        return []
    return [
        [row[left:right] for row in array[top:bottom]]
        for top, bottom in row_intervals
        for left, right in col_intervals
    ]


def solve(grid):
    panels = _split_panels(grid, 0)
    index = 0
    output = panels[index] if index < len(panels) else [row[:] for row in grid]
    return [list(row) for row in zip(*output)][::-1]
