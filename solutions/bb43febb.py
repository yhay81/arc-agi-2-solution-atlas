def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if all(grid[row + dr][col + dc] == 5 for dr in (-1, 0, 1) for dc in (-1, 0, 1)):
                output[row][col] = 2
    return output
