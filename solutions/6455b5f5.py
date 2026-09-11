from collections import Counter


def solve(grid):
    if not grid or not grid[0]:
        return [row[:] for row in grid]
    h, w = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = next(value for value in counts if counts[value] == max(counts.values()))
    seen = set()
    regions = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != background or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            region = []
            while stack:
                cr, cc = stack.pop()
                region.append((cr, cc))
                for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
                    if (
                        0 <= nr < h
                        and 0 <= nc < w
                        and grid[nr][nc] == background
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            regions.append(region)
    if not regions:
        return [row[:] for row in grid]
    sizes = [len(region) for region in regions]
    largest, smallest = (max(sizes), min(sizes))
    output = [row[:] for row in grid]
    for region, size in zip(regions, sizes, strict=True):
        color = 1 if size == largest else 8 if size == smallest else None
        if color is None:
            continue
        for row, col in region:
            output[row][col] = color
    return output
