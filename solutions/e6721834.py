def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0
    if not h or not w:
        return a

    def mode(panel):
        vals = {v for row in panel for v in row}
        return min(vals, key=lambda v: (-sum(x == v for row in panel for x in row), v))

    splits = []
    for axis in (0, 1):
        size = h if axis == 0 else w
        for cut in range(3, size - 2):
            first = [row[:] for row in a[:cut]] if axis == 0 else [row[:cut] for row in a]
            second = [row[:] for row in a[cut:]] if axis == 0 else [row[cut:] for row in a]
            if (
                abs(
                    (len(first) if axis == 0 else len(first[0]))
                    - (len(second) if axis == 0 else len(second[0]))
                )
                > 1
            ):
                continue
            b1, b2 = mode(first), mode(second)
            if b1 == b2:
                continue
            score = sum(v == b1 for row in first for v in row) + sum(
                v == b2 for row in second for v in row
            )
            splits.append((score, first, b1, second, b2))
    if not splits:
        return a
    best_score = max(x[0] for x in splits)
    best = [x for x in splits if x[0] == best_score]
    if len(best) != 1:
        return a
    _, first, bg1, second, bg2 = best[0]
    n1 = sum(v != bg1 for row in first for v in row)
    n2 = sum(v != bg2 for row in second for v in row)
    source, sbg, dest = (first, bg1, second) if n1 > n2 else (second, bg2, first)
    fg = [v for row in source for v in row if v != sbg]
    if not fg:
        return a
    body = min(set(fg), key=lambda v: (-fg.count(v), v))
    sh, sw = len(source), len(source[0])
    dh, dw = len(dest), len(dest[0])
    seen, comps = set(), []
    for r in range(sh):
        for c in range(sw):
            if source[r][c] == sbg or (r, c) in seen:
                continue
            stack, comp = [(r, c)], []
            seen.add((r, c))
            while stack:
                y, x = stack.pop()
                comp.append((y, x))
                for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                    if (
                        0 <= ny < sh
                        and 0 <= nx < sw
                        and source[ny][nx] != sbg
                        and (ny, nx) not in seen
                    ):
                        seen.add((ny, nx))
                        stack.append((ny, nx))
            comps.append(comp)
    out = [row[:] for row in dest]
    placed = 0
    for comp in comps:
        ys, xs = zip(*comp)
        top, left, bottom, right = min(ys), min(xs), max(ys), max(xs)
        tile = [row[left : right + 1] for row in source[top : bottom + 1]]
        markers = {v for row in tile for v in row if v not in (sbg, body)}
        if len(markers) != 1:
            continue
        marker = next(iter(markers))
        rel = [
            (r, c) for r in range(len(tile)) for c in range(len(tile[0])) if tile[r][c] == marker
        ]
        targets = [(r, c) for r in range(dh) for c in range(dw) if dest[r][c] == marker]
        anchors = []
        for tr, tc in targets:
            ar, ac = tr - rel[0][0], tc - rel[0][1]
            translated = {(ar + r, ac + c) for r, c in rel}
            if (
                ar >= 0
                and ac >= 0
                and ar + len(tile) <= dh
                and ac + len(tile[0]) <= dw
                and translated <= set(targets)
            ):
                anchors.append((ar, ac))
        if len(set(anchors)) != 1:
            continue
        ar, ac = anchors[0]
        for r, row in enumerate(tile):
            for c, value in enumerate(row):
                if value != sbg:
                    out[ar + r][ac + c] = value
        placed += 1
    return out if placed else a
