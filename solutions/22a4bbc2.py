def components(mask, diagonal=False):
    h, w = len(mask), len(mask[0])
    seen = set()
    groups = []
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
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    p = (y + dy, x + dx)
                    if 0 <= p[0] < h and 0 <= p[1] < w and mask[p[0]][p[1]] and p not in seen:
                        seen.add(p)
                        stack.append(p)
            groups.append(group)
    return groups


def solve(grid):
    a = grid
    out = [row[:] for row in a]
    groups = []
    for color in {v for row in a for v in row if v}:
        groups.extend(components([[v == color for v in row] for row in a]))
    for i, ps in enumerate(
        sorted(groups, key=lambda p: (min(y for y, x in p), min(x for y, x in p)))
    ):
        if i % 3 == 0:
            for r, c in ps:
                out[r][c] = 2
    return out
