from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    w = len(a[0])
    mid = mode(value for row in a for value in row)
    for r, row in enumerate(a):
        ix = [i for i, value in enumerate(row) if value == mid]
        if not len(ix):
            continue
        s, e = (ix[0], ix[-1] + 1)
        n = e - s
        dest = min(s, max(0, w // 2 + 1 - n))
        out[r] = list(row[:dest]) + [mid] * n + list(row[dest:s]) + list(row[e:])
    return out
