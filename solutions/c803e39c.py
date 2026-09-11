def solve(grid):
    g = grid
    g = [row[:] for row in g]
    n = len(g) - 2
    blocks = [[row[k * (n + 3) + 1 : k * (n + 3) + 1 + n] for row in g[1:-1]] for k in range(4)]
    seed, macro, one, zero = blocks
    color1 = one[0][0]
    color0 = zero[0][0]
    return [
        [color1 if macro[r // n][c // n] and seed[r % n][c % n] else color0 for c in range(n * n)]
        for r in range(n * n)
    ]
