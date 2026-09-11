def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    border = g[0][0]
    rails = [
        c
        for c in range(1, w - 1)
        if len({g[r][c] for r in range(1, h - 1)}) == 1 and g[1][c] not in (0, border)
    ]
    if len(rails) != 2:
        transposed = [list(row) for row in zip(*g)]
        result = solve(transposed)
        return [list(row) for row in zip(*result)]
    left, right = rails
    out = [[0] * w for _ in g]
    rail = g[1][left]
    seq = [tuple(row[left + 1 : right]) for row in g[1:-1]]
    period = next(
        p for p in range(1, len(seq) + 1) if all(seq[j] == seq[j % p] for j in range(len(seq)))
    )
    for r in range(h):
        out[r][left] = out[r][right] = rail
        interior = seq[(r - 1) % period]
        for c, value in enumerate(interior, left + 1):
            out[r][c] = value
        if any(interior):
            for c in list(range(left)) + list(range(right + 1, w)):
                out[r][c] = border
    return out
