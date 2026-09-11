def solve(grid):
    g = grid
    g = [row[:] for row in g]
    n = len(g)
    flip = sum(g[r][r] != 0 for r in range(n)) < sum(g[r][n - 1 - r] != 0 for r in range(n))
    if flip:
        transformed = solve([row[::-1] for row in g])
        return [row[::-1] for row in transformed]
    for p in range(1, n):
        if all(g[r][c] == g[r + p][c + p] for r in range(n - p) for c in range(n - p)):
            break
    out = [[0] * (2 * n) for _ in range(2 * n)]
    for r in range(2 * n):
        for c in range(2 * n):
            rr, cc = (r, c)
            while rr >= n or cc >= n:
                rr -= p
                cc -= p
            if rr >= 0 and cc >= 0:
                out[r][c] = g[rr][cc]
    return out
