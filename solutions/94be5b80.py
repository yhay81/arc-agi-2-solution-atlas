def solve(grid):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    source = [row[:] for row in grid]
    if not rows or not cols:
        return source

    def components(cells, diagonal=False):
        found, seen = [], set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if diagonal:
            directions += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for start in sorted(cells):
            if start in seen:
                continue
            seen.add(start)
            stack, component = [start], []
            while stack:
                row, col = stack.pop()
                component.append((row, col))
                for dr, dc in directions:
                    neighbor = row + dr, col + dc
                    if neighbor in cells and neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            found.append(component)
        return found

    occupied = {(row, col) for row in range(rows) for col in range(cols) if source[row][col]}
    key_cells = key_colors = None
    for component in components(occupied):
        top = min(row for row, _ in component)
        bottom = max(row for row, _ in component)
        left = min(col for _, col in component)
        right = max(col for _, col in component)
        if (
            bottom - top < 1
            or right - left < 1
            or len(component) != (bottom - top + 1) * (right - left + 1)
        ):
            continue
        first = source[top][left : right + 1]
        if len(set(first)) != len(first) or any(
            source[row][left : right + 1] != first for row in range(top, bottom + 1)
        ):
            continue
        key_cells, key_colors = set(component), first
        break
    if key_cells is None:
        return source

    glyphs = []
    for color in sorted({value for row in source for value in row if value}):
        cells = {
            (row, col) for row in range(rows) for col in range(cols) if source[row][col] == color
        }
        for component in components(cells, True):
            if any(cell in key_cells for cell in component):
                continue
            top = min(row for row, _ in component)
            left = min(col for _, col in component)
            bottom = max(row for row, _ in component)
            right = max(col for _, col in component)
            mask = {(row - top, col - left) for row, col in component}
            glyphs.append((top, left, bottom - top + 1, right - left + 1, mask, color))
    if not glyphs:
        return source
    height, width = glyphs[0][2:4]
    if any((item[2], item[3], item[4]) != (height, width, glyphs[0][4]) for item in glyphs):
        return source
    starts = {
        top - index * height
        for top, _, _, _, _, color in glyphs
        for index, expected in enumerate(key_colors)
        if color == expected
    }
    if len(starts) != 1:
        return source
    start = next(iter(starts))
    left = glyphs[0][1]
    if start < 0 or start + len(key_colors) * height > rows:
        return source
    output = [[0] * cols for _ in range(rows)]
    for index, color in enumerate(key_colors):
        top = start + index * height
        for dr, dc in glyphs[0][4]:
            output[top + dr][left + dc] = color
    return output
