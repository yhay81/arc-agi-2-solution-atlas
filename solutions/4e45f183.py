from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


def bounds(points):
    return (
        min(r for r, c in points),
        min(c for r, c in points),
        max(r for r, c in points),
        max(c for r, c in points),
    )


def components(mask, diagonal=False):
    unseen = {(r, c) for r, row in enumerate(mask) for c, v in enumerate(row) if v}
    groups = []
    offsets = (
        [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr or dc)]
        if diagonal
        else [(-1, 0), (1, 0), (0, -1), (0, 1)]
    )
    while unseen:
        start = unseen.pop()
        group = [start]
        queue = [start]
        for r, c in queue:
            for dr, dc in offsets:
                p = (r + dr, c + dc)
                if p in unseen:
                    unseen.remove(p)
                    queue.append(p)
                    group.append(p)
        groups.append(group)
    return groups


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    objs = components([[v != 0 for v in row] for row in a])
    if not (len(objs) == 9):
        raise ValueError("task assumptions are not satisfied")
    base = mode([v for row in a for v in row if v != 0])
    out = [[0] * len(a[0]) for _ in a]
    positions = []
    for ps in objs:
        r, c, b, d = bounds(ps)
        block = [row[c : d + 1] for row in a[r : b + 1]]
        accent = [(y, x) for y, row in enumerate(block) for x, v in enumerate(row) if v != base]
        y = sum(y for y, x in accent) / len(accent)
        x = sum(x for y, x in accent) / len(accent)
        rr = 0 if y < (len(block) - 1) / 2 else 2 if y > (len(block) - 1) / 2 else 1
        cc = 0 if x < (len(block[0]) - 1) / 2 else 2 if x > (len(block[0]) - 1) / 2 else 1
        positions.append((rr, cc, block))
    hs = len(positions[0][2])
    ws = len(positions[0][2][0])
    for r, c, p in positions:
        for y, row in enumerate(p):
            out[1 + r * (hs + 1) + y][1 + c * (ws + 1) : 1 + c * (ws + 1) + ws] = row
    return out
