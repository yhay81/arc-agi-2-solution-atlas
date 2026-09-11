def solve(grid):
    output = [row[:] for row in grid]
    parity = (len(grid[0]) - 1) % 2
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == 5 and c % 2 == parity:
                output[r][c] = 3
    return output
