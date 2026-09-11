from collections import Counter
from itertools import combinations


def components(grid, color):
    height, width = len(grid), len(grid[0])
    unseen = {(r, c) for r in range(height) for c in range(width) if grid[r][c] == color}
    result = []
    while unseen:
        start = unseen.pop()
        todo = [start]
        points = [start]
        while todo:
            r, c = todo.pop()
            for rr in range(max(0, r - 1), min(height, r + 2)):
                for cc in range(max(0, c - 1), min(width, c + 2)):
                    point = (rr, cc)
                    if point in unseen:
                        unseen.remove(point)
                        todo.append(point)
                        points.append(point)
        result.append(points)
    return result


def bounds(points):
    rows = [point[0] for point in points]
    cols = [point[1] for point in points]
    return min(rows), min(cols), max(rows), max(cols)


def solve(grid):
    a = grid
    bg = Counter(value for row in a for value in row).most_common(1)[0][0]
    solutions = []
    for color in {value for row in a for value in row} - {bg}:
        parts = components(a, color)
        centers = [
            (sum(r for r, _ in part) / len(part), sum(c for _, c in part) / len(part))
            for part in parts
        ]
        for inds in combinations(range(len(parts)), 4):
            boxes = [bounds(parts[i]) for i in inds]
            tops = sorted({box[0] for box in boxes})
            lefts = sorted({box[1] for box in boxes})
            if len(tops) != 2 or len(lefts) != 2:
                continue
            if {(box[0], box[1]) for box in boxes} != {(r, c) for r in tops for c in lefts}:
                continue
            if len({(box[2] - box[0], box[3] - box[1]) for box in boxes}) != 1:
                continue
            rmin = min(centers[i][0] for i in inds)
            rmax = max(centers[i][0] for i in inds)
            cmin = min(centers[i][1] for i in inds)
            cmax = max(centers[i][1] for i in inds)
            selected = set(inds)
            for i, part in enumerate(parts):
                if i in selected:
                    continue
                row, col = centers[i]
                if rmin < row < rmax and cmin < col < cmax:
                    top, left, bottom, right = bounds(part)
                    patch = [a[r][left : right + 1] for r in range(top, bottom + 1)]
                    solutions.append(((rmax - rmin) * (cmax - cmin), patch))
    if not (solutions):
        raise ValueError("task assumptions are not satisfied")
    return min(solutions, key=lambda item: item[0])[1]
