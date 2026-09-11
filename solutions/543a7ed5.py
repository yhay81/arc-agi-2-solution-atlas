def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 6 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            component = []
            while stack:
                r, c = stack.pop()
                component.append((r, c))
                for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= rr < height
                        and 0 <= cc < width
                        and grid[rr][cc] == 6
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            top, left = min(r for r, _ in component), min(c for _, c in component)
            bottom, right = max(r for r, _ in component), max(c for _, c in component)
            region = [row[left : right + 1] for row in grid[top : bottom + 1]]
            background = {
                (r, c)
                for r in range(len(region))
                for c in range(len(region[0]))
                if region[r][c] == 8
            }
            outside = set()
            stack = [
                cell
                for cell in background
                if cell[0] in (0, len(region) - 1) or cell[1] in (0, len(region[0]) - 1)
            ]
            outside.update(stack)
            while stack:
                r, c = stack.pop()
                for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (rr, cc) in background and (rr, cc) not in outside:
                        outside.add((rr, cc))
                        stack.append((rr, cc))
            for r, c in background - outside:
                output[top + r][left + c] = 4
            frame = (
                [(top - 1, c) for c in range(left - 1, right + 2)]
                + [(bottom + 1, c) for c in range(left - 1, right + 2)]
                + [(r, left - 1) for r in range(top, bottom + 1)]
                + [(r, right + 1) for r in range(top, bottom + 1)]
            )
            for r, c in frame:
                if 0 <= r < height and 0 <= c < width and grid[r][c] == 8:
                    output[r][c] = 3
    return output
