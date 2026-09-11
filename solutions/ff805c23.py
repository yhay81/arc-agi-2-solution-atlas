def _recover_rotationally_symmetric_patch(array):
    squares: list[tuple[int, int, int, int]] = []
    for color in {value for row in array for value in row if value != 0}:
        positions = [
            (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == color
        ]
        if not len(positions):
            continue
        rows, cols = zip(*positions)
        top, left, bottom, right = min(rows), min(cols), max(rows), max(cols)
        height, width = (bottom - top + 1, right - left + 1)
        if height >= 2 and height == width and (len(positions) == height * width):
            squares.append((top, left, bottom, right))
    if len(squares) != 1:
        return [row[:] for row in array]
    top, left, bottom, right = squares[0]
    reflected = [list(reversed(row)) for row in reversed(array)]
    return [row[left : right + 1] for row in reflected[top : bottom + 1]]


def solve(grid):
    return _recover_rotationally_symmetric_patch(grid)
