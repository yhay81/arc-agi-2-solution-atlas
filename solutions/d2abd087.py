def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [[0] * width for _ in range(height)]
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c]}
    while remaining:
        start = remaining.pop()
        stack, cells = [start], [start]
        while stack:
            row, col = stack.pop()
            for point in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if point in remaining:
                    remaining.remove(point)
                    cells.append(point)
                    stack.append(point)
        color = 2 if len(cells) == 6 else 1
        for row, col in cells:
            output[row][col] = color
    return output
