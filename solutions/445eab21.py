def solve(grid):
    h, w = len(grid), len(grid[0])
    rectangles = []
    for color in sorted({value for row in grid for value in row if value}):
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
                rows = [r for r, _ in component]
                cols = [c for _, c in component]
                top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
                box_h, box_w = bottom - top + 1, right - left + 1
                if len(component) != 2 * box_h + 2 * box_w - 4 or box_h < 3 or box_w < 3:
                    continue
                border = {
                    (r, c)
                    for r in range(top, bottom + 1)
                    for c in range(left, right + 1)
                    if r in (top, bottom) or c in (left, right)
                }
                if set(component) == border:
                    rectangles.append((box_h * box_w, color))
    if not rectangles:
        return [row[:] for row in grid]
    return [[max(rectangles)[1]] * 2 for _ in range(2)]
