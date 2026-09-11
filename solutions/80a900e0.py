def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    out = cp(g)
    ring = [(dr, dc) for dr in range(-2, 3) for dc in range(-2, 3) if abs(dr) + abs(dc) == 2]
    for r in range(2, h - 2):
        for c in range(2, w - 2):
            colors = {g[r + dr][c + dc] for dr, dc in ring}
            if len(colors) != 1 or next(iter(colors)) in (0, 1):
                continue
            for sr in (-1, 1):
                for sc in (-1, 1):
                    cap = [(r + sr * k, c + sc * (4 - k)) for k in (1, 2, 3)]
                    visible = [(rr, cc) for rr, cc in cap if 0 <= rr < h and 0 <= cc < w]
                    if len(visible) < 2:
                        continue
                    vals = {g[rr][cc] for rr, cc in visible}
                    if len(vals) != 1 or next(iter(vals)) in (0, 1):
                        continue
                    color = next(iter(vals))
                    for rr, cc in (cap[0], cap[-1]):
                        while 0 <= rr < h and 0 <= cc < w:
                            if g[rr][cc] in (0, 1, color):
                                out[rr][cc] = color
                            rr += sr
                            cc += sc
    return out
