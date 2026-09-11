def solve(grid):
    h, w = len(grid), len(grid[0])
    frame = 8
    object_color = 2
    output = [row[:] for row in grid]
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != frame or (r, c) in seen:
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
                        and grid[nr][nc] == frame
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            rows = [row for row, _ in component]
            cols = [col for _, col in component]
            top, bottom, left, right = (min(rows), max(rows), min(cols), max(cols))
            if bottom - top < 4 or right - left < 4:
                continue
            cells = [
                (row, col)
                for row in range(top, bottom + 1)
                for col in range(left, right + 1)
                if grid[row][col] == object_color
            ]
            for row, col in cells:
                targets = (
                    (row, left + right - col),
                    (top + bottom - row, col),
                    (top + bottom - row, left + right - col),
                )
                for target_row, target_col in targets:
                    if output[target_row][target_col] == 0:
                        output[target_row][target_col] = object_color
    return output
