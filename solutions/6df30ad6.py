def solve(grid):
    g = grid
    gray = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 5]
    dots = [(r, c, v) for r, row in enumerate(g) for c, v in enumerate(row) if v not in (0, 5)]
    distances = [min(((r - a) ** 2 + (c - b) ** 2 for a, b in gray)) for r, c, v in dots]
    colors = {v for (r, c, v), d in zip(dots, distances) if d == min(distances)}
    if len(colors) != 1:
        raise ValueError("color of the nearest point is not unique")
    color = next(iter(colors))
    return [[color if v == 5 else 0 for v in row] for row in g]
