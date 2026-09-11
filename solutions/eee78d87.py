def solve(grid):
    a = grid
    points = [(r, c) for r, row in enumerate(a) for c, value in enumerate(row) if value != 7]
    top = min(r for r, _ in points)
    left = min(c for _, c in points)
    bottom = max(r for r, _ in points)
    right = max(c for _, c in points)
    mask = [row[left : right + 1] for row in a[top : bottom + 1]]
    output = [[7] * 16 for _ in range(16)]
    for r in range(16):
        for c in range(16):
            if mask[(r - 5) % 3][(c - 5) % 3] != 7:
                output[r][c] = 9 if 5 <= r < 11 and 5 <= c < 11 else 0
    return output
