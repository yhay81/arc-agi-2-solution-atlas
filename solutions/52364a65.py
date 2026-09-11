def components(grid, color):
    h, w = len(grid), len(grid[0])
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != color or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            group = []
            while stack:
                y, x = stack.pop()
                group.append((y, x))
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    p = y + dy, x + dx
                    if (
                        0 <= p[0] < h
                        and 0 <= p[1] < w
                        and grid[p[0]][p[1]] == color
                        and p not in seen
                    ):
                        seen.add(p)
                        stack.append(p)
            yield group


def solve(grid):
    output = [row[:] for row in grid]
    for color in sorted({v for row in grid for v in row} - {8}):
        for group in components(grid, color):
            left = min(c for _, c in group)
            for r, c in group:
                if c < left + 2:
                    output[r][c] = 8
    return output
