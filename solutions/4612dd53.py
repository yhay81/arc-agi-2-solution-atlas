from itertools import combinations


def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    out = [r[:] for r in a]
    for t, b in combinations(range(h), 2):
        for l, r in combinations(range(w), 2):
            if b - t < 2 or r - l < 2:
                continue
            sides = [
                [a[t][c] for c in range(l, r + 1)],
                [a[b][c] for c in range(l, r + 1)],
                [a[y][l] for y in range(t, b + 1)],
                [a[y][r] for y in range(t, b + 1)],
            ]
            if (
                sum(a[y][x] == 1 for y, x in ((t, l), (t, r), (b, l), (b, r))) < 3
                or min(sum(v == 1 for v in s) for s in sides) < 3
                or min(sum(v == 1 for v in s) / len(s) for s in sides) < 0.5
            ):
                continue
            for c in range(l, r + 1):
                if a[t][c] == 0:
                    out[t][c] = 2
                if a[b][c] == 0:
                    out[b][c] = 2
            for y in range(t, b + 1):
                if a[y][l] == 0:
                    out[y][l] = 2
                if a[y][r] == 0:
                    out[y][r] = 2
    return out
