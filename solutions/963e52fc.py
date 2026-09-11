def solve(grid):
    output = []
    for row in grid:
        period = len(row)
        for candidate in range(1, len(row) + 1):
            if all(row[col] == row[col % candidate] for col in range(len(row))):
                period = candidate
                break
        output.append([row[col % period] for col in range(len(row) * 2)])
    return output
