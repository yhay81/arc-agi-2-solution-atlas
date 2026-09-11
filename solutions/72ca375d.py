def solve(grid):
    h, w = len(grid), len(grid[0])
    symmetric = []
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
                if len(component) < 2:
                    continue
                rows = [row for row, _ in component]
                cols = [col for _, col in component]
                top, bottom, left, right = (min(rows), max(rows), min(cols), max(cols))
                box_h, box_w = bottom - top + 1, right - left + 1
                mask = {(row - top, col - left) for row, col in component}
                if all(
                    ((row, col) in mask) == ((row, box_w - 1 - col) in mask)
                    for row in range(box_h)
                    for col in range(box_w)
                ):
                    symmetric.append(
                        [
                            [color if (row, col) in mask else 0 for col in range(box_w)]
                            for row in range(box_h)
                        ]
                    )
    if len(symmetric) != 1:
        return [row[:] for row in grid]
    return symmetric[0]
