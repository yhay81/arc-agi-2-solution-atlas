def _move_three_toward_four(array):
    three = [(r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == 3]
    four = [(r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == 4]
    if len(three) != 1 or len(four) != 1:
        return [row[:] for row in array]
    source, target = three[0], four[0]
    step = tuple((target[i] > source[i]) - (target[i] < source[i]) for i in range(2))
    destination = (source[0] + step[0], source[1] + step[1])
    output = [row[:] for row in array]
    output[source[0]][source[1]] = 0
    output[destination[0]][destination[1]] = 3
    return output


def solve(grid):
    return _move_three_toward_four(grid)
