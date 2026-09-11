from collections import Counter, deque


def _components(grid, color, diagonal):
    height, width = len(grid), len(grid[0])
    remaining = {
        (row, col) for row in range(height) for col in range(width) if grid[row][col] == color
    }
    directions = [
        (dr, dc)
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr or dc) and (diagonal or not (dr and dc))
    ]
    groups = []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        stack = [start]
        cells = []
        while stack:
            row, col = stack.pop()
            cells.append((row, col))
            for dr, dc in directions:
                point = row + dr, col + dc
                if point in remaining:
                    remaining.remove(point)
                    stack.append(point)
        groups.append(sorted(cells))
    return groups


def _containment_tree(grid, regions, background):
    height, width = len(grid), len(grid[0])
    labels = [[-1] * width for _ in range(height)]
    for index, cells in enumerate(regions):
        for row, col in cells:
            labels[row][col] = index
    neighbors = [set() for _ in regions]
    sea = []
    for index, cells in enumerate(regions):
        if grid[cells[0][0]][cells[0][1]] == background and any(
            row in (0, height - 1) or col in (0, width - 1) for row, col in cells
        ):
            sea.append(index)
        for row, col in cells:
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                rr, cc = row + dr, col + dc
                if 0 <= rr < height and 0 <= cc < width and labels[rr][cc] != index:
                    neighbors[index].add(labels[rr][cc])
    children = {index: [] for index in range(-1, len(regions))}
    seen = set(sea)
    queue = deque(sea)
    while queue:
        index = queue.popleft()
        for other in sorted(neighbors[index]):
            if other not in seen:
                seen.add(other)
                queue.append(other)
                children[-1 if index in sea else index].append(other)
    if len(seen) != len(regions):
        raise ValueError("task assumptions are not satisfied")
    return children


def _axis_positions(pieces, axis):
    order = sorted(range(len(pieces)), key=lambda index: pieces[index][2][axis])
    bands = []
    for index in order:
        if not bands or pieces[index][2][axis] - pieces[bands[-1][-1]][2][axis] > 3:
            bands.append([index])
        else:
            bands[-1].append(index)
    positions = {}
    end = -1
    for band in bands:
        before = max(pieces[index][1][axis] for index in band)
        after = max(
            len(pieces[index][0]) - 1 - pieces[index][1][axis]
            if axis == 0
            else len(pieces[index][0][0]) - 1 - pieces[index][1][axis]
            for index in band
        )
        anchor = end + 2 + before
        for index in band:
            positions[index] = anchor - pieces[index][1][axis]
        end = anchor + after
    return positions


def _add_root_margin(output, background):
    for axis in (0, 1):
        for edge in (0, -1):
            line = output[edge] if axis == 0 else [row[edge] for row in output]
            if sum(value != background for value in line) != 1:
                continue
            if axis == 0:
                blank = [background] * len(output[0])
                output.insert(0, blank) if edge == 0 else output.append(blank)
            elif edge == 0:
                for row in output:
                    row.insert(0, background)
            else:
                for row in output:
                    row.append(background)


def _render(index, regions, children, grid, background):
    color = background if index == -1 else grid[regions[index][0][0]][regions[index][0][1]]
    if not children[index]:
        cells = regions[index]
        center = (
            sum(row for row, _ in cells) / len(cells),
            sum(col for _, col in cells) / len(cells),
        )
        return [[color]], (0, 0), center, 0
    pieces = [_render(child, regions, children, grid, background) for child in children[index]]
    rows, cols = _axis_positions(pieces, 0), _axis_positions(pieces, 1)
    height = max(rows[k] + len(piece[0]) for k, piece in enumerate(pieces))
    width = max(cols[k] + len(piece[0][0]) for k, piece in enumerate(pieces))
    output = [[color] * (width + 1) for _ in range(height + 1)]
    for k, (piece, _, _, _) in enumerate(pieces):
        for row, values in enumerate(piece):
            output[rows[k] + row][cols[k] : cols[k] + len(values)] = values
    deepest = max(range(len(pieces)), key=lambda k: pieces[k][3])
    anchor = pieces[deepest][1][0] + rows[deepest], pieces[deepest][1][1] + cols[deepest]
    center, depth = pieces[deepest][2], pieces[deepest][3] + 1
    if index == -1:
        output = [row[1:-1] for row in output[1:-1]]
        _add_root_margin(output, background)
    return output, anchor, center, depth


def solve(grid):
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    ink = Counter(value for row in grid for value in row if value != background).most_common(1)[0][
        0
    ]
    regions = _components(grid, background, False) + _components(grid, ink, True)
    children = _containment_tree(grid, regions, background)
    return _render(-1, regions, children, grid, background)[0]
