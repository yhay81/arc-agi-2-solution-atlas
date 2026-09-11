def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0
    if not h or not w:
        return a
    seen, parts = set(), []
    for r in range(h):
        for c in range(w):
            if a[r][c] != 1 or (r, c) in seen:
                continue
            stack, comp = [(r, c)], []
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                comp.append((y, x))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = y + dy, x + dx
                        if (
                            (dy or dx)
                            and 0 <= ny < h
                            and 0 <= nx < w
                            and a[ny][nx] == 1
                            and (ny, nx) not in seen
                        ):
                            seen.add((ny, nx))
                            stack.append((ny, nx))
            parts.append(comp)
    if not parts:
        return a
    comp = max(parts, key=len)
    top, left = min(y for y, _ in comp), min(x for _, x in comp)
    bottom, right = max(y for y, _ in comp), max(x for _, x in comp)
    template = [
        [(y, x) in {(r, c) for r, c in comp} for x in range(left, right + 1)]
        for y in range(top, bottom + 1)
    ]
    out = [row[:] for row in a]
    variants = []
    for _ in range(4):
        for v in (template, [row[::-1] for row in template]):
            if v not in variants:
                variants.append(v)
        template = [list(row) for row in zip(*template[::-1])]
    for v in variants:
        vh, vw = len(v), len(v[0])
        holes = [(y, x) for y in range(vh) for x in range(vw) if not v[y][x]]
        for ar in range(-(vh - 1), h):
            for ac in range(-(vw - 1), w):
                targets = [(ar + y, ac + x) for y, x in holes]
                if (
                    len(targets) != sum(0 <= y < h and 0 <= x < w for y, x in targets)
                    or not targets
                    or any(a[y][x] != 4 for y, x in targets)
                ):
                    continue
                for y in range(vh):
                    for x in range(vw):
                        ty, tx = ar + y, ac + x
                        if v[y][x] and 0 <= ty < h and 0 <= tx < w and out[ty][tx] == 0:
                            out[ty][tx] = 1
    return out
