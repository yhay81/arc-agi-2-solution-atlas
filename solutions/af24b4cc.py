from collections import Counter


def mode(values):
    return Counter(values).most_common(1)[0][0]


def components(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    result = []
    for r in range(h):
        for c in range(w):
            if not grid[r][c] or (r, c) in seen:
                continue
            seen.add((r, c))
            stack = [(r, c)]
            part = []
            while stack:
                x, y = stack.pop()
                part.append((x, y))
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        p = (x + dx, y + dy)
                        if p not in seen and 0 <= p[0] < h and 0 <= p[1] < w and grid[p[0]][p[1]]:
                            seen.add(p)
                            stack.append(p)
            result.append(part)
    return result


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    objs = components([[v != 0 for v in row] for row in a])
    if not (len(objs) == 6):
        raise ValueError("task assumptions are not satisfied")
    objs = sorted(objs, key=lambda ps: (min(r for r, _ in ps), min(c for _, c in ps)))
    out = [[0] * 5 for _ in range(4)]
    for row in range(2):
        part = sorted(objs[row * 3 : (row + 1) * 3], key=lambda ps: min(c for _, c in ps))
        for col, ps in enumerate(part):
            out[row + 1][col + 1] = mode([a[r][c] for r, c in ps])
    return out
