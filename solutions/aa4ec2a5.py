from collections import Counter


def components(cells: set[tuple[int, int]]) -> list[list[tuple[int, int]]]:
    result = []
    while cells:
        stack = [cells.pop()]
        part = []
        while stack:
            row, col = stack.pop()
            part.append((row, col))
            for rr, cc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if (rr, cc) in cells:
                    cells.remove((rr, cc))
                    stack.append((rr, cc))
        result.append(part)
    return result


def solve(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(cell for row in grid for cell in row).most_common(1)[0][0]
    output = [row[:] for row in grid]
    for component in components(
        {(row, col) for row in range(height) for col in range(width) if grid[row][col] == 1}
    ):
        cells = set(component)
        top, bottom = min(row for row, _ in component), max(row for row, _ in component)
        left, right = min(col for _, col in component), max(col for _, col in component)
        pending = {
            (row, col)
            for row in range(top, bottom + 1)
            for col in range(left, right + 1)
            if grid[row][col] == background
        }
        pockets = set()
        for pocket in components(pending):
            if not any(row in (top, bottom) or col in (left, right) for row, col in pocket):
                pockets.update(pocket)
        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                if (
                    grid[row][col] == background
                    and (row, col) not in pockets
                    and any(
                        (row + dr, col + dc) in cells
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                    )
                ):
                    output[row][col] = 2
        rows_to_cols = {}
        for row, col in component:
            rows_to_cols.setdefault(row, []).append(col)
        for row, columns in rows_to_cols.items():
            segments = []
            for col in sorted(columns):
                if not segments or col > segments[-1][1] + 1:
                    segments.append((col, col))
                else:
                    segments[-1] = (segments[-1][0], col)
            for start, end in segments:
                for col in (start - 1, end + 1):
                    if (
                        0 <= col < width
                        and grid[row][col] == background
                        and (row, col) not in pockets
                    ):
                        output[row][col] = 2
                for adjacent_row in (row - 1, row + 1):
                    if 0 <= adjacent_row < height:
                        for col in range(start - 1, end + 2):
                            if (
                                0 <= col < width
                                and grid[adjacent_row][col] == background
                                and (adjacent_row, col) not in pockets
                            ):
                                output[adjacent_row][col] = 2
        for row, col in cells:
            output[row][col] = 8 if pockets else 1
        for row, col in pockets:
            output[row][col] = 6
    return output
