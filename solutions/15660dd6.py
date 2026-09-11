def solve(grid):
    grid = [list(row) for row in grid]
    width = len(grid[0])
    frame_size = None
    for size in range(3, 15):
        region = grid[1 : 1 + size]
        if len(region) != size or any(len(row) < size for row in region):
            continue
        if all(
            grid[1][1 + col] == 1
            and grid[size][1 + col] == 1
            and grid[1 + row][1] == 1
            and grid[1 + row][size] == 1
            for row in range(size)
            for col in range(size)
            if row in (0, size - 1) or col in (0, size - 1)
        ):
            frame_size = size
            break
    if frame_size is None:
        return [row[:] for row in grid]

    groups = (width - 1) // (frame_size + 1)
    base = {8, 1, 2}
    fills = set()
    for group in range(groups):
        left = 1 + group * (frame_size + 1)
        for row in range(3):
            top = 1 + row * (frame_size + 1)
            interior = [
                grid[top + r][left + c]
                for r in range(1, frame_size - 1)
                for c in range(1, frame_size - 1)
            ]
            if interior and len(set(interior)) == 1 and interior[0] not in base:
                fills.add(interior[0])

    output = [[8] * (groups * (frame_size + 1) - 1) for _ in range(frame_size)]
    for group in range(groups):
        left = 1 + group * (frame_size + 1)
        filled = shape = filled_row = None
        for row in range(3):
            top = 1 + row * (frame_size + 1)
            interior = [
                grid[top + r][left + c]
                for r in range(1, frame_size - 1)
                for c in range(1, frame_size - 1)
            ]
            if len(set(interior)) == 1 and interior[0] in fills:
                filled, filled_row = interior[0], row
            elif 2 in interior:
                shape = interior
        if filled is None or shape is None:
            continue
        output_left = group * (frame_size + 1)
        border = [grid[1][0], grid[frame_size + 2][0], grid[2 * (frame_size + 1) + 1][0]][
            filled_row
        ]
        for r in range(frame_size):
            for c in range(frame_size):
                if r in (0, frame_size - 1) or c in (0, frame_size - 1):
                    output[r][output_left + c] = border
        for index, value in enumerate(shape):
            r, c = divmod(index, frame_size - 2)
            output[r + 1][output_left + c + 1] = filled if value == 2 else 8
    return output
