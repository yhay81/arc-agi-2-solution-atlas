from collections import Counter, deque


def solve(grid):
    height, width = len(grid), len(grid[0])
    visited = [[False] * width for _ in range(height)]
    best_interior = best_any = None
    for r in range(height):
        for c in range(width):
            if visited[r][c]:
                continue
            color = grid[r][c]
            queue = deque([(r, c)])
            visited[r][c] = True
            cells = []
            touches_border = False
            while queue:
                row, col = queue.popleft()
                cells.append((row, col))
                touches_border |= row in (0, height - 1) or col in (0, width - 1)
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = row + dr, col + dc
                    if (
                        0 <= nr < height
                        and 0 <= nc < width
                        and not visited[nr][nc]
                        and grid[nr][nc] == color
                    ):
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            component = color, cells, touches_border
            if best_any is None or len(cells) > len(best_any[1]):
                best_any = component
            if not touches_border and (best_interior is None or len(cells) > len(best_interior[1])):
                best_interior = component

    color, cells, _ = best_interior or best_any
    rows = [r for r, _ in cells]
    cols = [c for _, c in cells]
    top, bottom = min(rows), max(rows)
    left, right = min(cols), max(cols)
    crop = [row[left : right + 1] for row in grid[top : bottom + 1]]

    padded = [[0] * (width + 2)]
    padded += [[0, *row, 0] for row in grid]
    padded.append([0] * (width + 2))
    pad = [row[left : right + 3] for row in padded[top : bottom + 3]]
    outer = [
        Counter(grid[0]).most_common(1)[0][0],
        Counter(row[-1] for row in grid).most_common(1)[0][0],
        Counter(grid[-1]).most_common(1)[0][0],
        Counter(row[0] for row in grid).most_common(1)[0][0],
    ]
    candidates = []
    for flip in (False, True):
        rotated = [row[::-1] for row in pad] if flip else pad
        for _ in range(4):
            sides = [
                rotated[0][1:-1],
                [row[-1] for row in rotated[1:-1]],
                rotated[-1][1:-1],
                [row[0] for row in rotated[1:-1]],
            ]
            valid = True
            score = 0
            for index, edge in enumerate(sides):
                if len(set(edge)) == 1 and edge[0] not in (0, 5, color):
                    score += 1
                    valid &= edge[0] == outer[index]
            if valid and score >= 2:
                candidates.append([row[1:-1] for row in rotated[1:-1]])
            rotated = [list(row) for row in zip(*rotated)][::-1]
    if not (candidates and all(candidate == candidates[0] for candidate in candidates)):
        raise ValueError("task assumptions are not satisfied")
    return candidates[0]
