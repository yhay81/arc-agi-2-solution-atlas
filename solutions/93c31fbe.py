def bbox(ps):
    return (
        min((r for r, c in ps)),
        min((c for r, c in ps)),
        max((r for r, c in ps)),
        max((c for r, c in ps)),
    )


def components(g, background=None, by_color=True, diagonal=False):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if diagonal:
        offsets += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    h, w = (len(g), len(g[0]))
    unseen = {(r, c) for r in range(h) for c in range(w) if g[r][c] != background}
    result = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = [start]
        cells = []
        color = g[start[0]][start[1]]
        while queue:
            r, c = queue.pop()
            cells.append((r, c))
            for dr, dc in offsets:
                p = (r + dr, c + dc)
                if p in unseen and (not by_color or g[p[0]][p[1]] == color):
                    unseen.remove(p)
                    queue.append(p)
        result.append((color, cells))
    return result


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    corners = []
    for col, ps in components(g, 0):
        if col in (0, 1) or len(ps) != 3:
            continue
        top, left, bottom, right = bbox(ps)
        if bottom - top == right - left == 1:
            missing = next(
                (r, c)
                for r in range(top, bottom + 1)
                for c in range(left, right + 1)
                if (r, c) not in ps
            )
            corners.append((top, left, missing[0] - top, missing[1] - left))
    frames = []
    for top, left, dr, dc in corners:
        if (dr, dc) != (1, 1):
            continue
        for t, right, rr, rc in corners:
            if t != top or (rr, rc) != (1, 0):
                continue
            for bottom, l, br, bc in corners:
                if l == left and (br, bc) == (0, 1) and ((bottom, right, 0, 0) in corners):
                    frames.append((top, left, bottom + 1, right + 1))
    out = [[0 if v == 1 else v for v in row] for row in g]
    for top, left, bottom, right in frames:
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                if g[r][c] == 1:
                    out[r][c] = 1
                    a, b = (
                        (r, left + right - c)
                        if right - left > bottom - top
                        else (top + bottom - r, c)
                    )
                    out[a][b] = 1
    return out
