from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


def weave(a):
    h, w = len(a), len(a[0])
    hr = max(range(h), key=lambda r: sum(v != 0 for v in a[r]))
    vc = max(range(w), key=lambda c: sum(a[r][c] != 0 for r in range(h)))
    vs = [a[r][vc] for r in range(h)]
    hs = a[hr]
    vb = mode([v for v in vs if v])
    hb = mode([v for v in hs if v])
    vp = [r for r in range(h) if vs[r] not in (0, vb) and r != hr]
    hp = [c for c in range(w) if hs[c] not in (0, hb) and c != vc]
    top, bottom = min(vp + [hr]), max(vp + [hr])
    left, right = min(hp), max(hp)
    vm, hm = vs[vp[0]], hs[hp[0]]
    out = [[0] * w for _ in range(h)]
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            if (r - top) % 2 == 0:
                out[r][c] = (vm if min(vp) <= r <= max(vp) else hm) if (c - left) % 2 == 0 else vb
            else:
                out[r][c] = hb if (c - left) % 2 == 0 else a[hr][vc]
    return out


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = weave(a)
    h, w = len(a), len(a[0])
    hr = max(range(h), key=lambda r: sum(v != 0 for v in a[r]))
    vc = max(range(w), key=lambda c: sum(a[r][c] != 0 for r in range(h)))
    vs = [a[r][vc] for r in range(h)]
    hs = a[hr]
    vb, hb = mode([v for v in vs if v]), mode([v for v in hs if v])
    vp = [r for r in range(h) if vs[r] not in (0, vb) and r != hr]
    hp = [c for c in range(w) if hs[c] not in (0, hb) and c != vc]
    near = min(vp, key=lambda r: abs(r - hr))
    if abs(near - hr) % 2 == 0:
        for c in range(min(hp) + 1, max(hp) + 1, 2):
            out[near][c] = a[hr][vc]
    return out
