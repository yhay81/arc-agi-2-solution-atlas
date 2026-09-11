def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
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
            if len(component) < 4:
                continue
            rows = [r for r, _ in component]
            cols = [c for _, c in component]
            top, bottom, left, right = (min(rows), max(rows), min(cols), max(cols))
            depth_values = {}
            for row, col in component:
                depth = min(row - top, bottom - row, col - left, right - col)
                depth_values.setdefault(depth, []).append(grid[row][col])
            if len(depth_values) < 2:
                continue
            depths = sorted(depth_values)
            if depths != list(range(depths[-1] + 1)):
                continue
            colors = [max(set(depth_values[d]), key=depth_values[d].count) for d in depths]
            if any(len(set(depth_values[d])) > 2 for d in depths):
                continue
            runs = []
            for color in colors:
                if not runs or runs[-1] != color:
                    runs.append(color)
            color_map = {color: runs[-1 - index] for index, color in enumerate(runs)}
            for row, col in component:
                depth = min(row - top, bottom - row, col - left, right - col)
                output[row][col] = color_map[colors[depth]]
    return output
