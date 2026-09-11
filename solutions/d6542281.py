def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    seen = set()
    objects = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == background or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                r, c = stack.pop()
                cells.append((r, c))
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        rr, cc = r + dr, c + dc
                        if (
                            0 <= rr < height
                            and 0 <= cc < width
                            and grid[rr][cc] != background
                            and (rr, cc) not in seen
                        ):
                            seen.add((rr, cc))
                            stack.append((rr, cc))
            objects.append(cells)
    templates = [cells for cells in objects if len({grid[r][c] for r, c in cells}) > 1]
    output = [row[:] for row in grid]
    stamped = set()
    for template_index, template in enumerate(templates):
        colors = {grid[r][c] for r, c in template}
        color_counts = {color: sum(grid[r][c] == color for r, c in template) for color in colors}
        singles = [
            cells
            for cells in objects
            if cells is not template and len({grid[r][c] for r, c in cells}) == 1
        ]
        anchor_colors = {
            color
            for color, amount in color_counts.items()
            if any(
                grid[cells[0][0]][cells[0][1]] == color and len(cells) == amount
                for cells in singles
            )
        }
        anchors = [cell for cell in template if grid[cell[0]][cell[1]] in anchor_colors]
        nonanchors = [cell for cell in template if grid[cell[0]][cell[1]] not in anchor_colors]
        for anchor in anchors:
            color = grid[anchor[0]][anchor[1]]
            amount = color_counts[color]
            targets = [
                cell
                for cells in singles
                if grid[cells[0][0]][cells[0][1]] == color and len(cells) == amount
                for cell in cells
            ]
            for target in targets:
                dr, dc = target[0] - anchor[0], target[1] - anchor[1]
                shifted = [(r + dr, c + dc) for r, c in template]
                if any(r < 0 or r >= height or c < 0 or c >= width for r, c in shifted):
                    continue
                if any(grid[r + dr][c + dc] != grid[r][c] for r, c in anchors):
                    continue
                if not any(grid[r + dr][c + dc] == background for r, c in nonanchors):
                    continue
                stamped.add(template_index)
                for (r, c), (rr, cc) in zip(template, shifted):
                    output[rr][cc] = grid[r][c]
        if template_index in stamped:
            for r, c in nonanchors:
                if color_counts[grid[r][c]] == 1:
                    output[r][c] = background
    return output
