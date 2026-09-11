def solve(grid):
    h, w = len(grid), len(grid[0])
    min_length = 4
    entries = []
    for color in sorted({value for row in grid for value in row if value}):
        if color == 0:
            continue
        seen = set()
        for r in range(h):
            for c in range(w):
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
                            0 <= nr < h
                            and 0 <= nc < w
                            and grid[nr][nc] == color
                            and (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                rows = [row for row, _ in component]
                cols = [col for _, col in component]
                height = max(rows) - min(rows) + 1
                width = max(cols) - min(cols) + 1
                if len(component) >= min_length and (height == 1 or width == 1):
                    entries.append((min(rows), min(cols), color, 0 if width == 1 else 1))
    if not entries:
        return [row[:] for row in grid]
    vertical = all((axis == 0 for _, _, _, axis in entries))
    entries.sort(key=lambda item: (item[1], item[0]) if vertical else (item[0], item[1]))
    size = len(entries)
    if vertical:
        colors = [color for _, _, color, _ in entries]
        return [colors[:] for _ in range(size)]
    return [[color] * size for _, _, color, _ in entries]
