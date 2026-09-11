from collections import Counter


def _components(mask):
    height, width = len(mask), len(mask[0])
    remaining = {(row, col) for row in range(height) for col in range(width) if mask[row][col]}
    found = []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        stack = [start]
        component = [start]
        while stack:
            row, col = stack.pop()
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    point = row + dr, col + dc
                    if (dr or dc) and point in remaining:
                        remaining.remove(point)
                        stack.append(point)
                        component.append(point)
        found.append(component)
    return found


def _find_wall(grid, background):
    height, width = len(grid), len(grid[0])
    mask = [[False] * width for _ in range(height)]
    for row, line in enumerate(grid):
        color, count = Counter(line).most_common(1)[0]
        if color not in (background, 8, 9) and count >= width * 0.7:
            mask[row] = [True] * width
    for col in range(width):
        line = [grid[row][col] for row in range(height)]
        color, count = Counter(line).most_common(1)[0]
        if color not in (background, 8, 9) and count >= height * 0.7:
            for row in range(height):
                mask[row][col] = True
    return mask


def _extract_scene(grid, background):
    height, width = len(grid), len(grid[0])
    wall_mask = _find_wall(grid, background)
    objects = _components(
        [
            [grid[row][col] != background and not wall_mask[row][col] for col in range(width)]
            for row in range(height)
        ]
    )
    objects = [
        cells
        for cells in objects
        if any(grid[row][col] == 8 for row, col in cells)
        and any(grid[row][col] == 9 for row, col in cells)
    ]
    marker_mask = [[value == 9 for value in row] for row in grid]
    for cells in objects:
        for row, col in cells:
            marker_mask[row][col] = False
    markers = _components(marker_mask)
    wall = [row[:] for row in grid]
    for cells in objects + markers:
        for row, col in cells:
            wall[row][col] = background
    return objects, markers, wall


def _crop(grid, cells, background):
    top = min(row for row, _ in cells)
    left = min(col for _, col in cells)
    bottom = max(row for row, _ in cells)
    right = max(col for _, col in cells)
    return [
        [grid[row][col] if (row, col) in cells else background for col in range(left, right + 1)]
        for row in range(top, bottom + 1)
    ]


def _orientations(block):
    for flipped in (False, True):
        transformed = [row[::-1] for row in block] if flipped else [row[:] for row in block]
        for _ in range(4):
            yield transformed, flipped
            transformed = [list(row) for row in zip(*transformed)][::-1]


def _alignment(motif, marker):
    nines = [
        (row, col) for row, line in enumerate(motif) for col, value in enumerate(line) if value == 9
    ]
    delta = (
        min(row for row, _ in marker) - min(row for row, _ in nines),
        min(col for _, col in marker) - min(col for _, col in nines),
    )
    shifted = {(row + delta[0], col + delta[1]) for row, col in nines}
    return delta if shifted == set(marker) else None


def _valid_placement(motif, delta, wall, background):
    height, width = len(wall), len(wall[0])
    cells = [
        (row + delta[0], col + delta[1])
        for row, line in enumerate(motif)
        for col, value in enumerate(line)
        if value != background
    ]
    if any(row < 0 or row >= height or col < 0 or col >= width for row, col in cells):
        return False
    for row, line in enumerate(motif):
        for col, color in enumerate(line):
            if color in (background, 8, 9):
                continue
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                near_row, near_col = row - dr, col - dc
                if not (
                    0 <= near_row < len(motif)
                    and 0 <= near_col < len(motif[0])
                    and motif[near_row][near_col] in (8, 9)
                ):
                    continue
                target_row = row + delta[0] + dr
                target_col = col + delta[1] + dc
                while (
                    0 <= target_row < height
                    and 0 <= target_col < width
                    and wall[target_row][target_col] == background
                ):
                    target_row += dr
                    target_col += dc
                if (
                    0 <= target_row < height
                    and 0 <= target_col < width
                    and wall[target_row][target_col] == color
                ):
                    break
            else:
                return False
    return True


def _render(motif, delta, shape, background):
    output = [[background] * len(shape[0]) for _ in shape]
    for row, line in enumerate(motif):
        for col, color in enumerate(line):
            if color != background:
                output[row + delta[0]][col + delta[1]] = color
    return output


def _place_object(grid, cells, markers, wall, background):
    candidates = []
    for motif, flipped in _orientations(_crop(grid, cells, background)):
        for marker_index, marker in enumerate(markers):
            delta = _alignment(motif, marker)
            if delta is not None and _valid_placement(motif, delta, wall, background):
                candidates.append((marker_index, _render(motif, delta, wall, background), flipped))
    if not candidates:
        raise ValueError("task assumptions are not satisfied")
    preferred = [candidate for candidate in candidates if candidate[2] == candidates[0][2]]
    if not all(item[:2] == preferred[0][:2] for item in preferred):
        raise ValueError("task assumptions are not satisfied")
    return preferred[0][:2]


def solve(grid):
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    objects, markers, wall = _extract_scene(grid, background)
    answers = [_place_object(grid, cells, markers, wall, background) for cells in objects]
    if len({marker_index for marker_index, _ in answers}) != len(answers):
        raise ValueError("task assumptions are not satisfied")
    output = [row[:] for row in wall]
    for _, placement in answers:
        for row, line in enumerate(placement):
            for col, color in enumerate(line):
                if color != background:
                    output[row][col] = color
    return output
