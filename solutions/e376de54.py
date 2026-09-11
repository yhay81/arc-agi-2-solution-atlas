from collections import Counter, defaultdict


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    back = bg(g)
    ps = [(r, c, v) for r, row in enumerate(g) for c, v in enumerate(row) if v != back]
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    dr, dc = max(
        directions,
        key=lambda d: sum(
            (
                0 <= r + d[0] < len(g)
                and 0 <= c + d[1] < len(g[0])
                and (g[r + d[0]][c + d[1]] == v)
                for r, c, v in ps
            )
        ),
    )
    lines = defaultdict(list)
    for r, c, v in ps:
        lines[r * dc - c * dr].append((r, c, v))
    keys = sorted(lines)
    base = keys[len(keys) // 2]
    coords = lines[base]
    out = [[back] * len(g[0]) for _ in g]
    for key, cells in lines.items():
        color = Counter((v for r, c, v in cells)).most_common(1)[0][0]
        delta = key - base
        norm = dr * dr + dc * dc
        for r, c, v in coords:
            rr = r + delta * dc // norm
            cc = c - delta * dr // norm
            if 0 <= rr < len(g) and 0 <= cc < len(g[0]):
                out[rr][cc] = color
    return out
