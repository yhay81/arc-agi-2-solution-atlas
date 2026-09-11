from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]
    colours = sorted(value for value in counts if value != background)
    if len(colours) != 2:
        return [row[:] for row in grid]
    output = [[background] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] in colours:
                output[r][c] = colours[1 - colours.index(grid[r][c])]
    positions = [(r, c) for r in range(h) for c in range(w) if output[r][c] != background]
    if not positions:
        return output
    split = (min(r for r, _ in positions) + max(r for r, _ in positions)) // 2
    upper, lower = output[: split + 1], output[split + 1 :]

    def component_count(candidate):
        cells = {(r, c) for r in range(h) for c in range(w) if candidate[r][c] != background}
        count = 0
        while cells:
            seed = min(cells)
            cells.remove(seed)
            stack = [seed]
            count += 1
            while stack:
                r, c = stack.pop()
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        point = (r + dr, c + dc)
                        if point in cells:
                            cells.remove(point)
                            stack.append(point)
        return count

    candidate = upper + lower
    accepted = [row[:] for row in candidate]
    for _ in range(w):
        if component_count(candidate) != 1:
            break
        accepted = [row[:] for row in candidate]
        upper = [row[-1:] + row[:-1] for row in upper]
        candidate = upper + lower
    return accepted
