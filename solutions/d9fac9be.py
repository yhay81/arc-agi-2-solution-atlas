def _center_of_hollow_square(array):
    centers: list[int] = []
    for top in range(len(array) - 2):
        for left in range(len(array[0]) - 2):
            window = [row[left : left + 3] for row in array[top : top + 3]]
            border = [*window[0], *window[2], window[1][0], window[1][2]]
            if len(set(border)) == 1 and border[0] != 0:
                center = window[1][1]
                if center != 0 and center != border[0]:
                    centers.append(center)
    if len(centers) != 1:
        return [row[:] for row in array]
    return [[centers[0]]]


def solve(grid):
    return _center_of_hollow_square(grid)
