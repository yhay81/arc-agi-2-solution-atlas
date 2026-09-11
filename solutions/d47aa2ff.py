def solve(grid):
    width = len(grid[0])
    middle = width // 2
    if width % 2 != 1 or not all(row[middle] == 5 for row in grid):
        raise ValueError("Expected two equal panels separated by a gray column")
    out = []
    for row in grid:
        line = []
        for left, right in zip(row[:middle], row[middle + 1 :], strict=True):
            if left == right:
                line.append(left)
            elif right == 0:
                line.append(2)
            elif left == 0:
                line.append(1)
            else:
                raise ValueError("Two different nonblack colors at one position")
        out.append(line)
    return out
