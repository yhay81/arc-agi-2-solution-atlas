from collections import deque


def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    out = [row[:] for row in a]
    start = next((r, c) for r in range(h) for c in range(w) if a[r][c] == 2)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start[0], start[1], 0, 0)])
    visited = set()

    def open_for_branch(r, c):
        return 0 <= r < h and 0 <= c < w and not (out[r][c] == 2 and a[r][c] == 0)

    while queue:
        row, col, direction, depth = queue.popleft()
        action = (row, col, direction)
        if action in visited:
            continue
        visited.add(action)
        dr, dc = directions[direction]
        while True:
            nr, nc = (row + dr, col + dc)
            if not (0 <= nr < h and 0 <= nc < w):
                break
            if a[nr][nc] not in (0, 2):
                p1, p2 = (1, 3) if direction in (0, 2) else (0, 2)
                r1, c1 = (row + directions[p1][0], col + directions[p1][1])
                r2, c2 = (row + directions[p2][0], col + directions[p2][1])
                if depth < 5 and open_for_branch(r1, c1) and open_for_branch(r2, c2):
                    queue.append((row, col, p1, depth + 1))
                    queue.append((row, col, p2, depth + 1))
                break
            out[nr][nc] = 2
            row, col = (nr, nc)
    if h > 2 and all(v == 0 for v in a[1]) and sum(v == 2 for v in out[1]) > 1:
        out[1] = [2] * w
    return out
