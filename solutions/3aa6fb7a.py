def _complete_l_components(array):
    output = [row[:] for row in array]
    for row in range(len(array) - 1):
        for col in range(len(array[0]) - 1):
            block = [array[row + dr][col + dc] for dr in (0, 1) for dc in (0, 1)]
            if block.count(8) == 3 and block.count(0) == 1:
                missing = block.index(0)
                output[row + missing // 2][col + missing % 2] = 1
    return output


def solve(grid):
    return _complete_l_components(grid)
