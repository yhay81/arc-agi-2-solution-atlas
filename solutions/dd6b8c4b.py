from collections import deque

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solve(grid):
    a = grid
    order = 0
    a = [row[:] for row in a]
    center = next((y, x) for y, row in enumerate(a) for x, v in enumerate(row) if v == 2)
    r, c = center
    slots = [(y, x) for y in range(r - 1, r + 2) for x in range(c - 1, c + 2)]
    todo = deque(slots)
    seen = set(slots)
    taken = []
    dirs = [D, D[::-1], [(0, 1), (1, 0), (0, -1), (-1, 0)]][order]
    while todo and len(taken) < 9:
        y, x = todo.popleft()
        for dy, dx in dirs:
            p = yy, xx = (y + dy, x + dx)
            if not (0 <= yy < len(a) and 0 <= xx < len(a[0])) or p in seen or a[yy][xx] == 6:
                continue
            seen.add(p)
            todo.append(p)
            if a[yy][xx] == 9:
                taken.append(p)
            if len(taken) == 9:
                break
    out = [row[:] for row in a]
    for p in taken:
        out[p[0]][p[1]] = 7
    for p in slots[: len(taken)]:
        out[p[0]][p[1]] = 9
    return out
