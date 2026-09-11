def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 2 or (row, col) in seen:
                continue
            seen.add((row, col))
            stack, component = [(row, col)], {(row, col)}
            while stack:
                r, c = stack.pop()
                for point in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (
                        0 <= point[0] < height
                        and 0 <= point[1] < width
                        and grid[point[0]][point[1]] == 2
                        and point not in seen
                    ):
                        seen.add(point)
                        component.add(point)
                        stack.append(point)
            if len(component) != 2:
                continue
            top, bottom = min(r for r, _ in component), max(r for r, _ in component)
            left, right = min(c for _, c in component), max(c for _, c in component)
            if (bottom - top + 1) * (right - left + 1) != 2:
                continue
            for r in range(max(0, top - 1), min(height, bottom + 2)):
                for c in range(max(0, left - 1), min(width, right + 2)):
                    if (r in (top - 1, bottom + 1) or c in (left - 1, right + 1)) and not output[r][
                        c
                    ]:
                        output[r][c] = 3
    return output
