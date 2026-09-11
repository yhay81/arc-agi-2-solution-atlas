from collections import Counter


def solve(grid):
    source = grid
    h, w = len(source), len(source[0])
    if h < 3 or w < 3:
        return [r[:] for r in source]
    sides = [
        source[0][1:-1],
        source[-1][1:-1],
        [source[r][0] for r in range(1, h - 1)],
        [source[r][-1] for r in range(1, h - 1)],
    ]
    if any(not s or 0 in s for s in sides):
        return [r[:] for r in source]
    colors = [Counter(s).most_common(1)[0][0] for s in sides]
    if len(set(colors)) != 4:
        return [r[:] for r in source]
    out = [r[:] for r in source]
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            out[r][c] = 0
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            v = source[r][c]
            if v == colors[0]:
                out[1][c] = v
            elif v == colors[1]:
                out[-2][c] = v
            elif v == colors[2]:
                out[r][1] = v
            elif v == colors[3]:
                out[r][-2] = v
    return out
