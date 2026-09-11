def solve(grid):
    return [
        [6 if cell == 4 and col % 3 == 0 else cell for col, cell in enumerate(row)] for row in grid
    ]
