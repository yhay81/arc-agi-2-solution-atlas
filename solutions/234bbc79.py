def solve(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                r, c = stack.pop()
                cells.append((r, c))
                for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= rr < height
                        and 0 <= cc < width
                        and grid[rr][cc] != 0
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    segments = []
    for cells in components:
        top, left = min(r for r, _ in cells), min(c for _, c in cells)
        bottom, right = max(r for r, _ in cells), max(c for _, c in cells)
        segment = [row[left : right + 1] for row in grid[top : bottom + 1]]
        colors = {value for row in segment for value in row if value not in (0, 5)}
        if len(colors) != 1:
            return [row[:] for row in grid]
        body = next(iter(colors))
        left_ends = [r for r, row in enumerate(segment) if row[0] == 5]
        right_ends = [r for r, row in enumerate(segment) if row[-1] == 5]
        segment = [[body if value == 5 else value for value in row] for row in segment]
        segments.append((left, top, segment, left_ends, right_ends))
    segments.sort(key=lambda item: item[0])
    if len(segments) < 2:
        return [row[:] for row in grid]
    output_width = sum(len(segment[0]) for _, _, segment, _, _ in segments)
    output = [[0] * output_width for _ in range(height)]
    cursor = 0
    previous_end = None
    for index, (_, original_top, segment, left_ends, right_ends) in enumerate(segments):
        out_top = original_top
        if previous_end is not None:
            if len(left_ends) != 1:
                return [row[:] for row in grid]
            out_top = previous_end - left_ends[0]
        if out_top < 0 or out_top + len(segment) > height:
            return [row[:] for row in grid]
        for row, line in enumerate(segment):
            output[out_top + row][cursor : cursor + len(line)] = line
        if right_ends:
            if len(right_ends) != 1:
                return [row[:] for row in grid]
            previous_end = out_top + right_ends[0]
        elif index < len(segments) - 1:
            return [row[:] for row in grid]
        cursor += len(segment[0])
    return output
