def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = None
    for r in range(0, len(a), 2):
        for c in range(0, len(a[0]), 2):
            block = [row[c : c + 2] for row in a[r : r + 2]]
            if out is None:
                out = [row[:] for row in block]
                continue
            n = len(out) + 2
            new = [[0] * n for _ in range(n)]
            for y in range(n):
                for x in range(n):
                    new[y][x] = block[int(y >= n // 2)][int(x >= n // 2)]
            for y in range(1, n - 1):
                new[y][1:-1] = out[y - 1][:]
            out = new
    return out
