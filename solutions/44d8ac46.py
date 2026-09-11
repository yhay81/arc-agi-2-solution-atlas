def solve(grid):
    a = [r[:] for r in grid]
    h, w = len(a), len(a[0])
    source = [r[:] for r in a]
    for side in range(min(h, w), 2, -1):
        for top in range(h - side + 1):
            for left in range(w - side + 1):
                bot, right = top + side - 1, left + side - 1
                edge = (
                    [a[top][c] for c in range(left, right + 1)]
                    + [a[bot][c] for c in range(left, right + 1)]
                    + [a[r][left] for r in range(top + 1, bot)]
                    + [a[r][right] for r in range(top + 1, bot)]
                )
                if not all(v == 5 for v in edge):
                    continue
                cells = [(r, c) for r in range(top + 1, bot) for c in range(left + 1, right)]
                if not any(a[r][c] == 0 for r, c in cells):
                    continue
                guide = [(r, c) for r, c in cells if a[r][c] == 5]
                if guide:
                    sides = [
                        all(a[top + 1][c] == 5 for c in range(left + 1, right)),
                        all(a[r][right - 1] == 5 for r in range(top + 1, bot)),
                        all(a[bot - 1][c] == 5 for c in range(left + 1, right)),
                        all(a[r][left + 1] == 5 for r in range(top + 1, bot)),
                    ]
                    if sum(sides) != 2 or not any(
                        sides[i] and sides[(i + 1) % 4] for i in range(4)
                    ):
                        continue
                for r, c in cells:
                    if a[r][c] == 0:
                        a[r][c] = 1
    return [[0 if v == 0 else 5 if v == 5 else 2 if v == 1 else v for v in row] for row in a]
