from collections import Counter


def mode(values):
    return Counter(v for row in values for v in row).most_common(1)[0][0]


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    color = mode(a)
    h, w = len(a), len(a[0])
    out = [[0] * (w * w) for _ in range(h * h)]
    for r, row in enumerate(a):
        for c, v in enumerate(row):
            if v == color:
                for ir in range(h):
                    out[r * h + ir][c * w : c * w + w] = a[ir][:]
    return out
