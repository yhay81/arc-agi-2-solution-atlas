def solve(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    components = []
    for r in range(height):
        for c in range(width):
            if not grid[r][c] or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            cells = []
            while stack:
                cr, cc = stack.pop()
                cells.append((cr, cc))
                for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
                    if (
                        0 <= nr < height
                        and 0 <= nc < width
                        and grid[nr][nc]
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            components.append(cells)
    if not components:
        return [row[:] for row in grid]
    scores = [sum(grid[r][c] == 2 for r, c in component) for component in components]
    best = max(scores)
    if best == 0 or scores.count(best) != 1:
        return [row[:] for row in grid]
    component = components[scores.index(best)]
    top, bottom = min(r for r, _ in component), max(r for r, _ in component)
    left, right = min(c for _, c in component), max(c for _, c in component)
    return [
        [grid[r][c] if (r, c) in component else 0 for c in range(left, right + 1)]
        for r in range(top, bottom + 1)
    ]
