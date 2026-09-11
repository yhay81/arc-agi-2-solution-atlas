from collections import Counter


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    bg = Counter(v for row in a for v in row).most_common(1)[0][0]
    colors = {v for row in a for v in row if v != bg}
    pts = {
        v: [(r, c) for r, row in enumerate(a) for c, x in enumerate(row) if x == v] for v in colors
    }
    boxes = {
        v: (
            min((r for r, c in p)),
            max((r for r, c in p)),
            min((c for r, c in p)),
            max((c for r, c in p)),
        )
        for v, p in pts.items()
    }
    n = max((max(r1 - r0 + 1, c1 - c0 + 1) for r0, r1, c0, c1 in boxes.values()))
    mask = set()
    for v, (r0, r1, c0, c1) in boxes.items():
        if r1 - r0 + 1 != n or c1 - c0 + 1 != n:
            continue
        for r, c in pts[v]:
            x, y = (r - r0, c - c0)
            mask.update(
                [
                    (x, y),
                    (n - 1 - x, y),
                    (x, n - 1 - y),
                    (n - 1 - x, n - 1 - y),
                    (y, x),
                    (n - 1 - y, x),
                    (y, n - 1 - x),
                    (n - 1 - y, n - 1 - x),
                ]
            )
    if not (mask):
        raise ValueError("task assumptions are not satisfied")
    out = [row[:] for row in a]
    for v, (r0, r1, c0, c1) in boxes.items():
        options = []
        for ar in range(max(0, r1 - n + 1), r0 + 1):
            for ac in range(max(0, c1 - n + 1), c0 + 1):
                if (
                    ar + n <= len(a)
                    and ac + n <= len(a[0])
                    and all(((r - ar, c - ac) in mask for r, c in pts[v]))
                ):
                    options.append((ar, ac))
        if not (len(options) == 1):
            raise ValueError((v, options))
        ar, ac = options[0]
        for r, c in mask:
            out[ar + r][ac + c] = v
    return out
