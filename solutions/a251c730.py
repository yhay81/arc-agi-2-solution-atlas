from collections import Counter


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def components(g, background=0, diagonal=False, mono=True):
    unseen = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != background}
    out = []
    while unseen:
        p = min(unseen)
        unseen.remove(p)
        q = [p]
        cells = []
        for r, c in q:
            cells.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if not (dr or dc) or (not diagonal and dr and dc):
                        continue
                    n = (r + dr, c + dc)
                    if n in unseen and (not mono or g[n[0]][n[1]] == g[r][c]):
                        unseen.remove(n)
                        q.append(n)
        out.append(cells)
    return out


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    right = [[1] * w for _ in range(h)]
    down = [[1] * w for _ in range(h)]
    for r in range(h - 1, -1, -1):
        for c in range(w - 1, -1, -1):
            if c + 1 < w and g[r][c + 1] == g[r][c]:
                right[r][c] += right[r][c + 1]
            if r + 1 < h and g[r + 1][c] == g[r][c]:
                down[r][c] += down[r + 1][c]
    frames = []
    for a in range(h - 4):
        for b in range(a + 4, h):
            for c in range(w - 4):
                color = g[a][c]
                frame_height = b - a + 1
                if down[a][c] < frame_height:
                    continue
                for d in range(c + 4, min(w, c + right[a][c])):
                    frame_width = d - c + 1
                    if right[b][c] < frame_width or down[a][d] < frame_height:
                        continue
                    interior = [row[c + 1 : d] for row in g[a + 1 : b]]
                    background = bg(interior)
                    if background == color:
                        continue
                    frames.append((a, b, c, d, background))
    frames = [
        f
        for f in frames
        if not any(
            f != q and q[0] <= f[0] and (q[1] >= f[1]) and (q[2] <= f[2]) and (q[3] >= f[3])
            for q in frames
        )
    ]
    if len(frames) != 2:
        raise ValueError(("Need two frames", frames))
    info = []
    for a, b, c, d, background in frames:
        tile = [row[c : d + 1] for row in g[a : b + 1]]
        interior = [row[1:-1] for row in tile[1:-1]]
        objs = components(interior, background, False, False)
        info.append((max(map(len, objs)), tile, interior, objs))
    info.sort(key=lambda x: x[0])
    _, out, target, markers = info[0]
    _, _, source, objects = info[1]
    templates = []
    for obj in objects:
        shape = {(r, c): source[r][c] for r, c in obj}
        if shape not in templates:
            templates.append(shape)
    for marker in markers:
        if len(marker) != 1:
            raise ValueError("Target has non-single marker")
        r, c = marker[0]
        color = target[r][c]
        options = []
        for template in templates:
            anchors = [p for p, v in template.items() if v == color]
            if len(anchors) != 1:
                continue
            ar, ac = anchors[0]
            shape = tuple(sorted(((rr - ar, cc - ac, v) for (rr, cc), v in template.items())))
            if shape not in options:
                options.append(shape)
        if len(options) != 1:
            raise ValueError("Template not unique")
        for dr, dc, v in options[0]:
            put(out, r + 1 + dr, c + 1 + dc, v)
    return out
