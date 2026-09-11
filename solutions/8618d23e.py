def solve(grid):
    a = grid
    k = len(a) // 2
    w = len(a[0])
    if not (len(a) % 2 == 0):
        raise ValueError("task assumptions are not satisfied")
    return [row + [9] for row in a[:k]] + [[9] * (w + 1)] + [[9] + row for row in a[k:]]
