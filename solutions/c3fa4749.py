def components(grid: list[list[bool]]) -> list[list[tuple[int, int]]]:
    height, width = len(grid), len(grid[0])
    seen = set()
    result = []
    for row in range(height):
        for col in range(width):
            if not grid[row][col] or (row, col) in seen:
                continue
            seen.add((row, col))
            stack = [(row, col)]
            part = []
            while stack:
                current = stack.pop()
                part.append(current)
                r, c = current
                for rr in range(r - 1, r + 2):
                    for cc in range(c - 1, c + 2):
                        if (rr, cc) == (r, c):
                            continue
                        if (
                            0 <= rr < height
                            and 0 <= cc < width
                            and grid[rr][cc]
                            and (rr, cc) not in seen
                        ):
                            seen.add((rr, cc))
                            stack.append((rr, cc))
            result.append(part)
    return result


def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for color in set(cell for row in grid for cell in row):
        for part in components([[cell == color for cell in row] for row in grid]):
            if len(part) < 20:
                continue
            top = min(row for row, _ in part)
            bottom = max(row for row, _ in part)
            left = min(col for _, col in part)
            right = max(col for _, col in part)
            mask = [[False] * width for _ in range(height)]
            for row, col in part:
                mask[row][col] = True
            holes = [[False] * width for _ in range(height)]
            for row in range(height):
                points = [col for col in range(width) if mask[row][col]]
                for first, second in zip(points, points[1:]):
                    if 1 < second - first <= 4:
                        for col in range(first + 1, second):
                            holes[row][col] = True
            for col in range(width):
                points = [row for row in range(height) if mask[row][col]]
                for first, second in zip(points, points[1:]):
                    if 1 < second - first <= 4:
                        for row in range(first + 1, second):
                            holes[row][col] = True
            for hole in components(holes):
                edge = [
                    (row, col) for row, col in hole if row in (top, bottom) or col in (left, right)
                ]
                colors = {grid[row][col] for row, col in edge}
                if not edge or len(colors) != 1:
                    continue
                filled = {tuple(cell) for cell in hole}
                outside = set()
                stack = []
                for row in range(height):
                    for col in range(width):
                        if row in (0, height - 1) or col in (0, width - 1):
                            if (row, col) not in filled and (row, col) not in outside:
                                outside.add((row, col))
                                stack.append((row, col))
                while stack:
                    row, col = stack.pop()
                    for rr, cc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                        if (
                            0 <= rr < height
                            and 0 <= cc < width
                            and (rr, cc) not in filled
                            and (rr, cc) not in outside
                        ):
                            outside.add((rr, cc))
                            stack.append((rr, cc))
                filled = {
                    (row, col)
                    for row in range(height)
                    for col in range(width)
                    if (row, col) not in outside
                }
                for _ in range(height * width):
                    added = set()
                    for row in range(top, bottom + 1):
                        for col in range(left, right + 1):
                            if (row, col) in filled or grid[row][col] == color:
                                continue
                            neighbors = sum(
                                (rr, cc) in filled
                                for rr, cc in (
                                    (row - 1, col),
                                    (row + 1, col),
                                    (row, col - 1),
                                    (row, col + 1),
                                )
                            )
                            if neighbors >= 2:
                                added.add((row, col))
                    if not added:
                        break
                    filled |= added
                replacement = next(iter(colors))
                for row, col in filled:
                    output[row][col] = replacement
    return output
