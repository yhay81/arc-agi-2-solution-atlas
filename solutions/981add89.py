from collections import Counter


def solve(grid):
    a = grid
    bg = Counter(v for row in a for v in row).most_common(1)[0][0]
    out = [row[:] for row in a]
    for c, v in enumerate(a[0]):
        if v != bg:
            for r in range(1, len(a)):
                out[r][c] = bg if a[r][c] == v else v
    return out
