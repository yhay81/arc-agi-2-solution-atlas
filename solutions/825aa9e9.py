def solve(grid):
    source = [list(row) for row in grid]
    height = len(source)
    width = len(source[0]) if height else 0
    if not height or not width:
        return source
    counts = {}
    for row in source:
        for color in row:
            counts[color] = counts.get(color, 0) + 1
    dominant_color = max(counts, key=lambda color: (counts[color], -color))
    bottom_colors = set(source[-1])
    frame_candidates = sorted(bottom_colors - {dominant_color})
    if len(frame_candidates) == 1:
        frame_color = frame_candidates[0]
    elif len(bottom_colors) == 1:
        frame_color = next(iter(bottom_colors))
    else:
        return source
    background_candidates = [
        (count, color) for color, count in counts.items() if color != frame_color
    ]
    if not background_candidates:
        return source
    background = max(background_candidates)[1]
    payload = {
        (row, col)
        for row in range(height)
        for col in range(width)
        if source[row][col] not in (background, frame_color)
    }
    if not payload:
        return source
    frame_rows = [
        row for row in range(height) if any(source[row][col] == frame_color for col in range(width))
    ]
    if not frame_rows:
        return source
    floor_row = frame_rows[-1]
    has_solid_floor = any(all(color == frame_color for color in source[row]) for row in frame_rows)
    global_gap = 2 if has_solid_floor else 1
    components = []
    seen = set()
    for start in sorted(payload):
        if start in seen:
            continue
        seen.add(start)
        stack = [start]
        component = []
        while stack:
            row, col = stack.pop()
            component.append((row, col))
            for row_delta in (-1, 0, 1):
                for col_delta in (-1, 0, 1):
                    if not row_delta and not col_delta:
                        continue
                    next_cell = (row + row_delta, col + col_delta)
                    if next_cell in payload and next_cell not in seen:
                        seen.add(next_cell)
                        stack.append(next_cell)
        components.append(component)
    output = [[background] * width for _ in range(height)]
    for row in range(height):
        for col in range(width):
            if source[row][col] == frame_color:
                output[row][col] = frame_color
    occupied = set()
    for component in sorted(components, key=lambda cells: -max(row for row, _ in cells)):
        limits = []
        for row, col in component:
            barrier = next(
                (
                    next_row
                    for next_row in range(row + 1, height)
                    if source[next_row][col] == frame_color
                ),
                None,
            )
            if barrier is None:
                barrier = floor_row
                gap = global_gap
            else:
                gap = 2
            limits.append(barrier - gap - row)
        shift = min(limits)
        while any((row + shift, col) in occupied for row, col in component):
            shift -= 1
        for row, col in component:
            target_row = row + shift
            if 0 <= target_row < height:
                output[target_row][col] = source[row][col]
                occupied.add((target_row, col))
    return output
