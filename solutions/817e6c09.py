from collections import deque


def objects(g, diagonal=False):
    seen = set()
    result = []
    h, w = (len(g), len(g[0]))
    for r in range(h):
        for c in range(w):
            if g[r][c] == 0 or (r, c) in seen:
                continue
            color = g[r][c]
            q = deque([(r, c)])
            seen.add((r, c))
            cells = []
            while q:
                a, b = q.popleft()
                cells.append((a, b))
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if (not dr and (not dc)) or (not diagonal and dr and dc):
                            continue
                        x, y = (a + dr, b + dc)
                        if (
                            0 <= x < h
                            and 0 <= y < w
                            and (g[x][y] == color)
                            and ((x, y) not in seen)
                        ):
                            seen.add((x, y))
                            q.append((x, y))
            result.append((color, cells))
    return result


def solve(grid):
    g = grid
    out = [r[:] for r in g]
    obs = sorted(
        (cells for color, cells in objects(g) if color == 2),
        key=lambda cs: min((c for r, c in cs)),
        reverse=True,
    )
    for rank, cells in enumerate(obs):
        if rank % 2 == 0:
            for r, c in cells:
                out[r][c] = 8
    return out
