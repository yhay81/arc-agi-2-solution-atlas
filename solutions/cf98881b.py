from itertools import pairwise, permutations


def _overlay_three_separated_panels(array):
    separators = [
        col
        for col in range(len(array[0]))
        if len({array[r][col] for r in range(len(array))}) == 1 and array[0][col] != 0
    ]
    candidates = [
        pair
        for pair in permutations(separators, 2)
        if pair[0] < pair[1]
        and pair[0] == pair[1] - pair[0] - 1
        and (pair[1] - pair[0] - 1 == len(array[0]) - pair[1] - 1)
    ]
    if len(candidates) != 1:
        return array.copy()
    edges = [-1, *candidates[0], len(array[0])]
    panels = [[row[left + 1 : right] for row in array] for left, right in pairwise(edges)]
    if len({(len(panel), len(panel[0])) for panel in panels}) != 1:
        return [row[:] for row in array]
    output = [[0] * len(panels[0][0]) for _ in panels[0]]
    for panel in panels:
        for r in range(len(output)):
            for c in range(len(output[0])):
                if output[r][c] == 0:
                    output[r][c] = panel[r][c]
    return output


def solve(grid):
    return _overlay_three_separated_panels(grid)
