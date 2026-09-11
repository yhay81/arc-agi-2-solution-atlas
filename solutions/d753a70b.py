from collections import Counter


def solve(grid):
    a = grid
    height, width = len(a), len(a[0])
    base = Counter(value for row in a for value in row).most_common(1)[0][0]
    out = [row[:] for row in a]
    five_components = []
    for color, change in ((2, -1), (5, 1)):
        seen = set()
        components = []
        for row in range(height):
            for col in range(width):
                if a[row][col] != color or (row, col) in seen:
                    continue
                seen.add((row, col))
                stack = [(row, col)]
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
                components.append(points)
        if color == 5:
            five_components = components
        for points in components:
            point_set = set(points)
            if len(points) == 1:
                radius = 0
                center_row, center_col = points[0]
            else:
                top = min(row for row, _ in points)
                left = min(col for _, col in points)
                bottom = max(row for row, _ in points)
                right = max(col for _, col in points)
                center_row = (top + bottom) // 2
                center_col = (left + right) // 2
                radius = (bottom - top) // 2
                visible = {
                    (row, col)
                    for row in range(height)
                    for col in range(width)
                    if abs(row - center_row) + abs(col - center_col) == radius
                }
                if visible != point_set:
                    center_row = center_col = radius = None
            r0, c0 = points[0]
            if radius is None:
                candidates = []
                for candidate_row in range(-height, 2 * height):
                    for candidate_col in range(-width, 2 * width):
                        candidate_radius = abs(candidate_row - r0) + abs(candidate_col - c0)
                        if any(
                            abs(candidate_row - row) + abs(candidate_col - col) != candidate_radius
                            for row, col in point_set
                        ):
                            continue
                        visible = set()
                        for row in range(
                            max(0, candidate_row - candidate_radius),
                            min(height, candidate_row + candidate_radius + 1),
                        ):
                            offset = candidate_radius - abs(row - candidate_row)
                            for col in (candidate_col - offset, candidate_col + offset):
                                if 0 <= col < width:
                                    visible.add((row, col))
                        if visible == point_set:
                            candidates.append((candidate_radius, candidate_row, candidate_col))
                radius, center_row, center_col = min(candidates)
            for row, col in points:
                out[row][col] = base
            for row in range(height):
                for col in range(width):
                    if abs(row - center_row) + abs(col - center_col) == radius + change:
                        out[row][col] = color

    def rotate(grid, turns):
        for _ in range(turns % 4):
            grid = [list(row) for row in zip(*grid)][::-1]
        return grid

    for points in five_components:
        if len(points) != 3:
            continue
        mask = [[0] * width for _ in range(height)]
        for row, col in points:
            mask[row][col] = 1
        for rotation in range(4):
            rotated_mask = rotate(mask, rotation)
            coordinates = [
                (row, col)
                for row, values in enumerate(rotated_mask)
                for col, value in enumerate(values)
                if value
            ]
            top = min(row for row, _ in coordinates)
            left = min(col for _, col in coordinates)
            bottom = max(row for row, _ in coordinates)
            right = max(col for _, col in coordinates)
            rotated_height = len(rotated_mask)
            if bottom != rotated_height - 1 or (bottom - top, right - left) != (1, 2):
                continue
            if {(row - top, col - left) for row, col in coordinates} != {
                (0, 1),
                (1, 0),
                (1, 2),
            }:
                continue
            normal = rotate(out, rotation)
            for row in range(len(normal)):
                for col in range(len(normal[0])):
                    if abs(row - bottom) + abs(col - (left + 1)) == 2:
                        normal[row][col] = base
                    if row >= bottom - 2 and abs(col - (left + 2)) == row - (bottom - 2):
                        normal[row][col] = 5
            out = rotate(normal, -rotation)
            break
    return out
