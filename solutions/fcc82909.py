from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    if not counts:
        return [row[:] for row in grid]
    background = counts.most_common(1)[0][0]
    output = [row[:] for row in grid]
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] == background or (r, c) in seen:
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
                        and grid[nr][nc] != background
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            rows = [r for r, _ in component]
            cols = [c for _, c in component]
            top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
            if (bottom - top, right - left) != (1, 1) or len(component) != 4:
                continue
            palette_size = len({grid[r][c] for r, c in component})
            for row in range(bottom + 1, min(h, bottom + 1 + palette_size)):
                for col in range(left, right + 1):
                    if output[row][col] == background:
                        output[row][col] = 3
    return output
