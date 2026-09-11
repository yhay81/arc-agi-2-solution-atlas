def solve(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    components = []
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
                        and grid[rr][cc] != 0
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    blocks = [
        cells
        for cells in components
        if len(cells) == 4
        and max(r for r, _ in cells) - min(r for r, _ in cells) == 1
        and max(c for _, c in cells) - min(c for _, c in cells) == 1
    ]
    if len(blocks) != 1:
        return [row[:] for row in grid]
    block = set(blocks[0])
    if any(len(cells) != 1 for cells in components if set(cells) != block):
        return [row[:] for row in grid]
    top, bottom = min(r for r, _ in block), max(r for r, _ in block)
    left, right = min(c for _, c in block), max(c for _, c in block)
    output = [row[:] for row in grid]
    changed = False
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in block:
                continue
            if top <= row <= bottom and col < left:
                ray = [(row, c) for c in range(col + 1, left)]
            elif top <= row <= bottom and col > right:
                ray = [(row, c) for c in range(right + 1, col)]
            elif left <= col <= right and row < top:
                ray = [(r, col) for r in range(row + 1, top)]
            elif left <= col <= right and row > bottom:
                ray = [(r, col) for r in range(bottom + 1, row)]
            else:
                ray = []
            if any(output[r][c] != 0 for r, c in ray):
                return [row[:] for row in grid]
            for r, c in ray:
                output[r][c] = grid[row][col]
                changed = True
    return output if changed else [row[:] for row in grid]
