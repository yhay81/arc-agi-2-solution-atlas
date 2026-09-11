def components(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 5 or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            g = []
            while stack:
                y, x = stack.pop()
                g.append((y, x))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        p = (y + dy, x + dx)
                        if (
                            0 <= p[0] < h
                            and 0 <= p[1] < w
                            and grid[p[0]][p[1]] == 5
                            and p not in seen
                        ):
                            seen.add(p)
                            stack.append(p)
            yield g


def solve(grid):
    a = grid
    out = [row[:] for row in a]
    for p in components(a):
        s = set(p)
        if any(all((r + k, c + sign * k) in s for k in range(3)) for r, c in s for sign in (-1, 1)):
            for r, c in p:
                out[r][c] = 8
    return out
