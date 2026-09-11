def _fill_numbered_frames(array):
    output = [row[:] for row in array]
    height, width = len(array), len(array[0])
    size_color = {5: 8, 7: 4, 9: 3}
    for top in range(height):
        for left in range(width):
            frame_color = array[top][left]
            if frame_color == 0:
                continue
            for size, fill_color in size_color.items():
                bottom, right = (top + size - 1, left + size - 1)
                if bottom >= height or right >= width:
                    continue
                if not all(array[top][col] == frame_color for col in range(left, right + 1)):
                    continue
                if not all(array[bottom][col] == frame_color for col in range(left, right + 1)):
                    continue
                if not all(array[row][left] == frame_color for row in range(top, bottom + 1)):
                    continue
                if not all(array[row][right] == frame_color for row in range(top, bottom + 1)):
                    continue
                for row in range(top + 1, bottom):
                    for col in range(left + 1, right):
                        if array[row][col] == 0:
                            output[row][col] = fill_color
    return output


def solve(grid):
    return _fill_numbered_frames(grid)
