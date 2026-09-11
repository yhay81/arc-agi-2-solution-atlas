def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def shape_key(o):
    shape = normalized_shape(o)
    return min(freeze(transform(shape, t)) for t in range(8))


def transform(g, t):
    x = [list(r) for r in g]
    if t >= 4:
        x = [row[::-1] for row in x]
    for _ in range(t % 4):
        x = [list(r) for r in zip(*x[::-1])]
    return x


def normalized_shape(o):
    a, b, c, d = bbox(o)
    return tuple(tuple(int((r, col) in set(o)) for col in range(c, d + 1)) for r in range(a, b + 1))


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def freeze(g):
    return tuple(tuple(r) for r in g)


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    legend = [(r, len(g[0]) - 1, v) for r, row in enumerate(g) if (v := row[-1]) != 0]
    colors = [v for r, c, v in legend]
    patterns = {}
    for color in colors:
        o = [(r, c) for r, c in points(g, color) if c != len(g[0]) - 1]
        patterns[color] = shape_key(o)
    n = len(colors) + 1
    matrix = [[0] * n for _ in range(n)]
    for i, color in enumerate(colors, 1):
        matrix[0][i] = matrix[i][0] = color
    for i, color in enumerate(colors, 1):
        for j, other in enumerate(colors, 1):
            if i != j:
                matrix[i][j] = 2 if patterns[color] == patterns[other] else 5
    return [
        [0 if r % 3 == 2 or c % 3 == 2 else matrix[r // 3][c // 3] for c in range(3 * n - 1)]
        for r in range(3 * n - 1)
    ]
