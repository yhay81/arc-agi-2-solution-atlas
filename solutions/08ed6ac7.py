def solve(grid):
    h, w = len(grid), len(grid[0])
    colors = [1, 2, 3, 4]
    order = "top_left"
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
    if order == "size_desc":
        components.sort(key=len, reverse=True)
    elif order == "size_asc":
        components.sort(key=len)
    elif order == "bottom_left":
        components.sort(
            key=lambda item: (-max((row for row, _ in item)), min((col for _, col in item)))
        )
    else:
        components.sort(
            key=lambda item: (min((row for row, _ in item)), min((col for _, col in item)))
        )
    if len(colors) < len(components):
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for color, component in zip(colors, components, strict=False):
        for row, col in component:
            output[row][col] = color
    return output
