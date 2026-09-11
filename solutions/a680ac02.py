def solve(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    blocks = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in seen:
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
                        and grid[rr][cc]
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            top, left = min(r for r, _ in cells), min(c for _, c in cells)
            bottom, right = max(r for r, _ in cells), max(c for _, c in cells)
            block_height, block_width = bottom - top + 1, right - left + 1
            if len(cells) >= block_height * block_width or block_height < 2 or block_width < 2:
                continue
            region = [line[left : right + 1] for line in grid[top : bottom + 1]]
            values = {value for line in region for value in line if value != 0}
            if len(values) == 1 and sum(value != 0 for line in region for value in line) == len(
                cells
            ):
                blocks.append((top, left, region))
    if not blocks:
        return [row[:] for row in grid]
    vertical = max(top for top, _, _ in blocks) - min(top for top, _, _ in blocks) > max(
        left for _, left, _ in blocks
    ) - min(left for _, left, _ in blocks)
    blocks.sort(key=lambda item: (item[0], item[1]) if vertical else (item[1], item[0]))
    if vertical:
        output = [
            [0] * max(len(block[0]) for _, _, block in blocks)
            for _ in range(sum(len(block) for _, _, block in blocks))
        ]
        row = 0
        for _, _, block in blocks:
            for r, line in enumerate(block):
                output[row + r][: len(line)] = line
            row += len(block)
    else:
        output = [
            [0] * sum(len(block[0]) for _, _, block in blocks)
            for _ in range(max(len(block) for _, _, block in blocks))
        ]
        col = 0
        for _, _, block in blocks:
            for r, line in enumerate(block):
                output[r][col : col + len(line)] = line
            col += len(block[0])
    return output
