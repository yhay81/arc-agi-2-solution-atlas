def _encode_u_frame_clearance(array):
    colors = list({v for row in array for v in row if v != 0})
    if len(colors) != 2:
        return [row[:] for row in array]
    for frame_color in colors:
        fill_color = next(color for color in colors if color != frame_color)
        frame_positions = [
            (r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == frame_color
        ]
        fill_positions = [
            (r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == fill_color
        ]
        if not len(frame_positions) or not len(fill_positions):
            continue
        top, left = min(r for r, _ in frame_positions), min(c for _, c in frame_positions)
        bottom, right = max(r for r, _ in frame_positions), max(c for _, c in frame_positions)
        fill_top, fill_left = min(r for r, _ in fill_positions), min(c for _, c in fill_positions)
        fill_bottom, fill_right = (
            max(r for r, _ in fill_positions),
            max(c for _, c in fill_positions),
        )
        if bottom <= top or right - left < 2:
            continue
        if not (
            all(array[r][left] == frame_color for r in range(top, bottom + 1))
            and all(array[r][right] == frame_color for r in range(top, bottom + 1))
            and all(array[bottom][c] == frame_color for c in range(left, right + 1))
            and (fill_left == left + 1)
            and (fill_right == right - 1)
            and (fill_bottom == bottom - 1)
            and all(
                array[r][c] == fill_color
                for r in range(fill_top, bottom)
                for c in range(left + 1, right)
            )
        ):
            continue
        clearance = fill_top - top
        spiral = ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (1, 1))
        if not 1 <= clearance <= len(spiral):
            continue
        output = [[0] * 3 for _ in range(3)]
        for row, col in spiral[:clearance]:
            output[row][col] = fill_color
        return output
    return [row[:] for row in array]


def solve(grid):
    return _encode_u_frame_clearance([row[:] for row in grid])
