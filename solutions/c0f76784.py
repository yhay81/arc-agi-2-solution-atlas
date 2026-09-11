def solve(grid):
    output = [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 5 or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            cells = []
            while stack:
                y, x = stack.pop()
                cells.append((y, x))
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    p = (y + dy, x + dx)
                    if 0 <= p[0] < h and 0 <= p[1] < w and grid[p[0]][p[1]] == 5 and p not in seen:
                        seen.add(p)
                        stack.append(p)
            rows = [y for y, x in cells]
            cols = [x for y, x in cells]
            top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
            height, width = bottom - top + 1, right - left + 1
            border = [[grid[y][x] for x in range(left, right + 1)] for y in range(top, bottom + 1)]
            if (
                height == width
                and all(border[0])
                and all(border[-1])
                and all(row[0] for row in border)
                and all(row[-1] for row in border)
            ):
                for y in range(top + 1, bottom):
                    for x in range(left + 1, right):
                        output[y][x] = height + 3
    return output
