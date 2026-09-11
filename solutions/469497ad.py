def solve(grid):
    h, w = len(grid), len(grid[0])
    factor = len({v for r in grid for v in r if v})
    blocks = [
        (r, c)
        for r in range(h - 1)
        for c in range(w - 1)
        if grid[r][c] and all(grid[i][j] == grid[r][c] for i in (r, r + 1) for j in (c, c + 1))
    ]
    if not factor or len(blocks) != 1:
        return [r[:] for r in grid]
    top, left = blocks[0]
    out = [[v for v in row for _ in range(factor)] for row in grid for _ in range(factor)]
    for r, c, anti in (
        (top - 1, left - 1, 0),
        (top - 1, left + 2, 1),
        (top + 2, left - 1, 1),
        (top + 2, left + 2, 0),
    ):
        if not (0 <= r < h and 0 <= c < w) or grid[r][c]:
            continue
        for i in range(factor):
            j = factor - 1 - i if anti else i
            if out[r * factor + i][c * factor + j] == 0:
                out[r * factor + i][c * factor + j] = 2
    return out
