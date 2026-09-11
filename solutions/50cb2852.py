def solve(grid):
    output = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    seen = set()
    for r in range(h):
        for c in range(w):
            color = grid[r][c]
            if not color or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            group = []
            while stack:
                y, x = stack.pop()
                group.append((y, x))
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    p = (y + dy, x + dx)
                    if (
                        0 <= p[0] < h
                        and 0 <= p[1] < w
                        and grid[p[0]][p[1]] == color
                        and p not in seen
                    ):
                        seen.add(p)
                        stack.append(p)
            ys = [y for y, x in group]
            xs = [x for y, x in group]
            top, bottom = min(ys), max(ys)
            left, right = min(xs), max(xs)
            if all(
                grid[y][x] == color for y in range(top, bottom + 1) for x in range(left, right + 1)
            ):
                for y in range(top + 1, bottom):
                    for x in range(left + 1, right):
                        output[y][x] = 8
    return output
