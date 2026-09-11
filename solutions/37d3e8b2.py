def groups(grid, color):
    h, w = len(grid), len(grid[0])
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != color or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            g = []
            while stack:
                y, x = stack.pop()
                g.append((y, x))
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
            yield g


def solve(grid):
    a = grid
    out = [row[:] for row in a]
    h, w = len(a), len(a[0])
    for ps in groups(a, 8):
        cells = set(ps)
        holes = 0
        top, bottom = min(r for r, c in ps), max(r for r, c in ps)
        left, right = min(c for r, c in ps), max(c for r, c in ps)
        seen = set()
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                if a[r][c] != 0 or (r, c) in seen:
                    continue
                stack = [(r, c)]
                seen.add((r, c))
                enclosed = True
                while stack:
                    y, x = stack.pop()
                    if y in (top, bottom) or x in (left, right):
                        enclosed = False
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        p = (y + dy, x + dx)
                        if (
                            top <= p[0] <= bottom
                            and left <= p[1] <= right
                            and a[p[0]][p[1]] == 0
                            and p not in seen
                        ):
                            seen.add(p)
                            stack.append(p)
                holes += enclosed
        color = {1: 1, 2: 2, 3: 3, 4: 7}[holes]
        for r, c in ps:
            out[r][c] = color
    return out
