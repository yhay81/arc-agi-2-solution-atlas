from collections import Counter


def _components(points: set[tuple[int, int]]) -> list[list[tuple[int, int]]]:
    groups = []
    while points:
        pending = [points.pop()]
        group = []
        while pending:
            point = pending.pop()
            group.append(point)
            r, c = point
            for neighbor in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if neighbor in points:
                    points.remove(neighbor)
                    pending.append(neighbor)
        groups.append(group)
    return groups


def solve(grid):
    frame_color = Counter(value for row in grid for value in row if value).most_common(1)[0][0]
    frames = _components(
        {
            (r, c)
            for r, row in enumerate(grid)
            for c, value in enumerate(row)
            if value == frame_color
        }
    )
    boxes = []
    legend: dict[tuple[int, int], int] = {}
    for frame in frames:
        top, bottom = min(r for r, _ in frame), max(r for r, _ in frame)
        left, right = min(c for _, c in frame), max(c for _, c in frame)
        interior = {
            (r, c)
            for r in range(top + 1, bottom)
            for c in range(left + 1, right)
            if grid[r][c] != frame_color
        }
        rooms = _components(interior)
        if len(rooms) != 4:
            continue
        ordered = []
        for room in rooms:
            center = (sum(r for r, _ in room) / len(room), sum(c for _, c in room) / len(room))
            key = (int(center[0] > (top + bottom) / 2), int(center[1] > (left + right) / 2))
            colors = {grid[r][c] for r, c in room if grid[r][c] not in (0, frame_color)}
            if colors:
                legend[key] = next(iter(colors))
            ordered.append((key, room))
        boxes.append(ordered)
    output = [row[:] for row in grid]
    for rooms in boxes:
        for key, room in rooms:
            for r, c in room:
                output[r][c] = legend[key]
    return output
