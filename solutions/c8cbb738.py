def _overlay_color_bboxes_centered(array):
    counts = {}
    for row in array:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    values = sorted(counts)
    if not len(values):
        return [row[:] for row in array]
    background = max(values, key=counts.get)
    boxes = []
    for color in values:
        if color == background:
            continue
        positions = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v == color]
        if not len(positions):
            continue
        top, left = min(r for r, c in positions), min(c for r, c in positions)
        bottom, right = max(r for r, c in positions), max(c for r, c in positions)
        boxes.append(
            (
                color,
                [
                    [array[r][c] == color for c in range(left, right + 1)]
                    for r in range(top, bottom + 1)
                ],
            )
        )
    if not boxes:
        return [row[:] for row in array]
    size = max(max(len(mask), len(mask[0])) for _, mask in boxes)
    output = [[background] * size for _ in range(size)]
    for color, mask in boxes:
        row = (size - len(mask)) // 2
        col = (size - len(mask[0])) // 2
        for r, mrow in enumerate(mask):
            for c, flag in enumerate(mrow):
                if flag:
                    output[row + r][col + c] = color
    return output


def solve(grid):
    return _overlay_color_bboxes_centered(grid)
