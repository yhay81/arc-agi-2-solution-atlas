def solve(grid):
    a = grid
    if (len(a), len(a[0])) != (5, 1):
        raise ValueError("Expected a five-row color column")
    return [a[i][:] for i in (1, 0, 2, 4, 3)]
