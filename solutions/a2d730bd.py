def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    colors = set(counts) - {background}
    output = [row[:] for row in grid]
    components_by_color = {}
    for color in colors:
        seen = set()
        groups = []
        for row in range(height):
            for col in range(width):
                if grid[row][col] != color or (row, col) in seen:
                    continue
                stack = [(row, col)]
                seen.add((row, col))
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r, c))
                    for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if (
                            0 <= rr < height
                            and 0 <= cc < width
                            and grid[rr][cc] == color
                            and (rr, cc) not in seen
                        ):
                            seen.add((rr, cc))
                            stack.append((rr, cc))
                groups.append(cells)
        components_by_color[color] = groups
        main = max(groups, key=len)
        top = min(r for r, _ in main)
        left = min(c for _, c in main)
        bottom = max(r for r, _ in main)
        right = max(c for _, c in main)
        tall = bottom - top > right - left
        for cells in groups:
            if cells is main:
                continue
            for row, col in cells:
                if tall:
                    output[row][min(col, left) : max(col, right) + 1] = [color] * (
                        max(col, right) - min(col, left) + 1
                    )
                else:
                    for rr in range(min(row, top), max(row, bottom) + 1):
                        output[rr][col] = color
                for rr, cc in ((row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)):
                    if 0 <= rr < height and 0 <= cc < width:
                        output[rr][cc] = color
    for color, groups in components_by_color.items():
        main = max(groups, key=len)
        top = min(r for r, _ in main)
        left = min(c for _, c in main)
        bottom = max(r for r, _ in main)
        right = max(c for _, c in main)
        tall = bottom - top > right - left
        for cells in groups:
            if cells is main:
                continue
            for row, col in cells:
                output[row][col] = background
                if tall:
                    near = left - 1 if col < left else right + 1
                    for rr in (row - 1, row + 1):
                        if 0 <= rr < height and 0 <= near < width:
                            output[rr][near] = color
                else:
                    near = top - 1 if row < top else bottom + 1
                    for cc in (col - 1, col + 1):
                        if 0 <= near < height and 0 <= cc < width:
                            output[near][cc] = color
    return output
