def solve(grid):
    g = grid
    out = [row[:] for row in g]
    for r in range(1, len(g)):
        for c in range(1, len(g[0]) - 1):
            if out[r - 1][c - 1] != 7 and out[r - 1][c + 1] != 7:
                out[r][c] = 5 if out[r - 1][c - 1] == 2 else 2
    return out
