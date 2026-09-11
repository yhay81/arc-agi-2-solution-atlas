class Matrix(list):
    @property
    def shape(self):
        return (len(self), len(self[0]))

    def __getitem__(self, key):
        return (
            super().__getitem__(key[0])[key[1]]
            if isinstance(key, tuple)
            else super().__getitem__(key)
        )

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            super().__getitem__(key[0])[key[1]] = value
        else:
            super().__setitem__(key, value)

    def copy(self):
        return Matrix(row[:] for row in self)

    def tolist(self):
        return [row[:] for row in self]


def solve(grid):
    grid = Matrix(row[:] for row in grid)
    taskvars = {"block_color": 5, "fill_color": 2, "extra_color": 1}
    block_color = taskvars["block_color"]
    fill_color = taskvars["fill_color"]
    extra_color = taskvars["extra_color"]
    output_grid = grid.copy()
    rows, cols = grid.shape
    block_positions = []
    for r in range(rows - 1):
        for c in range(cols - 1):
            if (
                grid[r, c] == block_color
                and grid[r, c + 1] == block_color
                and (grid[r + 1, c] == block_color)
                and (grid[r + 1, c + 1] == block_color)
            ):
                block_positions.append((r, c))
    if len(block_positions) < 2:
        return output_grid.tolist()
    block_top_rows = sorted(list(set((r for r, c in block_positions))))
    block_left_cols = sorted(list(set((c for r, c in block_positions))))
    rows_to_fill_completely = set()
    cols_to_fill_completely = set()
    for i in range(len(block_top_rows) - 1):
        current_block_bottom = block_top_rows[i] + 1
        next_block_top = block_top_rows[i + 1]
        for r in range(current_block_bottom + 1, next_block_top):
            left_bound = min(block_left_cols)
            right_bound = max(block_left_cols) + 1
            for c in range(left_bound, right_bound + 1):
                if c < cols and output_grid[r, c] == 0:
                    output_grid[r, c] = fill_color
            rows_to_fill_completely.add(r)
    for i in range(len(block_left_cols) - 1):
        current_block_right = block_left_cols[i] + 1
        next_block_left = block_left_cols[i + 1]
        for c in range(current_block_right + 1, next_block_left):
            top_bound = min(block_top_rows)
            bottom_bound = max(block_top_rows) + 1
            for r in range(top_bound, bottom_bound + 1):
                if r < rows and output_grid[r, c] == 0:
                    output_grid[r, c] = fill_color
            cols_to_fill_completely.add(c)
    for r in rows_to_fill_completely:
        for c in range(cols):
            if output_grid[r, c] == 0:
                output_grid[r, c] = extra_color
    for c in cols_to_fill_completely:
        for r in range(rows):
            if output_grid[r, c] == 0:
                output_grid[r, c] = extra_color
    return output_grid.tolist()
