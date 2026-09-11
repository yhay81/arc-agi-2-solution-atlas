def solve(grid):
    height, width = len(grid), len(grid[0])
    largest = True
    components = []
    for color in sorted({value for row in grid for value in row if value}):
        seen = set()
        for r in range(height):
            for c in range(width):
                if grid[r][c] != color or (r, c) in seen:
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
                            and grid[nr][nc] == color
                            and (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                components.append(component)
    if not components:
        return [row[:] for row in grid]
    component = (max if largest else min)(components, key=len)
    top, bottom = min(r for r, _ in component), max(r for r, _ in component)
    left, right = min(c for _, c in component), max(c for _, c in component)
    return [row[left : right + 1] for row in grid[top : bottom + 1]]
