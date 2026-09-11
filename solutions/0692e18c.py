def _kronecker_complement(grid):
    values = [v for row in grid for v in row if v]
    if not len(values):
        return [row[:] for row in grid]
    color = values[0]
    h, w = len(grid), len(grid[0])
    tile = [[color if v == 0 else 0 for v in row] for row in grid]
    return [
        [tile[ir][ic] if grid[r][c] else 0 for c in range(w) for ic in range(w)]
        for r in range(h)
        for ir in range(h)
    ]


def solve(grid):
    return _kronecker_complement(grid)
