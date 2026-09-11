def solve(grid):
    g = grid
    g = [row[:] for row in g]
    marks = [(r, c, v) for r, row in enumerate(g) for c, v in enumerate(row) if v not in (0, 1)]
    if len({v for r, c, v in marks}) != 1:
        raise ValueError("Ambiguous seed color")
    color = marks[0][2]
    rows = {r for r, c, v in marks}
    cols = {c for r, c, v in marks}
    return [
        [color if v == 1 and (r in rows or c in cols) else v for c, v in enumerate(row)]
        for r, row in enumerate(g)
    ]
