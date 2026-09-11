def solve(grid):
    output = [row[:] for row in grid]
    if len(grid) < 2 or any(value != 5 for value in grid[1]):
        return output
    header = grid[0]
    for row in range(2, len(grid)):
        output[row] = [header[(row - 2) % len(header)]] * len(header)
    return output
