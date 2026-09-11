from collections import Counter


def mode(values):
    return Counter(v for row in values for v in row).most_common(1)[0][0]


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    bg = mode(a)
    candidates = []
    for axis in (0, 1):
        ar = a if axis == 0 else [list(col) for col in zip(*a)]
        for r, row in enumerate(ar):
            ps = [i for i, value in enumerate(row) if value != bg]
            if (
                len(ps) >= 3
                and len({row[i] for i in ps}) == 1
                and (len(set(b - a for a, b in zip(ps, ps[1:]))) == 1)
                and (ps[1] - ps[0] >= 2)
            ):
                candidates.append((axis, r, int(row[ps[0]]), tuple(ps)))
    pairs = [
        (p, q)
        for p in candidates
        for q in candidates
        if p[0] == q[0] and p[1] < q[1] and (p[2] != q[2]) and (p[3] == q[3])
    ]
    if not (len(pairs) == 1):
        raise ValueError("task assumptions are not satisfied")
    p, q = pairs[0]
    axis = p[0]
    source = max((p[2], q[2]), key=lambda c: sum(v == c for row in a for v in row))
    dest = next(c for c in (p[2], q[2]) if c != source)
    ar = a if axis == 0 else [list(col) for col in zip(*a)]
    out = [row[:] for row in ar]
    for r, row in enumerate(ar):
        for c, value in enumerate(row):
            if value != source:
                continue
            yy = p[1] + q[1] - r
            if 0 <= yy < len(ar):
                out[yy][c] = dest
    return out if axis == 0 else [list(col) for col in zip(*out)]
