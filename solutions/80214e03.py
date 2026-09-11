from collections import Counter


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    pts = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v]
    r0 = min((r for r, c in pts))
    r1 = max((r for r, c in pts))
    c0 = min((c for r, c in pts))
    c1 = max((c for r, c in pts))
    rs = (
        [r0]
        + [
            r
            for r in range(r0 + 1, r1 + 1)
            if any(a[r][c] != a[r - 1][c] and a[r][c] and a[r - 1][c] for c in range(c0, c1 + 1))
        ]
        + [r1 + 1]
    )
    cs = (
        [c0]
        + [
            c
            for c in range(c0 + 1, c1 + 1)
            if any(a[r][c] != a[r][c - 1] and a[r][c] and a[r][c - 1] for r in range(r0, r1 + 1))
        ]
        + [c1 + 1]
    )
    out = []
    for ar, br in zip(rs, rs[1:]):
        row = []
        for ac, bc in zip(cs, cs[1:]):
            row.append(
                Counter(
                    a[r][c] for r in range(ar, br) for c in range(ac, bc) if a[r][c]
                ).most_common(1)[0][0]
            )
        out.append(row[::-1])
    return out
