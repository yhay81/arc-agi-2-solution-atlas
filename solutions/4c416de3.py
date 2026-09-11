from collections import Counter, deque


def components(grid: list[list[bool]], diagonal: bool) -> list[list[tuple[int, int]]]:
    height, width = len(grid), len(grid[0])
    steps = [
        (dr, dc)
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr or dc) and (diagonal or not (dr and dc))
    ]
    seen = set()
    result = []
    for row in range(height):
        for col in range(width):
            if not grid[row][col] or (row, col) in seen:
                continue
            seen.add((row, col))
            queue = deque([(row, col)])
            part = []
            while queue:
                r, c = queue.popleft()
                part.append((r, c))
                for dr, dc in steps:
                    rr, cc = r + dr, c + dc
                    if (
                        0 <= rr < height
                        and 0 <= cc < width
                        and grid[rr][cc]
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        queue.append((rr, cc))
            result.append(part)
    return result


def solve(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(cell for row in grid for cell in row).most_common(1)[0][0]
    parts = [
        (color, part)
        for color in set(cell for row in grid for cell in row) - {0, background}
        for part in components([[cell == color for cell in row] for row in grid], True)
    ]
    corners = []
    for zero in components([[cell == 0 for cell in row] for row in grid], False):
        top, bottom = min(row for row, _ in zero), max(row for row, _ in zero)
        left, right = min(col for _, col in zero), max(col for _, col in zero)
        if bottom - top < 2 or right - left < 2:
            continue
        corners.extend(
            ((top, left, -1, -1), (top, right, -1, 1), (bottom, left, 1, -1), (bottom, right, 1, 1))
        )
    templates = []
    for color, part in parts:
        if len(part) <= 1:
            continue
        for row, col, row_direction, col_direction in corners:
            if (row, col) in part:
                templates.append(
                    [((r - row) * row_direction, (c - col) * col_direction) for r, c in part]
                )
    if not templates:
        for color, part in parts:
            top, bottom = min(row for row, _ in part), max(row for row, _ in part)
            left, right = min(col for _, col in part), max(col for _, col in part)
            if bottom - top == 2 and right - left == 2:
                middle = (top + 1, left + 1)
                col_direction = -1 if grid[top][left] == color else 1
                templates.append(
                    [((r - middle[0]) * -1, (c - middle[1]) * col_direction) for r, c in part]
                )
    if not (templates):
        raise ValueError("task assumptions are not satisfied")
    template = templates[0]
    output = [row[:] for row in grid]
    for color, part in parts:
        if len(part) != 1:
            continue
        point = part[0]
        options = []
        for row, col, row_direction, col_direction in corners:
            delta = (
                (point[0] - row) * row_direction,
                (point[1] - col) * col_direction,
            )
            if delta[0] < 0 and delta[1] < 0 and delta in template:
                options.append(
                    (abs(delta[0]) + abs(delta[1]), row, col, row_direction, col_direction)
                )
        if not options:
            continue
        _, row, col, row_direction, col_direction = min(options)
        for dr, dc in template:
            rr = row + dr * row_direction
            cc = col + dc * col_direction
            if 0 <= rr < height and 0 <= cc < width:
                output[rr][cc] = color
    return output
