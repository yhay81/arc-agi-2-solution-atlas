def solve(grid):
    height, width = len(grid), len(grid[0])
    filler = grid[-1][-1]
    rows = [r for r, row in enumerate(grid) if any(value != filler for value in row)]
    cols = [c for c in range(width) if any(grid[r][c] != filler for r in range(height))]
    if not rows or not cols or rows[0] or cols[0]:
        return [row[:] for row in grid]
    ph, pw = rows[-1] + 1, cols[-1] + 1
    if any(grid[r][c] == filler for r in range(ph) for c in range(pw)):
        return [row[:] for row in grid]
    if any(grid[r][c] != filler for r in range(ph, height) for c in range(width)):
        return [row[:] for row in grid]
    if any(grid[r][c] != filler for r in range(height) for c in range(pw, width)):
        return [row[:] for row in grid]
    rp = next((p for p in range(1, ph + 1) if all(grid[r] == grid[r % p] for r in range(ph))), None)
    cp = next(
        (
            p
            for p in range(1, pw + 1)
            if all(grid[r][c] == grid[r][c % p] for r in range(ph) for c in range(pw))
        ),
        None,
    )
    if rp in (None, ph) or cp in (None, pw):
        return [row[:] for row in grid]
    tile = [row[:cp] for row in grid[:rp]]
    return [[tile[r % rp][(c + 1) % cp] for c in range(width)] for r in range(height)]
