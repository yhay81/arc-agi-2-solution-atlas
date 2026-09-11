from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


def solve(grid):
    a = grid
    a = [list(row) for row in a]
    flat = [v for row in a for v in row]
    base = mode(flat)
    edge = next(c for c in set(flat) if c != base)
    flipr = all(v == edge for v in a[0])
    flipc = all(row[0] == edge for row in a)
    b = a[::-1] if flipr else [row[:] for row in a]
    b = [row[::-1] for row in b] if flipc else b
    h, w = len(b), len(b[0])
    out = [[8] * w for _ in range(h)]
    out[-1] = [base] * w
    for row in out:
        row[-1] = base
    out[-2][:-1] = [edge] * (w - 1)
    for row in out[:-1]:
        row[-2] = edge
    for k in range(min(h, w)):
        out[h - 1 - k][w - 1 - k] = 8 if k < 2 else base
    if flipc:
        out = [row[::-1] for row in out]
    if flipr:
        out = out[::-1]
    return out
