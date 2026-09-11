from collections import Counter


def solve(grid):
    a = grid
    bg = Counter(value for row in a for value in row).most_common(1)[0][0]
    height, width = len(a), len(a[0])
    components = []
    for color in {value for row in a for value in row if value != bg}:
        seen = set()
        for row in range(height):
            for col in range(width):
                if a[row][col] != color or (row, col) in seen:
                    continue
                stack = [(row, col)]
                seen.add((row, col))
                points = []
                while stack:
                    r, c = stack.pop()
                    points.append((r, c))
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            neighbor = (r + dr, c + dc)
                            if (
                                neighbor not in seen
                                and 0 <= neighbor[0] < height
                                and 0 <= neighbor[1] < width
                                and a[neighbor[0]][neighbor[1]] == color
                            ):
                                seen.add(neighbor)
                                stack.append(neighbor)
                components.append((color, points))

    frames = []
    for color, points in components:
        top = min(row for row, _ in points)
        left = min(col for _, col in points)
        bottom = max(row for row, _ in points)
        right = max(col for _, col in points)
        if bottom - top < 2 or right - left < 2:
            continue
        if (
            all(a[top][col] == color for col in range(left, right + 1))
            and all(a[bottom][col] == color for col in range(left, right + 1))
            and all(a[row][left] == color for row in range(top, bottom + 1))
            and all(a[row][right] == color for row in range(top, bottom + 1))
            and len(
                {a[row][col] for row in range(top + 1, bottom) for col in range(left + 1, right)}
            )
            == 1
        ):
            frames.append(((bottom - top) * (right - left), top, left, bottom, right))

    _, top, left, bottom, right = max(frames)
    out = [row[left + 1 : right] for row in a[top + 1 : bottom]]
    active = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if a[row][col] != bg and not (top <= row <= bottom and left <= col <= right)
    }
    groups = {}
    seen = set()
    for start in sorted(active):
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        points = []
        while stack:
            row, col = stack.pop()
            points.append((row, col))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    neighbor = (row + dr, col + dc)
                    if neighbor in active and neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
        colors = tuple(sorted({a[row][col] for row, col in points}))
        groups.setdefault(colors, []).extend(points)

    for colors, points in groups.items():
        top2 = min(row for row, _ in points)
        left2 = min(col for _, col in points)
        bottom2 = max(row for row, _ in points)
        right2 = max(col for _, col in points)
        if bottom2 - top2 < 2 or right2 - left2 < 2:
            continue
        visible = set(points)
        for row in range(top + 1, bottom):
            for col in range(left + 1, right):
                if not (top2 <= row <= bottom2 and left2 <= col <= right2):
                    continue
                if row not in (top2, bottom2) and col not in (left2, right2):
                    continue
                if len(colors) == 1:
                    color = colors[0]
                else:
                    source = next(
                        point
                        for point in ((top2 + bottom2 - row, col), (row, left2 + right2 - col))
                        if point in visible
                    )
                    color = next(value for value in colors if value != a[source[0]][source[1]])
                out[row - top - 1][col - left - 1] = color
    return out
