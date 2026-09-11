def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def solve(grid):
    g = grid
    g = cp(g)
    cells = set(points(g, 8))
    shapes = {
        1: ((0, 0), (0, 1), (1, 0), (1, 1)),
        2: ((0, 1), (1, 0), (1, 1)),
        3: ((0, 0), (0, 1), (1, 1)),
        4: ((0, 0), (1, 0), (1, 1)),
    }
    options = []
    bycell = {p: [] for p in cells}
    for r in range(len(g) - 1):
        for c in range(len(g[0]) - 1):
            for color, shape in shapes.items():
                loc = frozenset(((r + dr, c + dc) for dr, dc in shape))
                if loc <= cells:
                    i = len(options)
                    options.append((color, loc))
                    for p in loc:
                        bycell[p].append(i)
    answers = set()

    def search(left, paint):
        if len(answers) > 1:
            return
        if not left:
            answers.add(tuple(sorted(paint)))
            return
        p = min(left, key=lambda p: sum(options[i][1] <= left for i in bycell[p]))
        for i in bycell[p]:
            color, loc = options[i]
            if loc <= left:
                search(left - loc, paint + [(r, c, color) for r, c in loc])

    search(cells, [])
    if len(answers) != 1:
        raise ValueError(("Tiling not unique", len(answers)))
    out = cp(g)
    for r, c, color in next(iter(answers)):
        out[r][c] = color
    return out
