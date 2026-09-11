def solve(grid):
    h, w = len(grid), len(grid[0])
    colors = sorted({value for row in grid for value in row if value})
    if len(colors) != 1:
        return [row[:] for row in grid]
    color = colors[0]
    seen = set()
    components = []
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
            components.append(component)
    if not components:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for component in components:
        rows = [row for row, _ in component]
        cols = [col for _, col in component]
        top, bottom, left, right = (min(rows), max(rows), min(cols), max(cols))
        side = bottom - top + 1
        if side < 3 or side != right - left + 1:
            return [row[:] for row in grid]
        border = {
            (row, col)
            for row in range(top, bottom + 1)
            for col in range(left, right + 1)
            if row in (top, bottom) or col in (left, right)
        }
        if set(component) != border:
            return [row[:] for row in grid]
        fill = 7 if side % 2 else 2
        for row in range(top + 1, bottom):
            output[row][left + 1 : right] = [fill] * (right - left - 1)
    return output
