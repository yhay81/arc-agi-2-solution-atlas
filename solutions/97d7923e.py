from collections import Counter


def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = cp(g)
    out = cp(g)
    legend = Counter()
    bars = {}
    for c in range(len(g[0])):
        r = 0
        while r < len(g):
            if g[r][c] == 0:
                r += 1
                continue
            start = r
            while r < len(g) and g[r][c] != 0:
                r += 1
            vals = [g[rr][c] for rr in range(start, r)]
            if len(set(vals)) == 1:
                legend[vals[0]] += len(vals)
            elif vals[0] == vals[-1]:
                bars.setdefault(vals[0], []).append((len(vals), start, r, c))
    for color, items in bars.items():
        rank = legend[color]
        ordered = sorted(items, reverse=True)
        if not 1 <= rank <= len(ordered):
            raise ValueError("Rank outside bar count")
        length, a, b, c = ordered[rank - 1]
        for r in range(a, b):
            out[r][c] = color
    return out
