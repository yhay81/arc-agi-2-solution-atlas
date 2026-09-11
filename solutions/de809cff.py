def solve(grid):
    a = grid
    a = [row[:] for row in a]
    colors = sorted({value for row in a for value in row if value})
    if not (len(colors) == 2):
        raise ValueError("task assumptions are not satisfied")
    other = {colors[0]: colors[1], colors[1]: colors[0]}
    h, w = len(a), len(a[0])
    o = [row[:] for row in a]
    seeds = []
    for y in range(h):
        for x in range(w):
            ns = [
                a[v][u]
                for v, u in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
                if 0 <= v < h and 0 <= u < w
            ]
            if a[y][x] == 0:
                for c in colors:
                    if ns.count(c) >= 3:
                        seeds.append((y, x, c))
    for y, x, c in seeds:
        o[y][x] = 8
    for y, x, c in seeds:
        for v in range(max(0, y - 1), min(h, y + 2)):
            for u in range(max(0, x - 1), min(w, x + 2)):
                if o[v][u] != 8 and a[v][u] in (0, c):
                    o[v][u] = other[c]
    clean = [row[:] for row in a]
    for _ in range(4):
        nxt = [row[:] for row in clean]
        for y in range(h):
            for x in range(w):
                if clean[y][x] == 0:
                    continue
                ns = [
                    clean[v][u]
                    for v, u in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
                    if 0 <= v < h and 0 <= u < w
                ]
                if ns.count(other[clean[y][x]]) >= 3:
                    nxt[y][x] = other[clean[y][x]]
        clean = nxt
    for y in range(h):
        for x in range(w):
            if a[y][x] == 0 or o[y][x] != a[y][x]:
                continue
            ns = [
                a[v][u] if 0 <= v < h and 0 <= u < w else 0
                for v, u in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
            ]
            if clean[y][x] != a[y][x]:
                o[y][x] = clean[y][x]
            elif ns.count(0) >= 3:
                o[y][x] = 0
    return o
