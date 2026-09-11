from collections import Counter


def mode(values):
    flat = [v for row in values for v in row] if values and isinstance(values[0], list) else values
    return Counter(flat).most_common(1)[0][0]


def components(mask, diagonal=False):
    unseen = {(r, c) for r, row in enumerate(mask) for c, v in enumerate(row) if v}
    out = []
    offsets = [
        (dr, dc)
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr or dc) and (diagonal or not (dr and dc))
    ]
    while unseen:
        p = min(unseen)
        unseen.remove(p)
        q = [p]
        cells = []
        while q:
            r, c = q.pop()
            cells.append((r, c))
            for dr, dc in offsets:
                n = (r + dr, c + dc)
                if n in unseen:
                    unseen.remove(n)
                    q.append(n)
        out.append(cells)
    return out


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    inner = [row[1:-1] for row in a[1:-1]]
    bg = mode(inner)
    directions = {
        mode([a[0][1:-1]]): (-1, 0),
        mode([a[-1][1:-1]]): (1, 0),
        mode([[row[0] for row in a[1:-1]]]): (0, -1),
        mode([[row[-1] for row in a[1:-1]]]): (0, 1),
    }
    for r in range(1, len(a) - 1):
        for c in range(1, len(a[0]) - 1):
            out[r][c] = bg
    for color in {v for row in inner for v in row} - {bg}:
        for ps in components([[v == color for v in row] for row in inner], True):
            ps = [(r + 1, c + 1) for r, c in ps]
            dr, dc = directions.get(color, (0, 0))
            dst = [(r + dr, c + dc) for r, c in ps]
            if any(r < 1 or r >= len(a) - 1 or c < 1 or c >= len(a[0]) - 1 for r, c in dst):
                dst = ps
            for r, c in dst:
                out[r][c] = color
    return out
