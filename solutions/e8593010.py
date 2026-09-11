def solve(grid):
    height, width = len(grid), len(grid[0])
    colors = {value for row in grid for value in row if value}
    if len(colors) != 1 or not any(not value for row in grid for value in row):
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    remaining = {(r, c) for r in range(height) for c in range(width) if not grid[r][c]}
    holes = []
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
        holes.append(cells)
    if not holes or any(len(hole) > 3 for hole in holes):
        return [row[:] for row in grid]
    for hole in holes:
        for row, col in hole:
            output[row][col] = 4 - len(hole)
    return output
