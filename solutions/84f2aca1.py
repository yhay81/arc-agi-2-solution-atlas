def solve(grid):
    out = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            cells = []
            edge = False
            while stack:
                y, x = stack.pop()
                cells.append((y, x))
                edge |= y in (0, h - 1) or x in (0, w - 1)
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    p = (y + dy, x + dx)
                    if 0 <= p[0] < h and 0 <= p[1] < w and not grid[p[0]][p[1]] and p not in seen:
                        seen.add(p)
                        stack.append(p)
            if not edge:
                color = {1: 5, 2: 7}[len(cells)]
                for y, x in cells:
                    out[y][x] = color
    return out
