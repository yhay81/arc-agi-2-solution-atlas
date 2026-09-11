def bounds(points):
    rows, cols = zip(*points)
    return min(rows), min(cols), max(rows), max(cols)


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    h, w = len(a), len(a[0])
    out = [[value if value in (7, 4) else 7 for value in row] for row in a]
    line = [r for r in range(h) if all(value == 4 for value in a[r])][0]
    dy = -(line + 1)
    pointer = [(r, c) for r in range(h) for c in range(w) if a[r][c] == 6]
    anchor = min(pointer, key=lambda point: point[1])
    body = [(r, c) for r in range(h) for c in range(w) if a[r][c] not in (7, 4, 6)]
    r0, c0, r1, c1 = bounds(body)
    for r, c in pointer:
        out[r + dy][c] = 6
    for r, c in body:
        out[r + anchor[0] - r1 + dy][c + anchor[1] - c1] = a[r][c]
    return out
