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
            top, bottom = min(r for r, _ in component), max(r for r, _ in component)
            left, right = min(c for _, c in component), max(c for _, c in component)
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    if output[row][col] == 0:
                        output[row][col] = 1
    return [[0 if value == 0 else 8 if value == 8 else 2 for value in row] for row in output]
