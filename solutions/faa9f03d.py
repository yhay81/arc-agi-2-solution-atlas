def _intersection_proposals(grid, colors):
    height, width = len(grid), len(grid[0])
    proposals = {}
    for row in range(height):
        for col in range(width):
            horizontal = vertical = None
            for color in colors:
                left = [index for index in range(col) if grid[row][index] == color]
                right = [index for index in range(col + 1, width) if grid[row][index] == color]
                if left and right and right[0] - left[-1] == 2:
                    horizontal = color
                up = [index for index in range(row) if grid[index][col] == color]
                down = [index for index in range(row + 1, height) if grid[index][col] == color]
                pure_up = up and not any(
                    0 <= col + step < width and grid[up[-1]][col + step] == color
                    for step in (-1, 1)
                )
                pure_down = down and not any(
                    0 <= col + step < width and grid[down[0]][col + step] == color
                    for step in (-1, 1)
                )
                if up and down and down[0] - up[-1] == 2 and (pure_up or pure_down):
                    vertical = color
            proposals[row, col] = horizontal, vertical
    return proposals


def _reaches(edges, start, target):
    reachable = {start}
    pending = [start]
    while pending:
        node = pending.pop()
        for first, second in edges:
            if first == node and second not in reachable:
                reachable.add(second)
                pending.append(second)
    return target in reachable


def _fill_long_gaps(output, erased):
    filled = [row[:] for row in output]
    width = len(output[0])
    for row, values in enumerate(filled):
        for color in {value for value in values if value}:
            positions = [col for col, value in enumerate(values) if value == color]
            for left, right in zip(positions, positions[1:]):
                bounded = left > 0 and right < width - 1
                surrounded = bounded and values[left - 1] == values[right + 1] == color
                untouched = not any((row, col) in erased for col in range(left + 1, right))
                if right - left > 2 and surrounded and untouched:
                    for col in range(left + 1, right):
                        if output[row][col] == 0:
                            output[row][col] = color


def solve(grid):
    a = grid
    source = [row[:] for row in a]
    height, width = len(source), len(source[0]) if source else 0
    output = [row[:] for row in source]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    priority = None
    erased = set()
    extension_colors = set()
    for marker_row in range(height):
        for marker_col in range(width):
            if source[marker_row][marker_col] != 4:
                continue
            options = []
            for row_delta, col_delta in directions:
                row, col = marker_row + row_delta, marker_col + col_delta
                length = 0
                color = None
                while 0 <= row < height and 0 <= col < width and output[row][col] not in (0, 4):
                    value = output[row][col]
                    if value != 2 and color is None:
                        color = value
                    if color is not None and value not in (2, color):
                        break
                    length += 1
                    row += row_delta
                    col += col_delta
                if length:
                    options.append(
                        (
                            output[marker_row + row_delta][marker_col + col_delta] == 2,
                            length,
                            row_delta,
                            col_delta,
                            color,
                        )
                    )
            if not options:
                continue
            _, _, row_delta, col_delta, color = max(options)
            if color is None:
                continue
            row, col = marker_row + row_delta, marker_col + col_delta
            kept = (row, col)
            remove = []
            gap = 0
            row += row_delta
            col += col_delta
            while 0 <= row < height and 0 <= col < width:
                value = output[row][col]
                if value in (color, 2):
                    remove.append((row, col))
                    gap = 0
                elif value == 0:
                    gap += 1
                    if gap > 1:
                        break
                else:
                    break
                row += row_delta
                col += col_delta
            queue = [(row, col) for row, col in remove if output[row][col] == 2]
            seen = set(remove)
            while queue:
                row, col = queue.pop()
                for step_row, step_col in directions:
                    next_cell = (row + step_row, col + step_col)
                    if next_cell == kept or next_cell in seen:
                        continue
                    next_row, next_col = next_cell
                    if (
                        0 <= next_row < height
                        and 0 <= next_col < width
                        and output[next_row][next_col] in (color, 2)
                    ):
                        seen.add(next_cell)
                        queue.append(next_cell)
            for row, col in seen:
                output[row][col] = 0
            erased |= seen
            output[marker_row][marker_col] = color
            extension_colors.add(color)
            priority = "h" if col_delta else "v"
            row, col = marker_row - row_delta, marker_col - col_delta
            while 0 <= row < height and 0 <= col < width:
                output[row][col] = color
                row -= row_delta
                col -= col_delta
    for row in range(height):
        for col in range(width):
            if output[row][col] != 2:
                continue
            values = []
            for row_delta, col_delta in directions:
                next_row, next_col = row + row_delta, col + col_delta
                value = (
                    output[next_row][next_col]
                    if 0 <= next_row < height and 0 <= next_col < width
                    else 0
                )
                if value not in (0, 2, 4):
                    values.append(value)
            if values:
                counts = {}
                for value in values:
                    counts[value] = counts.get(value, 0) + 1
                output[row][col] = max(counts, key=counts.get)
    pre = [row[:] for row in output]
    colors = {value for row in pre for value in row if value not in (0, 2, 4)}
    proposals = _intersection_proposals(pre, colors)
    edges = set()
    for (row, col), (horizontal, vertical) in proposals.items():
        if (
            source[row][col] == 0
            and horizontal is not None
            and vertical is not None
            and horizontal != vertical
        ):
            winner = horizontal if priority == "h" and horizontal in extension_colors else vertical
            front, back = winner, vertical if winner == horizontal else horizontal
            if front != back and not _reaches(edges, back, front):
                edges.add((front, back))
    for (row, col), (horizontal, vertical) in proposals.items():
        if (
            horizontal is not None
            and vertical is not None
            and horizontal != vertical
            and source[row][col] in (horizontal, vertical)
        ):
            front, back = (
                (vertical, source[row][col])
                if source[row][col] == horizontal
                else (horizontal, source[row][col])
            )
            if not _reaches(edges, back, front):
                edges.add((front, back))
    for (row, col), (horizontal, vertical) in proposals.items():
        if horizontal is not None and vertical is not None:
            if horizontal == vertical or _reaches(edges, horizontal, vertical):
                winner = horizontal
            elif _reaches(edges, vertical, horizontal):
                winner = vertical
            else:
                winner = (
                    horizontal if priority == "h" and horizontal in extension_colors else vertical
                )
            output[row][col] = winner
        elif vertical is not None:
            output[row][col] = vertical
        elif horizontal is not None and (not priority or pre[row][col] == 0):
            output[row][col] = horizontal
    _fill_long_gaps(output, erased)
    return output
