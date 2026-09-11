def components(mask, diagonal=False):
    h, w = len(mask), len(mask[0])
    seen = set()
    result = []
    steps = [
        (dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if diagonal or abs(dr) + abs(dc) == 1
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
                for dr, dc in steps:
                    p = (y + dr, x + dc)
                    if 0 <= p[0] < h and 0 <= p[1] < w and mask[p[0]][p[1]] and p not in seen:
                        seen.add(p)
                        stack.append(p)
            result.append(group)
    return result


def solve(grid):
    a = grid
    out = [row[:] for row in a]
    for color in {v for row in a for v in row if v}:
        mask = [[v == color for v in row] for row in a]
        for group in components(mask):
            if len(group) <= 2:
                for r, c in group:
                    out[r][c] = 3
    return out
