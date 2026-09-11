from collections import Counter


def cp(g):
    return [row[:] for row in g]


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    base = bg(g)
    blocks = []
    for r in range(h - 4):
        for c in range(w - 4):
            color = g[r][c]
            if color not in (2, 8):
                continue
            if (
                all(
                    g[r + dr][c + dc] == color
                    for dr in range(5)
                    for dc in range(5)
                    if dr in (0, 4) or dc in (0, 4)
                )
                and len({g[r + dr][c + dc] for dr in range(1, 4) for dc in range(1, 4)}) == 1
            ):
                blocks.append((r, c, color, [row[c : c + 5] for row in g[r : r + 5]]))
    out = cp(g)
    for r, c, _, p in blocks:
        for dr in range(5):
            for dc in range(5):
                out[r + dr][c + dc] = base
    for color in (8, 2):
        occupied = set()
        for r, c, _, p in sorted(
            [b for b in blocks if b[2] == color], key=lambda b: b[1], reverse=color == 2
        ):
            step = -1 if color == 8 else 1
            while (
                c + step >= 0
                and c + step + 4 < w
                and (
                    not any(
                        (r + dr, c + step + dc) in occupied for dr in range(5) for dc in range(5)
                    )
                )
            ):
                c += step
            for dr in range(5):
                for dc in range(5):
                    out[r + dr][c + dc] = p[dr][dc]
                    occupied.add((r + dr, c + dc))
    return out
