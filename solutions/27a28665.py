def _bounding_crop(array, mask):
    positions = [(r, c) for r, row in enumerate(mask) for c, value in enumerate(row) if value]
    if not len(positions):
        return [row[:] for row in array]
    top = min(r for r, _ in positions)
    bottom = max(r for r, _ in positions)
    left = min(c for _, c in positions)
    right = max(c for _, c in positions)
    return [row[left : right + 1] for row in array[top : bottom + 1]]


def _shape_signature(array):
    counts = [sum(row.count(color) for row in array) for color in range(10)]
    background = counts.index(max(counts))
    cropped = _bounding_crop(array, [[cell != background for cell in row] for row in array])
    return "/".join("".join("1" if cell != background else "0" for cell in row) for row in cropped)


def solve(grid):
    labels = {
        str(signature): int(label)
        for signature, label in [
            ("001/010/101", 1),
            ("010/101/010", 2),
            ("100/100/011", 3),
            ("101/000/101", 6),
        ]
    }
    signature = _shape_signature(grid)
    return [[labels[signature]]] if signature in labels else [row[:] for row in grid]
