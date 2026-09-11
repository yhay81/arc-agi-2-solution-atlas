def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    rect = []
    for color in {v for r in a for v in r if v}:
        rem = {(r, c) for r in range(h) for c in range(w) if a[r][c] == color}
        while rem:
            s = rem.pop()
            comp = {s}
            q = [s]
            while q:
                r, c = q.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    p = (r + dr, c + dc)
                    if p in rem:
                        rem.remove(p)
                        comp.add(p)
                        q.append(p)
            if len(comp) < 9:
                continue
            y, x = min(r for r, _ in comp), min(c for _, c in comp)
            v, u = max(r for r, _ in comp), max(c for _, c in comp)
            if min(v - y + 1, u - x + 1) < 3 or not any(
                all((r + i, c + j) in comp for i in range(3) for j in range(3))
                for r in range(y, v - 1)
                for c in range(x, u - 1)
            ):
                continue
            rect.append((y, x, v, u, color))

    def group(axis):
        ints = sorted((z[axis], z[axis + 2], i) for i, z in enumerate(rect))
        gs = []
        for lo, hi, i in ints:
            if gs and lo <= gs[-1][0]:
                gs[-1][0] = max(gs[-1][0], hi)
                gs[-1][1].append(i)
            else:
                gs.append([hi, [i]])
        return {i: g for g, (_, ids) in enumerate(gs) for i in ids}, len(gs)

    rows, hh = group(0)
    cols, ww = group(1)
    out = [[-1] * ww for _ in range(hh)]
    for i, z in enumerate(rect):
        out[rows[i]][cols[i]] = z[-1]
    return out
