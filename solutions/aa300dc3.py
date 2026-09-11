def pts(g, color):
    return {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color}


def cp(g):
    return [list(r) for r in g]


def paint(g, p, color):
    for r, c in p:
        if 0 <= r < len(g) and 0 <= c < len(g[0]):
            g[r][c] = color
    return g


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    black = pts(g, 0)
    cr = sum((r for r, c in black)) / len(black)
    cc_ = sum((c for r, c in black)) / len(black)
    cands = []
    for r, c in black:
        for dc in (-1, 1):
            p = set()
            rr, z = (r, c)
            while (rr, z) in black:
                p.add((rr, z))
                rr += 1
                z += dc
            cands.append(
                (p, abs((r - c if dc == 1 else r + c) - (cr - cc_ if dc == 1 else cr + cc_)))
            )
    return paint(cp(g), min(cands, key=lambda t: (-len(t[0]), t[1]))[0], 8)
