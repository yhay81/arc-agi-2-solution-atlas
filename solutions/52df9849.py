from collections import Counter


def convex_hull(points):
    ordered = sorted(set(points))

    def cross(origin, a, b):
        return (a[0] - origin[0]) * (b[1] - origin[1]) - (a[1] - origin[1]) * (b[0] - origin[0])

    lower = []
    for point in ordered:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(ordered):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def in_hull(point, hull):
    return all(
        (b[0] - a[0]) * (point[1] - a[1]) - (b[1] - a[1]) * (point[0] - a[0]) >= 0
        for a, b in zip(hull, hull[1:] + hull[:1])
    )


def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    base = bg(g)
    colors = set(sum(g, [])) - {base}
    masks = {}
    for color in colors:
        pts = points(g, color)
        hull = convex_hull(pts)
        if len(hull) < 3:
            aa, bb, cc, dd = bbox(pts)
            mask = {
                (r, c)
                for r in range(aa, bb + 1)
                for c in range(cc, dd + 1)
                if all(
                    (r - pts[0][0]) * (q[1] - pts[0][1]) == (c - pts[0][1]) * (q[0] - pts[0][0])
                    for q in pts
                )
            }
        else:
            aa, bb, cc, dd = bbox(pts)
            full = [
                all(((r, c) in pts for r, c in edge))
                for edge in [
                    [(aa, c) for c in range(cc, dd + 1)],
                    [(bb, c) for c in range(cc, dd + 1)],
                    [(r, cc) for r in range(aa, bb + 1)],
                    [(r, dd) for r in range(aa, bb + 1)],
                ]
            ]
            if any(full[i] and full[j] for i in (0, 1) for j in (2, 3)):
                masks[color] = {(r, c) for r in range(aa, bb + 1) for c in range(cc, dd + 1)}
                continue
            mask = {
                (r, c) for r in range(len(g)) for c in range(len(g[0])) if in_hull((r, c), hull)
            }
        masks[color] = mask
    before = {
        color: {g[r][c] for r, c in mask if g[r][c] not in (base, color)}
        for color, mask in masks.items()
    }
    out = cp(g)
    remaining = set(colors)
    while remaining:
        ready = [color for color in remaining if not before[color] & remaining]
        if not ready:
            raise ValueError("Occlusion cycle")
        for color in ready:
            for r, c in masks[color]:
                out[r][c] = color
            remaining.remove(color)
    return out
