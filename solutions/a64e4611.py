def rotate(grid):
    return [list(row) for row in zip(*grid[::-1])]


def trim_dead_ends(grid):
    remove = []
    for row in range(2, len(grid) - 1):
        col = 1
        while col < len(grid[0]) - 1:
            if grid[row][col] != 3:
                col += 1
                continue
            end = col
            while end + 1 < len(grid[0]) - 1 and grid[row][end + 1] == 3:
                end += 1
            if (
                end - col < 3
                and grid[row][col - 1] == 0
                and grid[row][end + 1] == 0
                and all(grid[row - 1][c] == 0 for c in range(col, end + 1))
            ):
                remove.extend((row, c) for c in range(col, end + 1))
            col = end + 1
    for row, col in remove:
        grid[row][col] = 0


def solve(grid):
    a = grid
    min_run = 12
    height, width = len(a), len(a[0])
    pad = [[0] * (width + 2) for _ in range(height + 2)]
    for r, row in enumerate(a, 1):
        pad[r][1:-1] = [int(value) for value in row]
    safe = [[False] * (width + 2) for _ in range(height + 2)]
    for r in range(1, height + 1):
        for c in range(1, width + 1):
            safe[r][c] = all(
                pad[rr][cc] == 0 for rr in range(r - 1, r + 2) for cc in range(c - 1, c + 2)
            )
    paint = [[False] * (width + 2) for _ in range(height + 2)]
    for axis in (0, 1):
        rows, cols = (len(safe), len(safe[0])) if axis == 0 else (len(safe[0]), len(safe))
        for r in range(rows):
            indices = []
            for c in range(cols):
                value = safe[r][c] if axis == 0 else safe[c][r]
                if value:
                    if indices and c == indices[-1] + 1:
                        indices.append(c)
                    else:
                        indices = [c]
                    continue
                if len(indices) >= min_run:
                    for q in indices:
                        if axis == 0:
                            paint[r][q] = True
                        else:
                            paint[q][r] = True
                indices = []
            if len(indices) >= min_run:
                for q in indices:
                    if axis == 0:
                        paint[r][q] = True
                    else:
                        paint[q][r] = True
    for r in range(len(pad)):
        for c in range(len(pad[0])):
            if paint[r][c]:
                pad[r][c] = 3
    while True:
        old = [row[:] for row in pad]
        for _ in range(4):
            trim_dead_ends(pad)
            pad = rotate(pad)
        if old == pad:
            break
    return [row[1:-1] for row in pad[1:-1]]
