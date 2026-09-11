def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c]}
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
        size = len(cells)
        if size <= 9:
            for r, c in cells:
                output[r][c] = size
    return [[{0: 0, 3: 2, 2: 3, 4: 1}.get(value, value) for value in row] for row in output]
