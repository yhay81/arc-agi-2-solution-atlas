def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    out = [[a[r % h][c % w] for c in range(3 * w)] for r in range(3 * h)]
    nonzero = [[value != 0 for value in row] for row in out]
    for r in range(3 * h):
        for c in range(3 * w):
            if out[r][c] == 0 and nonzero[(r + 1) % (3 * h)][(c + 1) % (3 * w)]:
                out[r][c] = 2
    return out
