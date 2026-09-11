def solve(grid):
    source = [list(row) for row in grid]
    if not source or not source[0]:
        return source
    height, width = len(source), len(source[0])
    if any(len(row) != width for row in source):
        return source
    if {value for row in source for value in row} - {0, 5}:
        return source

    mask = [[False] * (width + 2) for _ in range(height + 2)]
    for row in range(height):
        for col in range(width):
            mask[row + 1][col + 1] = source[row][col] == 5
    output = [[0] * (width + 2) for _ in range(height + 2)]
    line_required = {(0, 1): 0, (1, 0): 0, (1, 1): 1, (1, 2): 0}
    line_target = {(1, 1), (2, 1), (3, 1)}
    block_required = {
        (0, 0): 0,
        (0, 1): 0,
        (0, 2): 0,
        (0, 3): 0,
        (1, 0): 0,
        (1, 1): 1,
        (1, 2): 1,
        (1, 3): 0,
        (2, 0): 0,
        (2, 1): 1,
        (2, 2): 1,
        (3, 0): 0,
        (3, 1): 0,
    }
    block_target = {(1, 1), (1, 2), (2, 1), (2, 2)}

    def rotated_stencils(required, target, size):
        stencils = []
        for _ in range(4):
            stencils.append((required, target))
            required = {(col, size - 1 - row): value for (row, col), value in required.items()}
            target = {(col, size - 1 - row) for row, col in target}
        return stencils

    def collect_matches(current, stencils):
        marks = set()
        for required, target in stencils:
            for row in range(len(current)):
                for col in range(len(current[0])):
                    if any(
                        not (
                            0 <= row + dr < len(current)
                            and 0 <= col + dc < len(current[0])
                            and current[row + dr][col + dc] == bool(value)
                        )
                        for (dr, dc), value in required.items()
                    ):
                        continue
                    cells = {(row + dr, col + dc) for dr, dc in target}
                    if all(
                        0 <= target_row < len(current)
                        and 0 <= target_col < len(current[0])
                        and current[target_row][target_col]
                        for target_row, target_col in cells
                    ):
                        marks.update(cells)
        return marks

    line_stencils = rotated_stencils(line_required, line_target, 3)
    block_stencils = rotated_stencils(block_required, block_target, 4)
    for _ in range(max(height, width) ** 2):
        block_marks = collect_matches(mask, block_stencils)
        line_mask = [row[:] for row in mask]
        for row, col in block_marks:
            line_mask[row][col] = False
        line_marks = collect_matches(line_mask, line_stencils)
        marks = block_marks | line_marks
        if not marks:
            break
        for row, col in block_marks:
            output[row][col] = 8
        for row, col in line_marks:
            output[row][col] = 2
        for row, col in marks:
            mask[row][col] = False
    return [row[1:-1] for row in output[1:-1]]
