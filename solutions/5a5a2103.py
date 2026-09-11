def cp(g):
    return [row[:] for row in g]


def panels(g, separator):
    h, w = (len(g), len(g[0]))
    rs = [-1] + [r for r, row in enumerate(g) if all(v == separator for v in row)] + [h]
    cs = [-1] + [c for c in range(w) if all(row[c] == separator for row in g)] + [w]
    return [
        (a + 1, c + 1, [row[c + 1 : d] for row in g[a + 1 : b]])
        for a, b in zip(rs, rs[1:])
        for c, d in zip(cs, cs[1:])
        if b > a + 1 and d > c + 1
    ]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    separators = {row[0] for row in g if len(set(row)) == 1 and row[0] != 0}
    if len(separators) != 1:
        raise ValueError("Expected unique grid line color")
    ps = panels(g, separators.pop())
    templates = []
    for r, c, p in ps:
        nonzero = [(rr, cc) for rr, row in enumerate(p) for cc, v in enumerate(row) if v != 0]
        if nonzero and (
            len(nonzero) != 4
            or bbox(nonzero)[1] - bbox(nonzero)[0] != 1
            or bbox(nonzero)[3] - bbox(nonzero)[2] != 1
        ):
            templates.append(p)
    if len(templates) != 1:
        raise ValueError("Expected unique shape template")
    template = templates[0]
    out = cp(g)
    for r in sorted({r for r, c, p in ps}):
        rowpanels = [(c, p) for rr, c, p in ps if rr == r]
        first = min(rowpanels)[1]
        colors = set(v for row in first for v in row) - {0}
        if len(colors) != 1:
            raise ValueError("Ambiguous row instruction")
        color = colors.pop()
        for c, p in rowpanels:
            for dr, row in enumerate(template):
                for dc, v in enumerate(row):
                    out[r + dr][c + dc] = color if v else 0
    return out
