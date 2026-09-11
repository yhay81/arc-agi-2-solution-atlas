from collections import Counter


def solve(grid):
    a = grid
    a = [r[:] for r in a]
    h, w = len(a), len(a[0])
    bg = Counter(v for r in a for v in r).most_common(1)[0][0]
    seen = set()
    shapes = []
    for color in {v for r in a for v in r if v != bg}:
        for r in range(h):
            for c in range(w):
                if a[r][c] != color or (r, c) in seen:
                    continue
                q = [(r, c)]
                seen.add((r, c))
                p = []
                for y, x in q:
                    p.append((y, x))
                    for dy, dx in [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j]:
                        z = (y + dy, x + dx)
                        if (
                            0 <= z[0] < h
                            and 0 <= z[1] < w
                            and a[z[0]][z[1]] == color
                            and z not in seen
                        ):
                            seen.add(z)
                            q.append(z)
                top, left = min(y for y, x in p), min(x for y, x in p)
                bot, right = max(y for y, x in p), max(x for y, x in p)
                mask = {(y - top, x - left) for y, x in p}
                variants = set()
                for flip in (0, 1):
                    for k in range(4):
                        m = mask
                        variants.add(tuple(sorted(m)))
                        mask = {(x, bot - top - y) for y, x in m}
                    mask = {(y, right - left - x) for y, x in mask}
                shapes.append((color, p, top, bot, variants))
    out = [[bg] * w for _ in range(h)]
    for i, (color, p, top, bot, var) in enumerate(shapes):
        paired = any(i != j and var & z[4] for j, z in enumerate(shapes))
        shift = -top if paired else h - 1 - bot
        for y, x in p:
            if 0 <= y + shift < h:
                out[y + shift][x] = color
    return out
