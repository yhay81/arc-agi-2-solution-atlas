from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    seen = set()
    objects = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == background or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            component = []
            while stack:
                cr, cc = stack.pop()
                component.append((cr, cc))
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        point = (cr + dr, cc + dc)
                        if (
                            (dr or dc)
                            and 0 <= point[0] < h
                            and 0 <= point[1] < w
                            and grid[point[0]][point[1]] != background
                            and point not in seen
                        ):
                            seen.add(point)
                            stack.append(point)
            top, bottom = min(r for r, _ in component), max(r for r, _ in component)
            left, right = min(c for _, c in component), max(c for _, c in component)
            crop = [row[left : right + 1] for row in grid[top : bottom + 1]]
            objects.append((crop, {grid[r][c] for r, c in component}))
    motifs = [crop for crop, palette in objects if len(palette) > 1]
    masks = [crop for crop, palette in objects if len(palette) == 1]
    if len(motifs) != 1 or len(masks) != 1:
        return [row[:] for row in grid]
    motif, mask_crop = motifs[0], masks[0]
    mh, mw = len(motif), len(motif[0])
    mask = [[value != background for value in row] for row in mask_crop]
    output = [[background] * (len(mask[0]) * mw) for _ in range(len(mask) * mh)]
    for r in range(len(mask)):
        for c in range(len(mask[0])):
            if mask[r][c]:
                for dr in range(mh):
                    output[r * mh + dr][c * mw : c * mw + mw] = motif[dr][:]
    return output
