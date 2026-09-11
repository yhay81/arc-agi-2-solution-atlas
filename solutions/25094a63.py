def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = copy(g)
    candidates = []
    h, w = (len(g), len(g[0]))
    for col in {v for row in g for v in row}:
        for top in range(h):
            valid = [True] * w
            for bottom in range(top, h):
                valid = [a and g[bottom][c] == col for c, a in enumerate(valid)]
                if bottom - top < 2:
                    continue
                c = 0
                while c < w:
                    if not valid[c]:
                        c += 1
                        continue
                    end = c + 1
                    while end < w and valid[end]:
                        end += 1
                    if end - c >= 3:
                        candidates.append(((bottom - top + 1) * (end - c), top, c, bottom, end))
                    c = end
    used = set()
    for area, top, left, bottom, right in sorted(candidates, reverse=True):
        cells = {(r, c) for r in range(top, bottom + 1) for c in range(left, right)}
        if cells & used:
            continue
        used |= cells
        for r, c in cells:
            out[r][c] = 4
    return out
