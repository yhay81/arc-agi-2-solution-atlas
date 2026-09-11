from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]
    colors = [value for value in counts if value != background]
    if len(colors) != 1:
        return [row[:] for row in grid]
    frame = colors[0]
    seen = set()
    components = []
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
            top, bottom = min(r for r, _ in component), max(r for r, _ in component)
            left, right = min(c for _, c in component), max(c for _, c in component)
            side = bottom - top + 1
            border = {
                (r, c)
                for r in range(top, bottom + 1)
                for c in range(left, right + 1)
                if r in (top, bottom) or c in (left, right)
            }
            if side < 3 or side % 2 == 0 or side != right - left + 1 or set(component) != border:
                return [row[:] for row in grid]
            components.append(((top + bottom) // 2, (left + right) // 2))
    output = [row[:] for row in grid]
    for center_row, center_col in components:
        for col in range(w):
            if grid[center_row][col] == background:
                output[center_row][col] = 6
        for row in range(h):
            if grid[row][center_col] == background:
                output[row][center_col] = 6
    return output
