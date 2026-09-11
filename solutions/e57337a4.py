from collections import Counter


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    n = 3
    h, w = (len(g) // n, len(g[0]) // n)
    back = bg(g)
    return [
        [
            0
            if any(
                g[r][c] == 0 for r in range(a * h, (a + 1) * h) for c in range(b * w, (b + 1) * w)
            )
            else back
            for b in range(n)
        ]
        for a in range(n)
    ]
