def solve(grid):
    g = grid
    colors = sorted({v for row in g for v in row})
    if len(colors) != 2:
        raise ValueError("Expected exactly two colors")
    a, b = colors
    swapped = [[b if v == a else a for v in row] for row in g]
    return [row * 2 for row in swapped] * 2
