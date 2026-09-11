def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    out = [[0] * (w * w) for _ in range(h * h)]
    for r in range(h):
        for c in range(w):
            color = a[r][c]
            for ir in range(h):
                for ic in range(w):
                    if a[ir][ic] == color:
                        out[r * h + ir][c * w + ic] = color
    return out
