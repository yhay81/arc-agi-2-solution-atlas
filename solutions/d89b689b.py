def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    components = []
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
            components.append(component)
    bodies = [component for component in components if len(component) > 1]
    markers = [component for component in components if len(component) == 1]
    if len(bodies) != 1 or len(markers) != 4:
        return [row[:] for row in grid]
    body = bodies[0]
    top, bottom = min(r for r, _ in body), max(r for r, _ in body)
    left, right = min(c for _, c in body), max(c for _, c in body)
    if bottom - top != 1 or right - left != 1 or len(body) != 4:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    placements = {}
    center_row, center_col = (top + bottom) / 2, (left + right) / 2
    for component in markers:
        row, col = component[0]
        target = (top if row < center_row else bottom, left if col < center_col else right)
        if target in placements:
            return [row[:] for row in grid]
        placements[target] = grid[row][col]
        output[row][col] = 0
    for (row, col), color in placements.items():
        output[row][col] = color
    return output
