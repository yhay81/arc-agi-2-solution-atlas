def _move_frame_contents_to_opposite_outer_corners(array):
    h, w = len(array), len(array[0])
    frames: list[tuple[int, int, int, int, int]] = []
    for color in {v for row in array for v in row}:
        if color == 0:
            continue
        positions = [(r, c) for r in range(h) for c in range(w) if array[r][c] == color]
        top, left = min(r for r, _ in positions), min(c for _, c in positions)
        bottom, right = max(r for r, _ in positions), max(c for _, c in positions)
        if bottom - top < 2 or right - left < 2:
            continue
        if (
            all(array[top][c] == color for c in range(left, right + 1))
            and all(array[bottom][c] == color for c in range(left, right + 1))
            and all(array[r][left] == color for r in range(top, bottom + 1))
            and all(array[r][right] == color for r in range(top, bottom + 1))
        ):
            frames.append((top, left, bottom, right, color))
    if len(frames) != 1:
        return [row[:] for row in array]
    top, left, bottom, right, frame_color = frames[0]
    if top == 0 or left == 0 or bottom == h - 1 or right == w - 1:
        return [row[:] for row in array]
    center_row = (top + bottom) / 2
    center_col = (left + right) / 2
    output = [row[:] for row in array]
    for row in range(h):
        for col in range(w):
            if array[row][col] == 0 or array[row][col] == frame_color:
                continue
            if not (top < row < bottom and left < col < right):
                continue
            output[row][col] = 0
            target_row = bottom + 1 if row < center_row else top - 1
            target_col = right + 1 if col < center_col else left - 1
            output[target_row][target_col] = array[row][col]
    return output


def solve(grid):
    return _move_frame_contents_to_opposite_outer_corners([row[:] for row in grid])
