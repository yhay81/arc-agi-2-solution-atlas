def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    o = [[0] * (2 * w) for _ in range(2 * h)]
    for r, row in enumerate(g):
        o[r][:w] = row
        o[r + h][w:] = row
    occupied = [r for r, row in enumerate(o) if any(row)]
    for a, b in zip(occupied, occupied[1:]):
        if b - a == 2 and any(o[a][c] and o[b][c] for c in range(2 * w)):
            o[a + 1] = [3] * (2 * w)
    return o
