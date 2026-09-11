def solve(grid):
    a = grid
    symbols = []
    for tr in range(3):
        for tc in range(3):
            values = [
                a[r][c]
                for r in range(tr * 4, tr * 4 + 3)
                for c in range(tc * 4, tc * 4 + 3)
                if a[r][c] not in (7, 6)
            ]
            if values:
                symbols.append((tr, tc, values[0]))
    if any(value != 2 for _, _, value in symbols):
        return [[7] * 16 for _ in range(16)]
    (r1, c1, _), (r2, c2, _) = symbols
    if c1 == c2:
        r, c = min(r1, r2) - 1, c1
        extras = [(r, c - 1, 5), (r, c + 1, 8)]
    elif r1 == r2:
        r, c = r1, min(c1, c2) - 1
        extras = [(r - 1, c, 8), (r + 1, c, 5)]
    elif c2 < c1:
        extras = [(r2, c2 - 1, 8), (r2 + 1, c2, 5)]
    else:
        extras = [(r2, c2 + 1, 8), (r2 + 1, c2, 5)]
    lookup = {
        (r, c): v
        for r, c, v in symbols + [(r, c, v) for r, c, v in extras if 0 <= r < 3 and 0 <= c < 3]
    }
    out = [[7] * 11 for _ in range(11)]
    for i in (3, 7):
        for j in range(11):
            out[i][j] = out[j][i] = 6
    for r in range(11):
        for c in range(11):
            if r in (3, 7) or c in (3, 7):
                continue
            v = lookup.get((r // 4, c // 4), 0)
            if v and ((r % 4 == 1 and c % 4 in (0, 2)) or (c % 4 == 1 and r % 4 in (0, 2))):
                out[r][c] = v
    return out
