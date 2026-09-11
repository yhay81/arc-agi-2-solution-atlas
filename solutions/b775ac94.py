def solve(grid):
    height, width = len(grid), len(grid[0]) if grid else 0
    source = [row[:] for row in grid]
    components = []
    markers = []
    for color in sorted({value for row in source for value in row if value}):
        seen = set()
        for row in range(height):
            for col in range(width):
                if source[row][col] != color or (row, col) in seen:
                    continue
                seen.add((row, col))
                stack = [(row, col)]
                component = []
                while stack:
                    current_row, current_col = stack.pop()
                    component.append((current_row, current_col))
                    for row_delta in (-1, 0, 1):
                        for col_delta in (-1, 0, 1):
                            next_row = current_row + row_delta
                            next_col = current_col + col_delta
                            if (
                                (row_delta or col_delta)
                                and 0 <= next_row < height
                                and 0 <= next_col < width
                                and source[next_row][next_col] == color
                                and (next_row, next_col) not in seen
                            ):
                                seen.add((next_row, next_col))
                                stack.append((next_row, next_col))
                if len(component) == 1:
                    markers.append((color, row, col))
                else:
                    rows = [r for r, _ in component]
                    cols = [c for _, c in component]
                    top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
                    mask = {(r - top, c - left) for r, c in component}
                    components.append((top, bottom, left, right, mask))
    if not components or not markers:
        return source
    output = [row[:] for row in source]
    for top, bottom, left, right, mask in components:
        tile_height, tile_width = bottom - top + 1, right - left + 1
        groups = {}
        for marker_color, marker_row, marker_col in markers:
            row_delta = -1 if marker_row < top else 1 if marker_row > bottom else 0
            col_delta = -1 if marker_col < left else 1 if marker_col > right else 0
            if not (row_delta or col_delta):
                continue
            if row_delta and abs(marker_row - (top if row_delta < 0 else bottom)) != 1:
                continue
            if col_delta and abs(marker_col - (left if col_delta < 0 else right)) != 1:
                continue
            if not row_delta and marker_row not in (top, bottom):
                continue
            if not col_delta and marker_col not in (left, right):
                continue
            target_top = top + row_delta * tile_height
            target_left = left + col_delta * tile_width
            if (
                target_top < 0
                or target_left < 0
                or target_top + tile_height > height
                or target_left + tile_width > width
            ):
                continue
            if row_delta and col_delta:
                transformed = {(tile_height - 1 - r, tile_width - 1 - c) for r, c in mask}
                target_row = 0 if row_delta > 0 else tile_height - 1
                target_col = 0 if col_delta > 0 else tile_width - 1
                source_row, source_col = tile_height - 1 - target_row, tile_width - 1 - target_col
            elif row_delta:
                transformed = {(tile_height - 1 - r, c) for r, c in mask}
                target_row = 0 if row_delta > 0 else tile_height - 1
                target_col = marker_col - target_left
                source_row, source_col = tile_height - 1 - target_row, target_col
            else:
                transformed = {(r, tile_width - 1 - c) for r, c in mask}
                target_row = marker_row - target_top
                target_col = 0 if col_delta > 0 else tile_width - 1
                source_row, source_col = target_row, tile_width - 1 - target_col
            if (target_row, target_col) not in transformed:
                continue
            if (source_row, source_col) not in (
                (0, 0),
                (0, tile_width - 1),
                (tile_height - 1, 0),
                (tile_height - 1, tile_width - 1),
            ):
                continue
            groups.setdefault((source_row, source_col), []).append(
                (marker_color, target_top, target_left, transformed)
            )
        for candidates in groups.values():
            for marker_color, target_top, target_left, transformed in candidates:
                for row_offset in range(tile_height):
                    for col_offset in range(tile_width):
                        if (row_offset, col_offset) in transformed:
                            output[target_top + row_offset][target_left + col_offset] = marker_color
    return output
