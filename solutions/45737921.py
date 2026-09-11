from collections import deque


def groups(grid, monochrome=True):
    unseen = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v != 0}
    result = []
    while unseen:
        start = min(unseen)
        color = grid[start[0]][start[1]]
        unseen.remove(start)
        q = deque([start])
        cells = []
        while q:
            r, c = q.popleft()
            cells.append((r, c))
            for p in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if p in unseen and (not monochrome or grid[p[0]][p[1]] == color):
                    unseen.remove(p)
                    q.append(p)
        result.append((color, cells))
    return result


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = [r[:] for r in g]
    for _, cells in groups(g, False):
        colors = {g[r][c] for r, c in cells}
        if len(colors) != 2:
            raise ValueError("Expected two colors per object")
        a, b = sorted(colors)
        for r, c in cells:
            out[r][c] = b if g[r][c] == a else a
    return out
