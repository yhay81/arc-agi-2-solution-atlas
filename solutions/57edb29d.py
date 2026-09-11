from collections import Counter


def mode(values):
    return Counter(v for row in values for v in row).most_common(1)[0][0]


def bounds(points):
    return (
        min(r for r, c in points),
        min(c for r, c in points),
        max(r for r, c in points),
        max(c for r, c in points),
    )


def components(mask, diagonal=False):
    unseen = {(r, c) for r, row in enumerate(mask) for c, v in enumerate(row) if v}
    groups = []
    while unseen:
        p = unseen.pop()
        q = [p]
        group = [p]
        for r, c in q:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                z = (r + dr, c + dc)
                if z in unseen:
                    unseen.remove(z)
                    q.append(z)
                    group.append(z)
        groups.append(group)
    return groups


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    panels = []
    for ps in components([[v != 4 for v in row] for row in a]):
        r, c, b, d = bounds(ps)
        p = [row[c : d + 1] for row in a[r : b + 1]]
        panels.append((p, mode(p)))
    blank = [(p, bg) for p, bg in panels if all(v == bg for row in p for v in row)]
    if not (len(blank) == 1):
        raise ValueError("task assumptions are not satisfied")
    target, bg = blank[0]
    source, sbg = max(
        [(p, b) for p, b in panels if any(v != b for row in p for v in row)],
        key=lambda x: (len(x[0]), len(x[0][0])),
    )
    out = [[bg] * len(target[0]) for _ in target]

    def coord(v, n, m):
        return v if v < 3 else m - (n - v) if v >= n - 3 else m // 2

    for r in range(len(out)):
        for c in range(len(out[0])):
            color = source[coord(r, len(out), len(source))][coord(c, len(out[0]), len(source[0]))]
            if color != sbg:
                out[r][c] = color
    return out
