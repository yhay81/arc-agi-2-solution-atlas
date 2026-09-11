def rotate(g, k):
    for _ in range(k % 4):
        g = [list(r) for r in zip(*g[::-1])]
    return g


def bbox(ps):
    return (
        min((r for r, c in ps)),
        min((c for r, c in ps)),
        max((r for r, c in ps)),
        max((c for r, c in ps)),
    )


def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = copy(g)
    marks = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 4]
    top, left, bottom, right = bbox(marks)
    patch = [row[left : right + 1] for row in g[top : bottom + 1]]
    variants = []
    seen = set()
    for flip in (False, True):
        for k in range(4):
            variant = rotate([row[::-1] for row in patch] if flip else patch, k)
            key = tuple(map(tuple, variant))
            if key not in seen:
                seen.add(key)
                variants.append(variant)
    sixes = {(r, c) for r, row in enumerate(g) for c, value in enumerate(row) if value == 6}
    for p in variants:
        h, w = (len(p), len(p[0]))
        shape = {(r, c) for r, row in enumerate(p) for c, v in enumerate(row) if v == 6}
        offsets = {(row - r, col - c) for row, col in sixes for r, c in shape}
        for a, b in offsets:
            visible = {
                (a + r, b + c) for r, c in shape if 0 <= a + r < len(g) and 0 <= b + c < len(g[0])
            }
            actual = {(r, c) for r, c in sixes if a <= r < a + h and b <= c < b + w}
            if actual == visible and len(visible) >= 3:
                for r in range(h):
                    for c in range(w):
                        if p[r][c] == 4 and 0 <= a + r < len(g) and 0 <= b + c < len(g[0]):
                            out[a + r][b + c] = 4
    return out
