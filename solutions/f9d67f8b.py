def solve(grid):
    if not grid or not grid[0]:
        return [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    source = [row[:] for row in grid]

    def compatible_axis(axis, size, vertical):
        for offset in range(min(axis, size - axis)):
            first, second = axis - 1 - offset, axis + offset
            if vertical:
                for row in range(height):
                    left, right = source[row][first], source[row][second]
                    if left != 9 and right != 9 and left != right:
                        return False
            else:
                for col in range(width):
                    top, bottom = source[first][col], source[second][col]
                    if top != 9 and bottom != 9 and top != bottom:
                        return False
        return True

    def first_axis(size, vertical):
        valid = [axis for axis in range(1, size - 1) if compatible_axis(axis, size, vertical)]
        return min(valid, key=lambda axis: (abs(2 * axis - size), axis)) if valid else None

    output = [row[:] for row in source]
    vertical_axis = first_axis(width, True)
    horizontal_axis = first_axis(height, False)
    if vertical_axis is not None:
        for offset in range(min(vertical_axis, width - vertical_axis)):
            left_index, right_index = vertical_axis - 1 - offset, vertical_axis + offset
            for row in range(height):
                left, right = output[row][left_index], output[row][right_index]
                if left == 9:
                    output[row][left_index] = right
                if right == 9:
                    output[row][right_index] = left
    if horizontal_axis is not None:
        for offset in range(min(horizontal_axis, height - horizontal_axis)):
            top_index, bottom_index = horizontal_axis - 1 - offset, horizontal_axis + offset
            for col in range(width):
                top, bottom = output[top_index][col], output[bottom_index][col]
                if top == 9:
                    output[top_index][col] = bottom
                if bottom == 9:
                    output[bottom_index][col] = top
    remaining = [
        (row, col) for row in range(height) for col in range(width) if output[row][col] == 9
    ]
    if remaining and vertical_axis is not None:
        rows = {row for row, _ in remaining}
        minimum_column = min(col for _, col in remaining)
        if 0 in rows:
            if vertical_axis > width // 2:
                rotated = [
                    [output[height - 1 - col][row] for col in range(height)] for row in range(width)
                ]
            else:
                rotated = [
                    [output[col][width - 1 - row] for col in range(height)] for row in range(width)
                ]
            shift = width - vertical_axis - 3
            for row, col in remaining:
                rotated_column = col - minimum_column + shift
                if 0 <= row < len(rotated) and 0 <= rotated_column < len(rotated[row]):
                    output[row][col] = rotated[row][rotated_column]
        if height - 1 in rows:
            if vertical_axis > width // 2:
                rotated = [
                    [output[col][width - 1 - row] for col in range(height)] for row in range(width)
                ]
            else:
                rotated = [
                    [output[height - 1 - col][row] for col in range(height)] for row in range(width)
                ]
            shift = width - vertical_axis - 3
            for row, col in remaining:
                rotated_column = col - minimum_column + shift
                if 0 <= row < len(rotated) and 0 <= rotated_column < len(rotated[row]):
                    output[row][col] = rotated[row][rotated_column]
    return output
