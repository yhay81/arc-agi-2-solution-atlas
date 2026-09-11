def solve(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    for r in range(h):
        for c in range(w):
            if not grid[r][c] or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            component = []
            while stack:
                cr, cc = stack.pop()
                component.append((cr, cc))
                for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            if len(component) < 4:
                continue
            top = min((row for row, _ in component))
            left = min((col for _, col in component))
            bottom = max((row for row, _ in component))
            right = max((col for _, col in component))
            values = {grid[row][col] for row, col in component}
            if len(values) != 1:
                continue
            source = next(iter(values))
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    if grid[row][col] == 0:
                        continue
                    distance = min(row - top, bottom - row, col - left, right - col)
                    output[row][col] = source if distance == 0 else 2 if distance % 2 else 3
    return output
