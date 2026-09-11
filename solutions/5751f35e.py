from collections import Counter


def solve(grid):
    a = grid
    h, w = (len(a), len(a[0]))
    pal = {}
    for r in range(h):
        for c in range(w):
            if a[r][c]:
                pal.setdefault(min(r, c, h - r - 1, w - c - 1), Counter())[a[r][c]] += 1
    pal = {d: x.most_common(1)[0][0] for d, x in pal.items()}
    return [[pal.get(min(r, c, h - r - 1, w - c - 1), 0) for c in range(w)] for r in range(h)]
