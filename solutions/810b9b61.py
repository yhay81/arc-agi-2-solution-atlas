def solve(grid):
    h, w = len(grid), len(grid[0])
    source_color = 1
    target_color = 3
    output = [row[:] for row in grid]
    source, target = source_color, target_color
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != source or (r, c) in seen:
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
                        and grid[nr][nc] == source
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            if len(component) < 8:
                continue
            rows = [row for row, _ in component]
            cols = [col for _, col in component]
            top, bottom, left, right = (min(rows), max(rows), min(cols), max(cols))
            if bottom - top < 2 or right - left < 2:
                continue
            perimeter = {
                *[(top, col) for col in range(left, right + 1)],
                *[(bottom, col) for col in range(left, right + 1)],
                *[(row, left) for row in range(top, bottom + 1)],
                *[(row, right) for row in range(top, bottom + 1)],
            }
            cells = set(component)
            if cells != perimeter:
                continue
            for row, col in component:
                output[row][col] = target
    return output
