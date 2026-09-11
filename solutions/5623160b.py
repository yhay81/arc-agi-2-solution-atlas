def solve(grid):
    a = grid
    a = [r[:] for r in a]
    h, w = len(a), len(a[0])
    out = [r[:] for r in a]
    payload = []
    for color in {v for row in a for v in row if v not in (7, 9)}:
        unseen = {(r, c) for r in range(h) for c in range(w) if a[r][c] == color}
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
            dirs = []
            for r, c in o:
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if 0 <= r + dr < h and 0 <= c + dc < w and a[r + dr][c + dc] == 9:
                        dirs.append((-dr, -dc))
            if not (len(set(dirs)) == 1):
                raise ValueError("task assumptions are not satisfied")
            dr, dc = dirs[0]
            rs = [r for r, c in o]
            cs = [c for r, c in o]
            r, b = min(rs), max(rs)
            c, d = min(cs), max(cs)
            steps = r if dr < 0 else h - 1 - b if dr > 0 else c if dc < 0 else w - 1 - d
            payload.append((o, [(rr + dr * steps, cc + dc * steps) for rr, cc in o]))
            for rr, cc in o:
                out[rr][cc] = 7
    for src, dst in payload:
        for (r, c), (rr, cc) in zip(src, dst):
            out[rr][cc] = a[r][c]
    return out
