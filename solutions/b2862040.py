def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 1 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            component = []
            while stack:
                r, c = stack.pop()
                component.append((r, c))
                for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= rr < height
                        and 0 <= cc < width
                        and grid[rr][cc] == 1
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            if len(component) < 4:
                continue
            top, bottom = min(r for r, _ in component), max(r for r, _ in component)
            left, right = min(c for _, c in component), max(c for _, c in component)
            if bottom - top < 2 or right - left < 2:
                continue
            open_cells = {
                (r, c)
                for r in range(top, bottom + 1)
                for c in range(left, right + 1)
                if grid[r][c] != 1
            }
            visited = set()
            stack = [
                cell for cell in open_cells if cell[0] in (top, bottom) or cell[1] in (left, right)
            ]
            visited.update(stack)
            while stack:
                r, c = stack.pop()
                for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (rr, cc) in open_cells and (rr, cc) not in visited:
                        visited.add((rr, cc))
                        stack.append((rr, cc))
            if open_cells - visited:
                for r, c in component:
                    output[r][c] = 8
    return output
