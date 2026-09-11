from collections import Counter


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


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    objects = components(g, 0, False, True)
    holes = set()
    pieces = []
    out = [[0] * w for _ in g]
    for obj in objects:
        color = g[obj[0][0]][obj[0][1]]
        if color == 5:
            continue
        a, b, c, d = bbox(obj)
        area = (b - a + 1) * (d - c + 1)
        if len(obj) < area:
            for r, col in obj:
                out[r][col] = color
            holes |= {
                (r, col) for r in range(a, b + 1) for col in range(c, d + 1) if g[r][col] == 0
            }
        else:
            pieces.append((color, b - a + 1, d - c + 1))
    inventory = Counter(pieces)
    placements = []
    bycell = {p: [] for p in holes}
    for (color, ph, pw), count in inventory.items():
        for r, c in holes:
            cells = frozenset((rr, cc) for rr in range(r, r + ph) for cc in range(c, c + pw))
            if cells <= holes:
                index = len(placements)
                placements.append(((color, ph, pw), cells))
                for p in cells:
                    bycell[p].append(index)
    answers = set()
    visited = set()

    def search(left, stock, paint):
        if len(answers) > 1:
            return
        if not left:
            answers.add(tuple(sorted(paint)))
            return
        state = (frozenset(left), tuple(sorted(stock.items())), tuple(sorted(paint)))
        if state in visited:
            return
        visited.add(state)

        def options(p):
            return [i for i in bycell[p] if stock[placements[i][0]] and placements[i][1] <= left]

        p = min(left, key=lambda p: len(options(p)))
        for i in options(p):
            spec, cells = placements[i]
            stock[spec] -= 1
            search(left - cells, stock, paint + [(r, c, spec[0]) for r, c in cells])
            stock[spec] += 1

    search(holes, inventory, [])
    if len(answers) != 1:
        raise ValueError(("Packing not unique", len(answers)))
    for r, c, color in next(iter(answers)):
        out[r][c] = color
    return out
