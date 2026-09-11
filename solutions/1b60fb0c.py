def _complete_color_symmetry(array, mode, source_color, target_color):
    source = [[v == source_color for v in row] for row in array]
    h, w = len(array), len(array[0])
    rot = [row[::-1] for row in source[::-1]]
    lr = [row[::-1] for row in source]
    ud = source[::-1]
    if mode == "best":
        candidates = []
        if h == w:
            candidates.append([list(x) for x in zip(*source)])
        candidates.extend((rot, lr, ud))
        reflected = max(
            candidates,
            key=lambda x: sum(a and b for ra, rb in zip(x, source) for a, b in zip(ra, rb)),
        )
    elif mode == "diag":
        if h != w:
            return [row[:] for row in array]
        reflected = [list(x) for x in zip(*source)]
    elif mode == "rot180":
        reflected = rot
    elif mode == "lr":
        reflected = lr
    elif mode == "ud":
        reflected = ud
    else:
        return [row[:] for row in array]
    output = [row[:] for row in array]
    for r in range(h):
        for c in range(w):
            if reflected[r][c] and output[r][c] == 0:
                output[r][c] = target_color
    return output


def solve(grid):
    return _complete_color_symmetry(grid, "best", 1, 2)
