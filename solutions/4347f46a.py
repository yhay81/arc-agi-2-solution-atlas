def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for color in sorted({value for row in grid for value in row if value}):
        seen = set()
        for r in range(height):
            for c in range(width):
                if grid[r][c] != color or (r, c) in seen:
                    continue
                stack = [(r, c)]
                seen.add((r, c))
                component = []
                while stack:
                    cr, cc = stack.pop()
                    component.append((cr, cc))
                    for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
                        if (
                            0 <= nr < height
                            and 0 <= nc < width
                            and grid[nr][nc] == color
                            and (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                if len(component) < 4:
                    continue
                rows = [row for row, _ in component]
                cols = [col for _, col in component]
                top, bottom, left, right = (min(rows), max(rows), min(cols), max(cols))
                box_height, box_width = (bottom - top + 1, right - left + 1)
                if len(component) != box_height * box_width or box_height < 2 or box_width < 2:
                    continue
                for row, col in component:
                    if top < row < bottom and left < col < right:
                        output[row][col] = 0
    return output
