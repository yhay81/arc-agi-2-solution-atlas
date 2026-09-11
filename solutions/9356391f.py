def solve(grid):
    a = grid
    out = [row[:] for row in a]
    r, c = next((r, c) for r, row in enumerate(a[2:], 2) for c, v in enumerate(row) if v)
    end = max(i for i, v in enumerate(a[0]) if v)
    palette = a[0][: end + 1]
    for k, color in enumerate(palette):
        for y in range(2, len(a)):
            for x in range(len(a[0])):
                if max(abs(y - r), abs(x - c)) == k:
                    out[y][x] = color
        if r - k < 2 or r + k >= len(a) or c - k < 0 or c + k >= len(a[0]):
            out[0][k] = 5
    return out
