def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    unseen = {(r, c) for r in range(h) for c in range(w) if a[r][c] == 6}
    objs = []
    while unseen:
        s = unseen.pop()
        q = [s]
        o = []
        for r, c in q:
            o.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    p = (r + dr, c + dc)
                    if p in unseen:
                        unseen.remove(p)
                        q.append(p)
        objs.append(o)
    marks = [(r, c) for r in range(h) for c in range(w) if a[r][c] not in (0, 6)]
    pieces = []
    for o in objs:
        rs = [r for r, c in o]
        cs = [c for r, c in o]
        r, c, b, d = min(rs), min(cs), max(rs), max(cs)
        center = (sum(rs) / len(rs), sum(cs) / len(cs))
        m = min(marks, key=lambda p: (p[0] - center[0]) ** 2 + (p[1] - center[1]) ** 2)
        patch = [[0] * (d - c + 1) for _ in range(b - r + 1)]
        for rr, cc in o:
            patch[rr - r][cc - c] = a[m[0]][m[1]]
        pieces.append((r, c, patch))
    horizontal = max(c for r, c, p in pieces) - min(c for r, c, p in pieces) > max(
        r for r, c, p in pieces
    ) - min(r for r, c, p in pieces)
    pieces.sort(key=lambda t: t[1] if horizontal else t[0])
    ps = [p for r, c, p in pieces]
    if horizontal:
        hh = max(map(len, ps))
        out = []
        for i in range(hh):
            row = []
            for p in ps:
                row += ([0] * (hh - len(p)) + p)[i]
            out.append(row)
        return out
    ww = max(len(p[0]) for p in ps)
    out = []
    for p in ps:
        out += [row + [0] * (ww - len(row)) for row in p]
    return out
