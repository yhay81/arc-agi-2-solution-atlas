from collections import Counter


def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = cp(g)
    out = cp(g)
    quadrants = []
    for rows in ((0, 1), (3, 4)):
        for cols in ((0, 1), (3, 4)):
            quadrants.append(
                (rows, cols, Counter(g[r][c] for r in rows for c in cols if g[r][c] != 7))
            )
    target = Counter()
    for _, _, counts in quadrants:
        for color, n in counts.items():
            target[color] = max(target[color], n)
    if sum(target.values()) != 4:
        raise ValueError("Common quadrant multiset is ambiguous")
    for rows, cols, present in quadrants:
        missing = target - present
        if sum(missing.values()) != 1:
            raise ValueError("Missing quadrant color is ambiguous")
        color = next(missing.elements())
        for r in rows:
            for c in cols:
                if g[r][c] == 7:
                    out[r][c] = color
    return out
