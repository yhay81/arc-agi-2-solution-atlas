from collections import Counter


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    lines = [
        (r, Counter(row).most_common(1)[0][0])
        for r, row in enumerate(a)
        if Counter(row).most_common(1)[0][0] != 7
    ]
    out = []
    for r, row in enumerate(a):
        ds = [(abs(r - rr), v) for rr, v in lines]
        md = min((d for d, v in ds))
        vs = {v for d, v in ds if d == md}
        color = 1 if md == 0 or len(vs) > 1 else next(iter(vs))
        out.append([8 if v == 1 else 1 if v == 8 else color for v in row])
    return out
