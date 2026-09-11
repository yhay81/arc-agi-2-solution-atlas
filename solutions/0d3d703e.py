def solve(grid):
    substitutions = {1: 5, 2: 6, 3: 4, 4: 3, 5: 1, 6: 2, 8: 9, 9: 8}
    return [[substitutions.get(cell, cell) for cell in row] for row in grid]
