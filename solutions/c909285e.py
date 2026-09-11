def solve(grid):
    height, width = len(grid), len(grid[0])
    choices = []
    for color in sorted({value for row in grid for value in row}):
        occupied = [[grid[r][c] == color for c in range(width)] for r in range(height)]
        seen = set()
        components = []
        for r in range(height):
            for c in range(width):
                if not occupied[r][c] or (r, c) in seen:
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
                            and occupied[nr][nc]
                            and (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                components.append(cells)
        if len(components) == 1:
            choices.append(components[0])
    if not choices:
        return [row[:] for row in grid]
    component = min(choices, key=len)
    top = min(row for row, _ in component)
    bottom = max(row for row, _ in component)
    left = min(col for _, col in component)
    right = max(col for _, col in component)
    return [row[left : right + 1] for row in grid[top : bottom + 1]]
