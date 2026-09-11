def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0
    if not h or not w:
        return a
    marker = 2
    axis = barrier = None
    direction = 0
    for c in range(w):
        if all(a[r][c] == marker for r in range(h)):
            axis, barrier, direction = 1, c, 1 if c >= w // 2 else -1
            break
    if axis is None:
        for r in range(h):
            if all(a[r][c] == marker for c in range(w)):
                axis, barrier, direction = 0, r, 1 if r >= h // 2 else -1
                break
    if axis is None:
        return a
    seen, parts = set(), []
    for r in range(h):
        for c in range(w):
            if a[r][c] in (0, marker) or (r, c) in seen:
                continue
            color = a[r][c]
            stack, comp = [(r, c)], []
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                comp.append((y, x))
                for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                    if 0 <= ny < h and 0 <= nx < w and a[ny][nx] == color and (ny, nx) not in seen:
                        seen.add((ny, nx))
                        stack.append((ny, nx))
            parts.append(comp)
    key = lambda p: min(x for _, x in p) if axis == 1 else min(y for y, _ in p)
    parts.sort(key=key, reverse=direction > 0)
    out = [[0] * w for _ in range(h)]
    for comp in parts:
        shift = 0
        while True:
            candidate = shift + direction
            valid = True
            for y, x in comp:
                ty, tx = (y + candidate, x) if axis == 0 else (y, x + candidate)
                pos = ty if axis == 0 else tx
                if (
                    not (0 <= ty < h and 0 <= tx < w)
                    or out[ty][tx]
                    or (pos <= barrier if direction < 0 else pos >= barrier)
                ):
                    valid = False
                    break
            if not valid:
                break
            shift = candidate
        for y, x in comp:
            ty, tx = (y + shift, x) if axis == 0 else (y, x + shift)
            out[ty][tx] = a[y][x]
    if axis == 0:
        out[barrier] = [marker] * w
    else:
        for r in range(h):
            out[r][barrier] = marker
    return out
