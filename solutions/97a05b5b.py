def _components(grid, diagonal, same_color):
    remaining = {
        (row, col) for row, values in enumerate(grid) for col, value in enumerate(values) if value
    }
    directions = [
        (dr, dc)
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr or dc) and (diagonal or not (dr and dc))
    ]
    found = []
    while remaining:
        start = min(remaining)
        color = grid[start[0]][start[1]]
        remaining.remove(start)
        stack = [start]
        cells = []
        while stack:
            row, col = stack.pop()
            cells.append((row, col))
            for dr, dc in directions:
                point = row + dr, col + dc
                if point in remaining and (not same_color or grid[point[0]][point[1]] == color):
                    remaining.remove(point)
                    stack.append(point)
        found.append(cells)
    return found


def _bounds(cells):
    return (
        min(row for row, _ in cells),
        max(row for row, _ in cells),
        min(col for _, col in cells),
        max(col for _, col in cells),
    )


def _crop(grid, cells):
    top, bottom, left, right = _bounds(cells)
    return [row[left : right + 1] for row in grid[top : bottom + 1]]


def _variants(glyph):
    variants = []
    rotated = glyph
    for _ in range(4):
        for variant in (rotated, [row[::-1] for row in rotated]):
            if variant not in variants:
                variants.append(variant)
        rotated = [list(row) for row in zip(*rotated[::-1])]
    return variants


def _best_placement(output, glyph, canvas_color):
    matches = []
    for variant in _variants(glyph):
        for row in range(len(output) - 2):
            for col in range(len(output[0]) - 2):
                window = [line[col : col + 3] for line in output[row : row + 3]]
                if all(
                    value in (0, canvas_color) and (value == 0) == (variant[dr][dc] == canvas_color)
                    for dr, line in enumerate(window)
                    for dc, value in enumerate(line)
                ):
                    margin = min(row, col, len(output) - row - 3, len(output[0]) - col - 3)
                    matches.append((margin, row, col, variant))
    if not matches:
        return None
    margin = max(match[0] for match in matches)
    positions = {(row, col) for score, row, col, _ in matches if score == margin}
    if len(positions) != 1:
        return None
    row, col = next(iter(positions))
    variant = next(
        item
        for score, match_row, match_col, item in matches
        if score == margin and (match_row, match_col) == (row, col)
    )
    return row, col, variant


def solve(grid):
    components = _components(grid, False, True)
    if not components:
        return [row[:] for row in grid]
    canvas = max(components, key=len)
    canvas_color = grid[canvas[0][0]][canvas[0][1]]
    top, bottom, left, right = _bounds(canvas)
    output = [row[left : right + 1] for row in grid[top : bottom + 1]]
    outside = [row[:] for row in grid]
    for row in range(top, bottom + 1):
        outside[row][left : right + 1] = [0] * (right - left + 1)

    glyphs = []
    for cells in _components(outside, True, False):
        glyph = _crop(outside, cells)
        if (
            len(glyph) == len(glyph[0]) == 3
            and all(value for row in glyph for value in row)
            and any(canvas_color in row for row in glyph)
        ):
            glyphs.append(glyph)
    for glyph in glyphs:
        placement = _best_placement(output, glyph, canvas_color)
        if placement is None:
            return [row[:] for row in grid]
        row, col, variant = placement
        for dr in range(3):
            output[row + dr][col : col + 3] = variant[dr]
    return output
