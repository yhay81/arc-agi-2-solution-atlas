def solve(grid):
    output = [row[:] for row in grid]
    for row in range(len(output) - 2):
        for col in range(len(output[0]) - 2):
            if all(output[r][c] == 0 for r in range(row, row + 3) for c in range(col, col + 3)):
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        output[r][c] = 1
    return output
