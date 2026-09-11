def _crop_inside_monochrome_rectangle(array):
    for color in sorted({value for row in array for value in row}):
        positions = [
            (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == color
        ]
        if len(positions) < 8:
            continue
        top, left = min(r for r, _ in positions), min(c for _, c in positions)
        bottom, right = max(r for r, _ in positions), max(c for _, c in positions)
        if bottom - top < 2 or right - left < 2:
            continue
        perimeter = {
            *((top, col) for col in range(left, right + 1)),
            *((bottom, col) for col in range(left, right + 1)),
            *((row, left) for row in range(top, bottom + 1)),
            *((row, right) for row in range(top, bottom + 1)),
        }
        if {tuple(int(value) for value in point) for point in positions} == perimeter:
            return [row[left + 1 : right] for row in array[top + 1 : bottom]]
    return [row[:] for row in array]


def solve(grid):
    return _crop_inside_monochrome_rectangle(grid)
