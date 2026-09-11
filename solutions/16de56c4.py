from collections import Counter


def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = cp(g)
    h, w = (len(g), len(g[0]))
    specs = []
    for vertical in [False, True]:
        for line in range(w if vertical else h):
            vals = [g[p][line] if vertical else g[line][p] for p in range(h if vertical else w)]
            counts = Counter(vals)
            for color, num in counts.items():
                if color == 0 or num < 2:
                    continue
                ps = [p for p, v in enumerate(vals) if v == color]
                diffs = [b - a for a, b in zip(ps, ps[1:])]
                if len(set(diffs)) != 1:
                    continue
                step = diffs[0]
                stops = [
                    p for p, v in enumerate(vals) if v not in (0, color) and (p - ps[0]) % step == 0
                ]
                lo, hi = (0, len(vals) - 1)
                newcolor = color
                if stops:
                    left = [p for p in stops if p < min(ps)]
                    right = [p for p in stops if p > max(ps)]
                    if left:
                        lo = max(left)
                        newcolor = vals[lo]
                    if right:
                        hi = min(right)
                        newcolor = vals[hi]
                specs.append(
                    (
                        vertical,
                        line,
                        [(p, newcolor) for p in range(lo, hi + 1) if (p - ps[0]) % step == 0],
                    )
                )
    orientation = Counter((v for v, l, c in specs)).most_common(1)[0][0]
    for vertical, line, cells in specs:
        if vertical != orientation:
            continue
        for p, color in cells:
            if vertical:
                out[p][line] = color
            else:
                out[line][p] = color
    return out
