def components(mask, diagonal=False):
    h, w = len(mask), len(mask[0])
    seen = set()
    groups = []
    steps = [
        (dy, dx) for dy in (-1, 0, 1) for dx in (-1, 0, 1) if diagonal or abs(dy) + abs(dx) == 1
    ]
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
    cols = [5, 2, 8, 9, 6]
    counts = [len(components([[v == c for v in row] for row in a], True)) for c in cols]
    out = [[7] * 5 for _ in range(max(counts))]
    for x, (color, n) in enumerate(zip(cols, counts)):
        if n:
            for row in out[-n:]:
                row[x] = color
    return out
