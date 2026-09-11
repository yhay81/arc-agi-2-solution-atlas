def solve(grid):
    a = grid
    h, w = len(a) // 4, len(a[0])
    out = [[0] * w for _ in range(h)]
    for color in (2, 8, 4, 5):
        for block in range(4):
            for r in range(h):
                for c in range(w):
                    if a[block * h + r][c] == color:
                        out[r][c] = color
    return out
