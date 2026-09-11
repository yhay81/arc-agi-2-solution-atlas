from collections import Counter


def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    bg = Counter(v for r in a for v in r).most_common(1)[0][0]
    line = next(
        c
        for c in {v for r in a for v in r if v != bg}
        if any(all(a[r][j] == c for j in range(w)) for r in range(h))
        or any(all(a[i][j] == c for i in range(h)) for j in range(w))
    )
    rows = [r for r in range(h) if all(v == line for v in a[r])]
    if rows:
        t = [list(x) for x in zip(*a)]
        return [list(x) for x in zip(*solve(t))]
    axis = next(j for j in range(w) if all(a[i][j] == line for i in range(h)))
    out = [r[:] for r in a]
    for color in {v for r in a for v in r if v not in (bg, line)}:
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
            rs = [r for r, _ in comp]
            cs = [c for _, c in comp]
            top, bottom = min(rs), max(rs)
            left, right = min(cs), max(cs)
            if len(comp) < 4 or len(comp) != (bottom - top + 1) * (right - left + 1):
                continue
            ref = [(r, 2 * axis - c) for r, c in comp]
            for r, c in ref:
                if 0 <= r < h and 0 <= c < w:
                    out[r][c] = color
            for r in range(top, bottom + 1):
                for c in range(min(left, 2 * axis - right), max(right, 2 * axis - left) + 1):
                    out[r][c] = line
            for r, c in comp | set(ref):
                if 0 <= r < h and 0 <= c < w:
                    out[r][c] = color
    return out
