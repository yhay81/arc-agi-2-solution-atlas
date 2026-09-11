def solve(grid):
    a = grid
    if not (len(a) == len(a[0])):
        raise ValueError("task assumptions are not satisfied")
    return [row[:2] if len(a[0]) % 2 else row[-2:] for row in a[:2]]
