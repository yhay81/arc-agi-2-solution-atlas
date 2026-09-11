def solve(grid):
    h, w = len(grid), len(grid[0])
    if len({value for row in grid for value in row if value}) != 1:
        return [row[:] for row in grid]
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
    if len(components) < 2:
        return [row[:] for row in grid]
    shapes = []
    for component in components:
        top = min((row for row, _ in component))
        left = min((col for _, col in component))
        shapes.append(tuple(sorted(((row - top, col - left) for row, col in component))))
    counts = {shape: shapes.count(shape) for shape in set(shapes)}
    if not any(count == 1 for count in counts.values()) or not any(
        count > 1 for count in counts.values()
    ):
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for component, shape in zip(components, shapes, strict=True):
        color = 2 if counts[shape] == 1 else 1
        for row, col in component:
            output[row][col] = color
    return output
