def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    v = [c for c in range(w) if all(row[c] == 0 for row in g)]
    rows = [r for r, row in enumerate(g) if all(x == 0 for x in row)]
    if len(v) != 2:
        if len(rows) != 2:
            raise ValueError("cannot identify two parallel lines")
        t = solve([list(row) for row in zip(*g)])
        return [list(row) for row in zip(*t)]
    center = sum(v) // 2
    cross = max(range(h), key=lambda r: sum(x == 0 for x in g[r]))
    n = sum(x == 5 for row in g for x in row)
    out = [[7] * w for _ in g]
    for r in range(h):
        out[r][center - 1] = out[r][center + 1] = 0
    out[cross] = [0] * w
    for r in range(cross - n // 2, cross + (n + 1) // 2):
        if 0 <= r < h:
            out[r][center] = 5
    return out
