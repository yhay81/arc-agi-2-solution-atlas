from collections import Counter


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


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    background = bg(g)
    h, w = (len(g), len(g[0]))
    targets = []
    for color in set(sum(g, [])) - {background}:
        a, b, c, d = bbox(points(g, color))
        if ((a == 0 and b == h - 1) or (c == 0 and d == w - 1)) and all(
            g[r][col] in (background, color) for r in range(a, b + 1) for col in range(c, d + 1)
        ):
            targets.append((color, a, b, c, d))
    if len(targets) != 1:
        raise ValueError("Ambiguous binary target")
    color, a, b, c, d = targets[0]
    target = [row[c : d + 1] for row in g[a : b + 1]]
    inventory = [
        [background if a <= r <= b and c <= col <= d else v for col, v in enumerate(row)]
        for r, row in enumerate(g)
    ]
    objects = components(inventory, background, True, False)
    pieces = []
    for obj in objects:
        aa, bb, cc, dd = bbox(obj)
        pieces.append([(r - aa, col - cc, g[r][col]) for r, col in obj])
    holes = [
        (r, col) for r, row in enumerate(target) for col, v in enumerate(row) if v == background
    ]
    index = {p: i for i, p in enumerate(holes)}
    n = len(holes)
    if sum(map(len, pieces)) != n:
        raise ValueError(f"Piece area {sum(map(len, pieces))} vs target {n}")
    options = []
    cover = [[] for _ in holes]
    for i, piece in enumerate(pieces):
        ph = max((r for r, c, v in piece)) + 1
        pw = max((c for r, c, v in piece)) + 1
        for r in range(len(target) - ph + 1):
            for col in range(len(target[0]) - pw + 1):
                cells = [(r + dr, col + dc, v) for dr, dc, v in piece]
                if not all(((rr, cc) in index for rr, cc, v in cells)):
                    continue
                mask = sum((1 << index[rr, cc] for rr, cc, v in cells))
                k = len(options)
                options.append((i, mask, cells))
                for rr, cc, v in cells:
                    cover[index[rr, cc]].append(k)
    answers = []
    seen = set()

    def search(filled, used, selected):
        if len(answers) > 1:
            return
        if filled == (1 << n) - 1:
            out = cp(target)
            for k in selected:
                for r, c, v in options[k][2]:
                    out[r][c] = v
            key = tuple(map(tuple, out))
            if key not in seen:
                seen.add(key)
                answers.append(out)
            return
        candidates = None
        for p in range(n):
            if filled >> p & 1:
                continue
            avail = [
                k
                for k in cover[p]
                if not used >> options[k][0] & 1 and (not options[k][1] & filled)
            ]
            if not avail:
                return
            if candidates is None or len(avail) < len(candidates):
                candidates = avail
            if len(candidates) == 1:
                break
        equivalent = set()
        for k in candidates:
            i, mask, cells = options[k]
            sig = (mask, tuple(cells))
            if sig in equivalent:
                continue
            equivalent.add(sig)
            search(filled | mask, used | 1 << i, selected + [k])

    search(0, 0, [])
    if len(answers) != 1:
        raise ValueError(f"Packing solutions {len(answers)}")
    return answers[0]
