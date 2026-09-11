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
            component = []
            while stack:
                cr, cc = stack.pop()
                component.append((cr, cc))
                for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
                    if (
                        0 <= nr < height
                        and 0 <= nc < width
                        and grid[nr][nc]
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            components.append(component)
    if not components:
        return [row[:] for row in grid]
    scores = [sum(grid[row][col] != 1 for row, col in component) for component in components]
    best_score = min(scores)
    choices = [
        component
        for component, score in zip(components, scores, strict=True)
        if score == best_score
    ]
    if len(choices) != 1:
        return [row[:] for row in grid]
    component = choices[0]
    top, bottom = min(row for row, _ in component), max(row for row, _ in component)
    left, right = min(col for _, col in component), max(col for _, col in component)
    cells = set(component)
    return [
        [grid[r][c] if (r, c) in cells else 0 for c in range(left, right + 1)]
        for r in range(top, bottom + 1)
    ]
