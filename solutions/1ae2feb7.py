def solve(grid):
    a = grid
    a = [row[:] for row in a]
    h, w = len(a), len(a[0])
    walls = [
        x
        for x in range(w)
        if len(set(row[x] for row in a) - {0}) == 1 and sum(row[x] != 0 for row in a) >= h * 0.7
    ]
    if not (len(walls) == 1):
        raise ValueError("task assumptions are not satisfied")
    x = walls[0]
    flip = sum(v != 0 for row in a for v in row[:x]) < sum(
        v != 0 for row in a for v in row[x + 1 :]
    )
    z = [row[::-1] for row in a] if flip else [row[:] for row in a]
    x = w - 1 - x if flip else x
    o = [row[:] for row in z]
    for r in range(h):
        segments = []
        i = 0
        while i < x:
            c = z[r][i]
            j = i + 1
            while j < x and z[r][j] == c:
                j += 1
            if c != 0:
                segments.append((c, j - i))
            i = j
        for c, n in reversed(segments):
            for j in range(x + 1, w, n):
                if o[r][j] == 0:
                    o[r][j] = c
    return [row[::-1] for row in o] if flip else o
