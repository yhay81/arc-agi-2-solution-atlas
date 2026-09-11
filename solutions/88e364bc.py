from collections import Counter


def solve(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    colors = {value for row in grid for value in row} - {background, 2, 4}

    def components(color):
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
        return groups

    directions = {}
    for color in colors:
        for cells in components(color):
            top, left = min(r for r, _ in cells), min(c for _, c in cells)
            bottom, right = max(r for r, _ in cells), max(c for _, c in cells)
            if bottom - top < 2 or right - left < 2:
                continue
            if (
                not all(grid[top][c] == color for c in range(left, right + 1))
                or not all(grid[bottom][c] == color for c in range(left, right + 1))
                or not all(grid[r][left] == color for r in range(top, bottom + 1))
                or not all(grid[r][right] == color for r in range(top, bottom + 1))
            ):
                continue
            inner = [grid[r][left + 1 : right] for r in range(top + 1, bottom)]
            if not all(value != background for row in inner for value in row) or not any(
                value == 2 for row in inner for value in row
            ):
                continue
            center = ((bottom - top) / 2, (right - left) / 2)
            marker = [
                (r - top, c - left)
                for r in range(top, bottom + 1)
                for c in range(left, right + 1)
                if grid[r][c] == 2
            ]
            marker_center = (
                sum(r for r, _ in marker) / len(marker),
                sum(c for _, c in marker) / len(marker),
            )
            directions[color] = (
                (marker_center[0] > center[0]) - (marker_center[0] < center[0]),
                (marker_center[1] > center[1]) - (marker_center[1] < center[1]),
            )
    if not (directions):
        raise ValueError("task assumptions are not satisfied")
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 4:
                continue
            found = []
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                rr, cc = row + dr, col + dc
                while 0 <= rr < height and 0 <= cc < width:
                    if grid[rr][cc] in directions:
                        found.append(grid[rr][cc])
                        break
                    rr += dr
                    cc += dc
            if not (found and len(set(found)) == 1):
                raise ValueError("task assumptions are not satisfied")
            color = found[0]
            dr, dc = directions[color]
            rr, cc = row, col
            while True:
                checks = [(rr + dr, cc + dc)]
                if dr and dc:
                    checks.extend(((rr + dr, cc), (rr, cc + dc)))
                if any(
                    not (0 <= r < height and 0 <= c < width) or grid[r][c] == color
                    for r, c in checks
                ):
                    break
                rr += dr
                cc += dc
            output[row][col] = background
            output[rr][cc] = 4
    return output
