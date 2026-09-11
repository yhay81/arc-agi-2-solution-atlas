def _describe_colors(grid, background):
    height, width = len(grid), len(grid[0])
    result = []
    for color in sorted({value for row in grid for value in row} - {background}):
        cells = [
            (row, col) for row in range(height) for col in range(width) if grid[row][col] == color
        ]
        rows, cols = zip(*cells)
        top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
        shape_height, shape_width = bottom - top + 1, right - left + 1
        result.append(
            (
                color,
                shape_height,
                shape_width,
                len(cells) / (shape_height * shape_width),
                top,
                left,
                cells,
            )
        )
    return result


def _build_base(grid, background, descriptions):
    dense = [item for item in descriptions if item[3] >= 0.3]
    if not dense:
        return None
    largest_area = max(item[1] * item[2] for item in dense)
    bases = sorted(
        (item for item in dense if item[1] * item[2] == largest_area),
        key=lambda item: (item[4], item[5]),
    )
    tile_height, tile_width = bases[0][1:3]
    if any(item[1:3] != (tile_height, tile_width) for item in bases):
        return None
    output = [[background] * tile_width for _ in range(tile_height * len(bases))]
    for index, (color, height, width, _, top, left, _) in enumerate(bases):
        for row in range(height):
            for col in range(width):
                if grid[top + row][left + col] != background:
                    output[index * tile_height + row][col] = color
    return output, {item[0] for item in bases}, tile_height, tile_width


def _components(cells):
    cells = set(cells)
    result = []
    while cells:
        start = min(cells)
        cells.remove(start)
        stack = [start]
        component = []
        while stack:
            row, col = stack.pop()
            component.append((row, col))
            for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if neighbor in cells:
                    cells.remove(neighbor)
                    stack.append(neighbor)
        result.append(component)
    return result


def _extract_motifs(descriptions, base_colors, tile_height, tile_width):
    motifs = []
    for color, height, width, density, top, left, cells in descriptions:
        if color in base_colors:
            continue
        parts = (
            [cells]
            if density >= 0.3 and height <= tile_height and width <= tile_width
            else _components(cells)
        )
        for component in parts:
            component_top = min(row for row, _ in component)
            component_left = min(col for _, col in component)
            motifs.append(
                (color, {(row - component_top, col - component_left) for row, col in component})
            )
    return motifs


def _placement_options(motifs, holes, height, width):
    placements = []
    for _, glyph in motifs:
        glyph_height = max(row for row, _ in glyph) + 1
        glyph_width = max(col for _, col in glyph) + 1
        options = []
        for top in range(height - glyph_height + 1):
            for left in range(width - glyph_width + 1):
                cells = frozenset((top + row, left + col) for row, col in glyph)
                if cells <= holes:
                    options.append((top, left, cells))
        if not options:
            return None
        placements.append(options)
    return placements


def _exact_cover(placements, holes):
    by_cell = {
        cell: [
            (index, option)
            for index, options in enumerate(placements)
            for option in options
            if cell in option[2]
        ]
        for cell in holes
    }
    failed = set()

    def search(remaining, used):
        state = frozenset(remaining), used
        if state in failed:
            return None
        if not remaining:
            return [] if len(used) == len(placements) else None
        choices = []
        for index, options in enumerate(placements):
            if index not in used:
                choices.append([(index, option) for option in options if option[2] <= remaining])
        choices.extend(
            [
                (index, option)
                for index, option in by_cell[cell]
                if index not in used and option[2] <= remaining
            ]
            for cell in sorted(remaining)
        )
        if any(not choice for choice in choices):
            failed.add(state)
            return None
        for index, (top, left, cells) in min(choices, key=len):
            suffix = search(remaining - cells, used | {index})
            if suffix is not None:
                return [(index, top, left), *suffix]
        failed.add(state)
        return None

    return search(holes, frozenset())


def solve(grid):
    if not grid or not grid[0]:
        return [row[:] for row in grid]
    counts = {
        value: sum(row.count(value) for row in grid) for value in {v for row in grid for v in row}
    }
    background = max(counts, key=lambda value: (counts[value], -value))
    descriptions = _describe_colors(grid, background)
    base = _build_base(grid, background, descriptions)
    if base is None:
        return [row[:] for row in grid]
    output, base_colors, tile_height, tile_width = base
    motifs = _extract_motifs(descriptions, base_colors, tile_height, tile_width)
    holes = {
        (row, col)
        for row in range(len(output))
        for col in range(tile_width)
        if output[row][col] == background
    }
    if not motifs or sum(len(glyph) for _, glyph in motifs) != len(holes):
        return [row[:] for row in grid]
    placements = _placement_options(motifs, holes, len(output), tile_width)
    selected = None if placements is None else _exact_cover(placements, holes)
    if selected is None:
        raise ValueError("motifs do not exactly cover the base mosaic")
    for index, top, left in selected:
        color, glyph = motifs[index]
        for row, col in glyph:
            output[top + row][left + col] = color
    return output
