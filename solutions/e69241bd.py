def components(mask, diagonal=False):
    h, w = len(mask), len(mask[0])
    seen = set()
    groups = []
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r in range(h):
        for c in range(w):
            if not mask[r][c] or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            group = []
            while stack:
                y, x = stack.pop()
                group.append((y, x))
                for dy, dx in steps:
                    p = (y + dy, x + dx)
                    if 0 <= p[0] < h and 0 <= p[1] < w and mask[p[0]][p[1]] and p not in seen:
                        seen.add(p)
                        stack.append(p)
            groups.append(group)
    return groups


def solve(grid):
    a = grid
    out = [row[:] for row in a]
    for ps in components([[v != 5 for v in row] for row in a]):
        colors = {a[r][c] for r, c in ps} - {0}
        if len(colors) == 1:
            color = colors.pop()
            for r, c in ps:
                out[r][c] = color
    return out
