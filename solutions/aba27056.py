def solve(grid):
    source = [list(row) for row in grid]
    output = [row[:] for row in source]
    if not source or not source[0]:
        return output
    height, width = len(source), len(source[0])
    counts = {}
    for row in source:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    if len(counts) < 2:
        return output
    background = min(((-count, value) for value, count in counts.items()))[1]
    colors = [value for value in counts if value != background]
    if len(colors) != 1:
        return output
    source_color = colors[0]
    points = [
        (row, col)
        for row in range(height)
        for col in range(width)
        if source[row][col] == source_color
    ]
    if len(points) < 5:
        return output
    top = min(row for row, _ in points)
    bottom = max(row for row, _ in points)
    left = min(col for _, col in points)
    right = max(col for _, col in points)
    if top == bottom or left == right:
        return output
    sides = {
        "top": [(top, col) for col in range(left, right + 1)],
        "bottom": [(bottom, col) for col in range(left, right + 1)],
        "left": [(row, left) for row in range(top, bottom + 1)],
        "right": [(row, right) for row in range(top, bottom + 1)],
    }
    gaps = {
        side: sum(source[row][col] == background for row, col in cells)
        for side, cells in sides.items()
    }
    opening = max(gaps, key=gaps.get)
    if not gaps[opening]:
        return output
    for row in range(top, bottom + 1):
        for col in range(left, right + 1):
            if source[row][col] == background:
                output[row][col] = 4
    if opening in ("left", "right"):
        edge = left if opening == "left" else right
        coordinates = [row for row in range(top, bottom + 1) if source[row][edge] == background]
    else:
        edge = top if opening == "top" else bottom
        coordinates = [col for col in range(left, right + 1) if source[edge][col] == background]
    if not coordinates:
        return output
    gap_start, gap_end = min(coordinates), max(coordinates)
    if opening in ("left", "right"):
        sequence = [source[row][edge] for row in range(top, bottom + 1)]
    else:
        sequence = [source[edge][col] for col in range(left, right + 1)]
    prefix = 0
    while prefix < len(sequence) and sequence[prefix] == source_color:
        prefix += 1
    suffix = 0
    while suffix < len(sequence) and sequence[-1 - suffix] == source_color:
        suffix += 1
    if prefix >= 2 and suffix >= 2:
        gap_start -= 1
        gap_end += 1
    if gap_end - gap_start + 1 >= 3:
        core_start, core_end = gap_start + 1, gap_end - 1
    else:
        core_start, core_end = gap_start, gap_end
    for distance in range(1, max(height, width) + 1):
        layer = edge - distance if opening in ("left", "top") else edge + distance
        if opening in ("left", "right"):
            if not 0 <= layer < width:
                continue
            for coordinate in range(core_start, core_end + 1):
                if 0 <= coordinate < height and output[coordinate][layer] == background:
                    output[coordinate][layer] = 4
            edge_offset = distance - 1
            for coordinate in (gap_start - edge_offset, gap_end + edge_offset):
                if 0 <= coordinate < height and output[coordinate][layer] == background:
                    output[coordinate][layer] = 4
        else:
            if not 0 <= layer < height:
                continue
            for coordinate in range(core_start, core_end + 1):
                if 0 <= coordinate < width and output[layer][coordinate] == background:
                    output[layer][coordinate] = 4
            edge_offset = distance - 1
            for coordinate in (gap_start - edge_offset, gap_end + edge_offset):
                if 0 <= coordinate < width and output[layer][coordinate] == background:
                    output[layer][coordinate] = 4
    return output
