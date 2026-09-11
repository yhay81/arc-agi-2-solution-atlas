from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


def bounds(points):
    rs, cs = zip(*points)
    return min(rs), min(cs), max(rs), max(cs)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    bg = mode([v for row in a for v in row])
    out = [row[:] for row in a]
    for col in {v for row in a for v in row} - {bg}:
        ps = {(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == col}
        left = min((c for r, c in ps))
        right = max((c for r, c in ps))

        def score(axis):
            kept = [(r, c) for r, c in ps if (r, axis - c) in ps]
            if not kept:
                return (len(ps), 999, 999, axis)
            r, c, b, d = bounds(kept)
            return (len(ps) - len(kept), abs(b - r - (d - c)), abs(axis - left - right), axis)

        axis = min(range(2 * left, 2 * right + 1), key=score)
        for r, c in ps:
            if (r, axis - c) not in ps:
                out[r][c] = bg
    return out
