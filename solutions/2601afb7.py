def solve(grid):
    a = grid
    a = [row[:] for row in a]
    h, w = len(a), len(a[0])
    bars = []
    for c in range(w):
        rows = [r for r in range(h) if a[r][c] != 7]
        if not len(rows):
            continue
        colors = {a[r][c] for r in rows}
        if len(colors) != 1 or rows != list(range(h - len(rows), h)):
            raise ValueError("Expected bottom-aligned single-color bars")
        bars.append((c, a[rows[0]][c], len(rows)))
    out = [[7] * w for _ in range(h)]
    for index, (c, _, _) in enumerate(bars):
        color = bars[(index - 1) % len(bars)][1]
        height = bars[(index + 1) % len(bars)][2]
        for r in range(h - height, h):
            out[r][c] = color
    return out
