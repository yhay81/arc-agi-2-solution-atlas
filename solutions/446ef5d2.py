from collections import Counter


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
                r, c = stack.pop()
                part.append((r, c))
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
    background = Counter(cell for row in grid for cell in row).most_common(1)[0][0]
    colors = set(cell for row in grid for cell in row)
    mark = next(
        color
        for color in colors - {background}
        if sum(cell == color for row in grid for cell in row) == 3
        and max(
            max(row for row in range(height) for col in range(width) if grid[row][col] == color)
            - min(row for row in range(height) for col in range(width) if grid[row][col] == color),
            max(col for row in range(height) for col in range(width) if grid[row][col] == color)
            - min(col for row in range(height) for col in range(width) if grid[row][col] == color),
        )
        == 1
    )
    markers = [
        (row, col) for row in range(height) for col in range(width) if grid[row][col] == mark
    ]
    top = min(row for row, _ in markers)
    left = min(col for _, col in markers)
    bottom = max(row for row, _ in markers)
    right = max(col for _, col in markers)
    corner = next(
        (row, col) for row in (top, bottom) for col in (left, right) if grid[row][col] != mark
    )
    parts = components(
        [
            [grid[row][col] != background and grid[row][col] != mark for col in range(width)]
            for row in range(height)
        ]
    )
    base = Counter(grid[row][col] for part in parts for row, col in part).most_common(1)[0][0]
    area = sum(len(part) for part in parts)
    anchor = next(index for index, part in enumerate(parts) if corner in part)
    full = (1 << area) - 1
    for canvas_height in range(1, height + 1):
        if area % canvas_height:
            continue
        canvas_width = area // canvas_height
        if canvas_width > width:
            continue
        origin_row = corner[0] - canvas_height + 1 if corner[0] == top else corner[0]
        origin_col = corner[1] - canvas_width + 1 if corner[1] == left else corner[1]
        if (
            min(origin_row, origin_col) < 0
            or origin_row + canvas_height > height
            or origin_col + canvas_width > width
        ):
            continue
        options = []
        cover = [[] for _ in range(area)]
        for index, part in enumerate(parts):
            part_top = min(row for row, _ in part)
            part_left = min(col for _, col in part)
            part_bottom = max(row for row, _ in part)
            part_right = max(col for _, col in part)
            offsets = [(row - part_top, col - part_left) for row, col in part]
            values = [grid[row][col] for row, col in part]
            part_height = part_bottom - part_top + 1
            part_width = part_right - part_left + 1
            positions = (
                [(part_top - origin_row, part_left - origin_col)]
                if index == anchor
                else [
                    (row, col)
                    for row in range(canvas_height - part_height + 1)
                    for col in range(canvas_width - part_width + 1)
                ]
            )
            for row, col in positions:
                cells = [(row + dr, col + dc) for dr, dc in offsets]
                if any(r < 0 or c < 0 or r >= canvas_height or c >= canvas_width for r, c in cells):
                    continue
                edge = [r in (0, canvas_height - 1) or c in (0, canvas_width - 1) for r, c in cells]
                if any(value != base for value, is_edge in zip(values, edge) if is_edge):
                    continue
                ids = [r * canvas_width + c for r, c in cells]
                option_index = len(options)
                options.append((index, ids, values, sum(1 << cell for cell in ids)))
                for cell in ids:
                    cover[cell].append(option_index)
        canvas = [-1] * area
        failed = set()

        def search(occupied: int, used: int) -> list[int] | None:
            state = occupied, used, tuple(canvas)
            if state in failed:
                return None
            if occupied == full:
                colors = set(canvas) - {base, -1}
                for color in colors:
                    if (
                        len(
                            components(
                                [
                                    [
                                        canvas[row * canvas_width + col] == color
                                        for col in range(canvas_width)
                                    ]
                                    for row in range(canvas_height)
                                ]
                            )
                        )
                        != 1
                    ):
                        failed.add(state)
                        return None
                return canvas[:]
            best = None
            for cell in range(area):
                if occupied >> cell & 1:
                    continue
                candidates = [
                    option
                    for option in cover[cell]
                    if not used >> options[option][0] & 1 and not occupied & options[option][3]
                ]
                if not candidates:
                    failed.add(state)
                    return None
                if best is None or len(candidates) < len(best):
                    best = candidates
                if len(best) == 1:
                    break
            for option in best:
                index, cells, values, mask = options[option]
                valid = True
                for cell, value in zip(cells, values):
                    if value == base:
                        continue
                    row, col = divmod(cell, canvas_width)
                    if any(
                        0 <= rr < canvas_height
                        and 0 <= cc < canvas_width
                        and canvas[rr * canvas_width + cc] not in (-1, base, value)
                        for rr, cc in (
                            (row - 1, col),
                            (row + 1, col),
                            (row, col - 1),
                            (row, col + 1),
                        )
                    ):
                        valid = False
                        break
                if not valid:
                    continue
                for cell, value in zip(cells, values):
                    canvas[cell] = value
                answer = search(occupied | mask, used | (1 << index))
                if answer is not None:
                    return answer
                for cell in cells:
                    canvas[cell] = -1
            failed.add(state)
            return None

        answer = search(0, 0)
        if answer is not None:
            output = [[background] * width for _ in range(height)]
            for row in range(canvas_height):
                for col in range(canvas_width):
                    output[origin_row + row][origin_col + col] = answer[row * canvas_width + col]
            return output
    raise ValueError("no connected-color rectangle packing")
