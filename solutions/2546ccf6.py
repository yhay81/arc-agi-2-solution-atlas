def runs(ids):
    out = []
    for n in ids:
        if not out or n != out[-1][-1] + 1:
            out.append([])
        out[-1].append(n)
    return out


def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    sep = next(
        c
        for c in {v for r in a for v in r if v}
        if any(all(a[r][x] == c for x in range(w)) for r in range(h))
        and any(all(a[x][j] == c for x in range(h)) for j in range(w))
    )
    rs = runs([r for r in range(h) if not all(v == sep for v in a[r])])
    cs = runs([c for c in range(w) if not all(a[r][c] == sep for r in range(h))])
    parts = [[[a[r][c] for c in cc] for r in rr] for rr in rs for cc in cs]
    out = [r[:] for r in a]

    def part(i, j):
        return parts[i * len(cs) + j]

    for i in range(len(rs) - 1):
        for j in range(len(cs) - 1):
            group = [(y, x, part(i + y, j + x)) for y in (0, 1) for x in (0, 1)]
            for color in {v for r in a for v in r if v not in (0, sep)}:
                if sum(any(color in row for row in p) for _, _, p in group) != 3:
                    continue
                for y, x, p in group:
                    if any(v for row in p for v in row):
                        continue
                    mate = part(i + y, j + 1 - x)
                    other = part(i + 1 - y, j + x)
                    one = [row[::-1] for row in mate]
                    two = other[::-1]
                    if one != two:
                        continue
                    for r, rr in enumerate(rs[i + y]):
                        for c, cc in enumerate(cs[j + x]):
                            out[rr][cc] = one[r][c]
    return out
