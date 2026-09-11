from math import gcd, isqrt


def solve(grid):
    source = [list(row) for row in grid]
    values = {}
    for row in source:
        for value in row:
            if value:
                values[value] = values.get(value, 0) + 1
    if not values:
        return source
    background = max(values, key=values.get)
    background_cells = [
        (row, col)
        for row, line in enumerate(source)
        for col, value in enumerate(line)
        if value == background
    ]
    top = min(row for row, _ in background_cells)
    left = min(col for _, col in background_cells)
    bottom = max(row for row, _ in background_cells)
    right = max(col for _, col in background_cells)
    coarse = [line[left : right + 1] for line in source[top : bottom + 1]]

    def components(colour, data=source):
        remaining = {
            (row, col)
            for row, line in enumerate(data)
            for col, value in enumerate(line)
            if value == colour
        }
        found = []
        while remaining:
            seed = min(remaining)
            remaining.remove(seed)
            stack = [seed]
            component = [seed]
            while stack:
                row, col = stack.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    cell = (row + dr, col + dc)
                    if cell in remaining:
                        remaining.remove(cell)
                        stack.append(cell)
                        component.append(cell)
            found.append(component)
        return found

    other = []
    for colour in sorted(values):
        if colour != background:
            other.extend((colour, cells) for cells in components(colour))
    significant = [(colour, cells) for colour, cells in other if len(cells) >= 4]
    scale_square = 0
    for _, cells in significant:
        scale_square = gcd(scale_square, len(cells))
    scale = isqrt(scale_square) if scale_square else 1
    if scale * scale != scale_square:
        scale = 1

    height, width = len(coarse), len(coarse[0])
    remaining = {
        (row, col) for row in range(height) for col in range(width) if coarse[row][col] == 0
    }
    zero_components = []
    while remaining:
        seed = min(remaining)
        remaining.remove(seed)
        stack = [seed]
        component = [seed]
        while stack:
            row, col = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                cell = (row + dr, col + dc)
                if cell in remaining:
                    remaining.remove(cell)
                    stack.append(cell)
                    component.append(cell)
        zero_components.append(component)
    zero_components.sort(key=min)

    palettes = {}
    for colour, cells in significant:
        if len(cells) % (scale * scale):
            continue
        size = len(cells) // (scale * scale)
        centre = (
            sum(row for row, _ in cells) / len(cells),
            sum(col for _, col in cells) / len(cells),
        )
        palettes.setdefault(size, []).append((colour, centre))
    used = {}
    for cells in zero_components:
        entries = palettes.get(len(cells), [])
        available = [
            (index, colour, centre)
            for index, (colour, centre) in enumerate(entries)
            if index not in used.get(len(cells), set())
        ]
        if not available:
            continue
        centre = (
            sum(row for row, _ in cells) / len(cells) + top,
            sum(col for _, col in cells) / len(cells) + left,
        )
        index, colour, _ = min(
            available,
            key=lambda item: (centre[0] - item[2][0]) ** 2 + (centre[1] - item[2][1]) ** 2,
        )
        used.setdefault(len(cells), set()).add(index)
        for row, col in cells:
            coarse[row][col] = colour

    return [
        [coarse[row // scale][col // scale] for col in range(width * scale)]
        for row in range(height * scale)
    ]
