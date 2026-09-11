def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = copy(g)
    for r, row in enumerate(g):
        segs = []
        start = 0
        for c in range(1, len(row) + 1):
            if c == len(row) or (row[c] != 2 and row[start] != 2 and (row[c] != row[start])):
                segs.append((start, c))
                start = c
        clean = [
            v
            if v != 2
            else next(
                (
                    row[x]
                    for d in range(1, len(row))
                    for x in (c - d, c + d)
                    if 0 <= x < len(row) and row[x] != 2
                ),
                8,
            )
            for c, v in enumerate(row)
        ]
        start = 0
        for c in range(1, len(row) + 1):
            if c == len(row) or clean[c] != clean[start]:
                color = clean[start]
                n = sum(v == 2 for v in row[start:c])
                out[r][start:c] = [color] * (c - start)
                for x in range(start, start + n) if color == 8 else range(c - n, c):
                    out[r][x] = 2
                start = c
    return out
