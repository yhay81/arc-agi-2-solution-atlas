def solve(grid):
    output = [row[:] for row in grid]
    for row in range(len(grid)):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col - 1 : col + 2] == [1, 0, 1]:
                output[row][col] = 2
    return output
