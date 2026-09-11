def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for color in {cell for row in grid for cell in row if cell}:
        remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == color}
        while remaining:
            start = remaining.pop()
            stack, cells = [start], [start]
            while stack:
                r, c = stack.pop()
                for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if point in remaining:
                        remaining.remove(point)
                        cells.append(point)
                        stack.append(point)
            columns = [c for _, c in cells]
            output[-1][(min(columns) + max(columns)) // 2] = 4
    return output
