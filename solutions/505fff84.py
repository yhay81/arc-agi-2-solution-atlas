def solve(grid):
    g = grid
    o = []
    for row in g:
        if 1 in row and 8 in row:
            a, b = sorted([row.index(1), row.index(8)])
            o.append(row[a + 1 : b])
    if not (o):
        raise ValueError("task assumptions are not satisfied")
    return o
