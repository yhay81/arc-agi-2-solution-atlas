def solve(grid):
    units = sum(cell != 0 for row in grid for cell in row) // 4
    block = [[8 if row * 2 + col >= 4 - units else 0 for col in range(2)] for row in range(2)]
    return [
        [block[row % 3][col % 3] if row % 3 < 2 and col % 3 < 2 else 0 for col in range(5)]
        for row in range(5)
    ]
