def solve(grid):
    if not grid or not grid[0]:
        return [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    components = {}
    for color in (5, 7):
        seen = set()
        found = []
        for row in range(height):
            for col in range(width):
                if grid[row][col] != color or (row, col) in seen:
                    continue
                stack = [(row, col)]
                seen.add((row, col))
                component = []
                while stack:
                    current_row, current_col = stack.pop()
                    component.append((current_row, current_col))
                    for next_row, next_col in (
                        (current_row - 1, current_col),
                        (current_row + 1, current_col),
                        (current_row, current_col - 1),
                        (current_row, current_col + 1),
                    ):
                        if (
                            0 <= next_row < height
                            and 0 <= next_col < width
                            and grid[next_row][next_col] == color
                            and (next_row, next_col) not in seen
                        ):
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
                found.append(component)
        components[color] = found
    marker_components, target_components = components[5], components[7]
    if not marker_components or not target_components:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for component in marker_components:
        for row, col in component:
            output[row][col] = 4
    for component in target_components:
        top = min(row for row, _ in component)
        bottom = max(row for row, _ in component)
        left = min(col for _, col in component)
        right = max(col for _, col in component)
        if len(component) != (bottom - top + 1) * (right - left + 1):
            continue
        horizontal, vertical = [], []
        for marker in marker_components:
            marker_top = min(row for row, _ in marker)
            marker_bottom = max(row for row, _ in marker)
            marker_left = min(col for _, col in marker)
            marker_right = max(col for _, col in marker)
            row_overlap = max(0, min(marker_bottom, bottom) - max(marker_top, top) + 1)
            col_overlap = max(0, min(marker_right, right) - max(marker_left, left) + 1)
            if row_overlap and (marker_right == left - 1 or marker_left == right + 1):
                horizontal.append(marker)
            if col_overlap and (marker_bottom == top - 1 or marker_top == bottom + 1):
                vertical.append(marker)
        supplied = sum(len(marker) for marker in horizontal + vertical)
        if not supplied:
            continue
        if horizontal:
            rows = sorted(
                range(top, bottom + 1),
                key=lambda row: min(
                    abs(row - marker_row) for marker in horizontal for marker_row, _ in marker
                ),
            )
            cells = [(row, col) for row in rows for col in range(left, right + 1)]
        elif vertical:
            columns = sorted(
                range(left, right + 1),
                key=lambda col: min(
                    abs(col - marker_col) for marker in vertical for _, marker_col in marker
                ),
            )
            cells = [(row, col) for col in columns for row in range(top, bottom + 1)]
        else:
            continue
        for row, col in cells[:supplied]:
            if 0 <= row < height and 0 <= col < width:
                output[row][col] = 5
    return output
