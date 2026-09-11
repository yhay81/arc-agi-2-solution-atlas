def solve(grid):
    h, w = len(grid), len(grid[0])
    marks = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 2]
    if not marks or len({r for r, _ in marks}) != 1:
        return [row[:] for row in grid]
    row = marks[0][0]
    cols = sorted(c for _, c in marks)
    if (
        cols[0]
        or cols != list(range(cols[0], cols[-1] + 1))
        or sum(v != 0 for line in grid for v in line) != len(cols)
    ):
        return [line[:] for line in grid]
    out = [line[:] for line in grid]
    length = len(cols)
    for r in range(row):
        width = length + row - r
        if width > w:
            return [line[:] for line in grid]
        out[r][:width] = [3] * width
    for r in range(row + 1, h):
        width = length - (r - row)
        if width > 0:
            out[r][:width] = [1] * width
    return out
