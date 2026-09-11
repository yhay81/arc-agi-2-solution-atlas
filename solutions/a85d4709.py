def _encode_marker_column(grid):
    if len(grid[0]) != 3 or any(sum(v == 5 for v in row) != 1 for row in grid):
        return [row[:] for row in grid]
    colors = {0: 2, 1: 4, 2: 3}
    return [[colors[row.index(5)]] * 3 for row in grid]


def solve(grid):
    return _encode_marker_column(grid)
