def solve(grid):
    g = grid
    return [
        [8 if a or b else 0 for a, b in zip(row[: len(row) // 2], row[len(row) // 2 + 1 :])]
        for row in g
    ]
