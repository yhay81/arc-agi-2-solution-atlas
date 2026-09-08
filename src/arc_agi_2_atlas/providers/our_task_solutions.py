import numpy as np


def verify_solution_outputs(task, split, solve_fn):
    """
    Check whether a solution function produces correct outputs for all pairs in a split.

    Args:
        task (dict): Dictionary containing 'train' and 'test' grids.
        split (str): 'train' or 'test'.
        solve_fn (callable): Function that transforms an input grid.

    Returns:
        bool: True if outputs match on every pair, False otherwise.
    """
    for pair in task[split]:
        input_grid = np.array(pair["input"])
        true_output = np.array(pair["output"])
        if not np.array_equal(solve_fn(input_grid), true_output):
            return False
    return True


def solve_c9e6f938(input_grid):
    """
    Concepts: mirror reflection right, append, concatenate

    Transformation steps:
    1. Compute the mirror image of the input grid (flip horizontally).
    2. Concatenate the mirror image to the original grid on the right side.
    """
    input_grid = np.array(input_grid)
    # Step 1: Compute the mirror image of the input grid
    mirror = np.fliplr(input_grid)
    # Step 2: Concatenate the mirror image to the original grid on the right side
    output_grid = np.concatenate([input_grid, mirror], axis=1)
    return output_grid


def solve_0520fde7(input_grid):
    """
    Concepts: symmetry, AND gate, scalar multiplication

    Trasformation steps:
    step 1. Identify columns with the value 5. That column devide the grid into two equal size parts.
    step 2. xor the left and right parts of the grid.
    step 3. multiply it by 2
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Find the column with 5s (the axis)
    col_with_5 = None
    for i in range(ncols):
        if np.array_equal(input_grid[:, i], 5 * np.ones(nrows)):
            col_with_5 = i
            break

    # Step 2a: Split grid into left and right parts
    left = input_grid[:, :col_with_5]
    right = input_grid[:, col_with_5 + 1 :]

    # Step 2b: AND the left and right parts
    and_result = np.bitwise_and(left, right)

    # Step 3: Multiply by 2
    output_grid = and_result * 2

    return output_grid


def solve_c8f0f002(input_grid):
    """
    Concepts: replace specific color or value in a grid.

    Transformation steps:
    1. Replace every occurrence of 7 with 5 in the input grid.
    """
    input_grid = np.array(input_grid)
    # Step 1. Replace 7 with 5
    output_grid = np.where(input_grid == 7, 5, input_grid)
    return output_grid


def solve_b1948b0a(input_grid):
    """
    Concepts: replace specific color or value in a grid.

    Transformation steps:
    1. Replace every occurrence of 6 with 2 in the input grid.
    """
    input_grid = np.array(input_grid)
    # Step 1. Replace 6 with 2
    output_grid = np.where(input_grid == 6, 2, input_grid)
    return output_grid


def solve_3618c87e(input_grid):
    """
    Concepts: bring certain value or color down, gravity effect, column-wise transformation

    Transformation steps:
    1. Find all positions of 1s
    2. For each position, clear the original position by replacing 1 with 0.
    3. Place a 1 at the bottom of its column.
    4. All other values remain unchanged.
    """
    input_grid = np.array(input_grid)

    output_grid = input_grid.copy()
    nrows, _ = output_grid.shape

    rows, cols = np.where(output_grid == 1)  # Step 1. Find all positions of 1s
    for r, c in zip(rows, cols):
        output_grid[r, c] = 0  # Step 2. Replece 1 with 0 to clear its original position
        output_grid[nrows - 1, c] = 1  # Step 3. Place 1 at the bottom of its column
    return output_grid


def solve_a79310a0(input_grid):
    """
    Concepts: cyclic shift, value replacement

    Transformation steps:
    1. Cyclically shifts all rows downward by one (last row wraps to top).
    2. Replace all occurrences of the marked value (8) with a new value (2).
    """

    shifted_grid = np.vstack(
        [input_grid[-1:], input_grid[:-1]]
    )  # Step1. Shift last row to the top and move others down
    output_grid = np.where(
        shifted_grid == 8, 2, shifted_grid
    )  # Step2. Replace all occurrences of 8 with 2
    return output_grid


def solve_be03b35f(input_grid):
    """
    Concepts: 2x2 grid extraction, 2D 90 degree rotation, pattern matching

    Transformation steps:
    1. Extract 2x2 grids from three corners: top-left, top-right, and bottom-left
    2. Select TL as the base and generate its 90, 180, and 270 degree rotations
    3. Find which rotations match TR and BL
    4. The unmatched rotation is the output
    """
    input_grid = np.array(input_grid)

    # Step 1: Extract 2x2 corners
    top_left = input_grid[0:2, 0:2]
    top_right = input_grid[0:2, 3:5]
    bottom_left = input_grid[3:5, 0:2]
    two_corners = [top_right, bottom_left]

    # Step 2: Generate all rotations of TL
    rotations = [np.rot90(top_left, k) for k in [1, 2, 3]]

    # Step 3: Identify which rotation is NOT in [TR, BL]
    for rot in rotations:
        if not any(np.array_equal(rot, c) for c in two_corners):
            output_grid = rot
            break

    return output_grid


def solve_8be77c9e(input_grid):
    """
    Concepts: mirror reflection down, append, concatenate

    True Transformation steps:
    1. Compute the mirror image of the input grid (flip horizontally).
    2. Concatenate the mirror image to the original grid on the right side.
    """
    input_grid = np.array(input_grid)
    # Step 1: Compute the mirror image of the input grid
    mirror = np.flipud(input_grid)
    # Step 2: Concatenate the mirror image to the original grid on the down side
    output_grid = np.concatenate([input_grid, mirror], axis=0)
    return output_grid


def solve_a85d4709(input_grid):
    """
    Concepts: find positions, mapping, replace values or colors, column and row operation

    Transformation steps:
    1. Find all positions of marked number 5
    2. create a mapping from column index to value
    3. Replece each row with the corresponding value based on column index
    """
    output_grid = np.zeros_like(input_grid)

    rows, cols = np.where(input_grid == 5)  # Step 1. Find all positions of marked number 5
    col_to_value = {0: 2, 1: 4, 2: 3}  # Step 2. create a mapping from column index to value
    for r, c in zip(rows, cols):
        output_grid[r, :] = col_to_value.get(
            c, 0
        )  # Step 3. Replece each row with the corresponding value based on column index
    return output_grid


def solve_44f52bb0(input_grid):
    """
    Concepts: symmetry detection

    Transformation steps:
    1. Flip the input grid horizontally.
    2. Check if the input grid is symmetric (equal to its flipped version).
    3. If symmetric, output a single cell grid with value 1.
    4. If not symmetric, output a single cell grid with value 7.
    """

    flipped_input = np.fliplr(input_grid)  # Step 1: Flip the input grid horizontally
    symmery_check = np.all(
        input_grid == flipped_input
    )  # Step 2: Check if the input grid is symmetric
    if symmery_check:
        output_grid = [[1]]  # Step 3: If symmetric, output a single cell grid with value 1
    else:
        output_grid = [[7]]  # Step 4: If not symmetric, output a single cell grid with value 7

    return output_grid


def solve_94f9d214(input_grid):
    """
    Concepts: combining halves of a grid, conditional value replacement

    Transformation steps:
    1. Get the top and bottom halves of the input grid.
    2. Add the two halves together element-wise.
    3. In the added grid, find all positions where the value is 0.
    4. Set those positions to 2 in the output grid.
    """
    input_grid = np.array(input_grid)
    nrow, ncol = input_grid.shape

    # Step 1: Split into top and bottom halves
    top_half = input_grid[: nrow // 2, :]
    bottom_half = input_grid[nrow // 2 :, :]

    # Step 3: Add the two halves together
    added = top_half + bottom_half

    output_grid = np.zeros_like(added)  # initialize output grid with zeros

    # Step 4: In the added grid, find all positions where the value is 0.
    # Set those positions to 2 in the output grid.
    output_grid[added == 0] = 2

    return output_grid


def solve_bdad9b1f(input_grid):
    """
    Concepts: finding marked values in a grid, conditional value replacement

    Transformation steps:
    1. Get the positions of two marked values in the input grid.
    2. Set all rows with the first marked value to that value.
    3. Set all columns with the second marked value to that value.
    4. Set the intersection of those rows and columns to a specific value (4).
    """
    # oberve two type of marked values in the input grid
    marked_value1, marked_value2 = 2, 8

    # Step 1: Get the positions of the marked values
    rows1, _ = np.where(input_grid == marked_value1)
    _, cols2 = np.where(input_grid == marked_value2)

    output_grid = np.zeros_like(input_grid)  # Initialize output grid with zeros
    output_grid[rows1, :] = (
        marked_value1  # Step 2: Set all rows with the first marked value to that value.
    )
    output_grid[:, cols2] = (
        marked_value2  # Step 3: Set all columns with the second marked value to that value.
    )

    output_grid[rows1, cols2] = (
        4  # Step 4: Set the intersection of marked_value1 rows and marked_value2 columns to 4
    )

    return output_grid


def solve_25ff71a9(input_grid):
    """
    Concepts: move all value or color down by one row, gravity effect, row-wise transformation

    Transformation steps:
    1. Move all rows down by one and wrap around the last row to the first row.

    """
    input_grid = np.array(input_grid)

    # Step 1: Move all rows down by one and wrap around the last row to the first row.
    output_grid = np.vstack([input_grid[-1:], input_grid[:-1]])

    return output_grid


def solve_99b1bc43(input_grid):
    """
    Concepts: axis (row) to devide grid in two halves, Two halves of a grid around an axis, Double controlled gate logic using two halves of a grid split by a row containing '4'.

    Transformation steps:
    1. Find the row containing the value 4; this acts as the axis to split the grid.
    2. Split the grid into top_half (above the axis) and bottom_half (below the axis).
    3. For each cell in the top_half, pair it with the corresponding cell in the bottom_half.
    4. Use a mapping to determine the output value for each cell based on the pair:
       - (0, 0) -> 0
       - (0, 2) -> 3
       - (1, 0) -> 3
       - (1, 2) -> 0
    5. Construct the output grid using these mapped values.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Find the row with 4s (the axis)
    row_with_4 = None
    for i in range(nrows):
        if np.array_equal(input_grid[i, :], 4 * np.ones(ncols)):
            row_with_4 = i
            break

    top_half = input_grid[:row_with_4]  # Step 2: Get the top half above the axis
    bottom_half = input_grid[row_with_4 + 1 :]  # Step 2: Get the bottom half below the axis
    nrows, ncols = top_half.shape

    # Step 3 and 4: Mapping for output values based on paired cells
    value_map = {(0, 0): 0, (0, 2): 3, (1, 0): 3, (1, 2): 0}
    output_grid = np.zeros_like(top_half, dtype=int)

    for r in range(nrows):
        for c in range(ncols):  # Step 5: Construct the output grid using the mapping
            output_grid[r, c] = value_map[(top_half[r, c], bottom_half[r, c])]

    return output_grid


def solve_017c7c7b(input_grid):
    """
    Concepts: Pattern matching and continuation, index finding, and grid block appending.

    Transformation steps:
    1. Identify the starting row index by locating the first block of two consecutive rows in the input grid that exactly matches the last two rows of the grid.
    2. From this index, select the next three rows and append them to the bottom of the original grid.
    3. Multiply every value in the resulting grid by 2, so that all 1s become 2 and all 0s remain 0.
    """
    input_grid = np.array(input_grid)
    nrows, _ = input_grid.shape

    num_extra_rows = 3
    last_two_rows = input_grid[-2:, :]
    # Step 1: Find the index of the first block of two consecutive rows that matches the last two rows
    marked_idx = None
    for i in range(nrows - 2):
        block = input_grid[i : i + 2, :]
        if np.all(block == last_two_rows):
            marked_idx = i + 2
            break

    # Step 2: Append the next three rows after the matched block to the bottom of the grid
    extra_rows = input_grid[marked_idx : marked_idx + num_extra_rows, :]
    output_grid = np.vstack([input_grid, extra_rows])

    # Step 3: Scale all values by 2
    output_grid = 2 * output_grid

    return output_grid


def solve_49d1d64f(input_grid):
    """
    Concepts: Padding a border around the input grid.

    Transformation steps:
    1. Create a new grid with zeros of size (nrows + 2, ncols + 2).
    2. Copy the input grid into the center of the new grid.
    3. Replicate the first row of the input grid to the top border and the last row to the bottom border.
    4. Replicate the first column of the input grid to the left border and the last column to the right border.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    # Step 1: Initalize the output grid with zeros of size (nrows + 2, ncols + 2)
    output_grid = np.zeros((nrows + 2, ncols + 2), dtype=int)

    # Step 2: Copy the input grid into the center of the output grid
    output_grid[1 : nrows + 1, 1 : ncols + 1] = input_grid

    # Step 3: Add Top and bottom borders from the input grid
    output_grid[0, 1 : ncols + 1] = input_grid[0]
    output_grid[nrows + 1, 1 : ncols + 1] = input_grid[-1]

    # Step 4: Add Left and right borders from the input grid
    output_grid[1 : nrows + 1, 0] = input_grid[:, 0]
    output_grid[1 : nrows + 1, ncols + 1] = input_grid[:, -1]

    return output_grid


def solve_ed36ccf7(input_grid):
    """
    Concepts: grid rotation.

    Transformation steps:
    1. Rotates the input grid by 90 degrees counter clockwise.
    """
    input_grid = np.array(input_grid)

    # Step 1: Rotate the input grid by 90 degrees counter clockwise
    output_grid = np.rot90(input_grid, k=1)

    return output_grid


def solve_aedd82e4(input_grid):
    """
    Concepts: conditional change of grid cells based on neighbors, value replacement

    Transformation steps:
    1. Check if a cell in the input grid is 2.
    2. If it is, check its four neighbors (up, down, left, right).
    3. If all neighbors are 0, change the cell to 1.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    nrows, ncols = input_grid.shape

    for i in range(nrows):
        for j in range(ncols):
            if input_grid[i][j] != 2:  # Step 1: Check if the cell is 2
                continue

            neighbors = []  # Step 2: Collect neighbors
            if i > 0:
                neighbors.append(input_grid[i - 1][j])
            if i < nrows - 1:
                neighbors.append(input_grid[i + 1][j])
            if j > 0:
                neighbors.append(input_grid[i][j - 1])
            if j < ncols - 1:
                neighbors.append(input_grid[i][j + 1])

            if all(n == 0 for n in neighbors):  # Step 3: Check if all neighbors are 0
                output_grid[i][j] = 1  # Step 3: Change the cell to 1 if condition is met

    return output_grid


def solve_e9afcf9a(input_grid):
    """
    Concepts: even odd, row swap

    Transformation steps:
    1. For each odd column (0-based: index 1, 3, 5, ...) Swap row 0 and row 1.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    ncols = input_grid.shape[1]
    # Step 1: For each odd column (0-based: index 1, 3, 5, ...) Swap row 0 and row 1
    for j in range(ncols):
        if j % 2 == 1:
            output_grid[0, j], output_grid[1, j] = output_grid[1, j], output_grid[0, j]

    return output_grid


def solve_6430c8c4(input_grid):
    """
    Concepts: axis (row) to devide grid in two halves, Two halves of a grid around an axis, addition, conditional replacement

    Transformation steps:
    1. Find the row containing the value 4; this acts as the axis to split the grid.
    2. Split the grid into top_half (above the axis) and bottom_half (below the axis).
    3. Add the two halves together
    4. Find the indices where the addition results in 0.
    5. Replace those indices in the output grid with 3.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Find the row with 4s (the axis)
    row_with_4 = None
    for i in range(nrows):
        if np.array_equal(input_grid[i, :], 4 * np.ones(ncols)):
            row_with_4 = i
            break

    top_half = input_grid[:row_with_4]  # Step 2: Get the top half above the axis
    bottom_half = input_grid[row_with_4 + 1 :]  # Step 2: Get the bottom half below the axis

    # Step 3: Add the two halves together
    added = top_half + bottom_half

    # Step 4: Fine the indices where the addition results in 0
    rows, cols = np.where(added == 0)

    output_grid = np.zeros_like(top_half, dtype=int)  # Initialize output grid with zeros
    for r, c in zip(rows, cols):  #  Step 5: replace those indices with 3
        output_grid[r, c] = 3

    return output_grid


def solve_d631b094(input_grid):
    """
    Concepts: Find and produce non-zero values in a grid.

    Transformation steps:
    1. Dig out all non-zero values from the input grid.
    """
    input_grid = np.array(input_grid)
    # Step 1: Flatten the grid and filter out zeros
    output_grid = input_grid[input_grid != 0].reshape(1, -1)

    return output_grid


def solve_6d0aefbc(input_grid):
    """
    Concepts: mirror reflection right, append, concatenate

    Transformation steps:
    1. Compute the mirror image of the input grid (flip horizontally).
    2. Concatenate the mirror image to the original grid on the right side.
    """
    input_grid = np.array(input_grid)
    # Step 1: Compute the mirror image of the input grid
    mirror = np.fliplr(input_grid)
    # Step 2: Concatenate the mirror image to the original grid on the right side
    output_grid = np.concatenate([input_grid, mirror], axis=1)

    return output_grid


def solve_ed98d772(input_grid):
    """
    Concepts: Rotate grid, concatenate or stack grids

    Transformation steps:
    1. Generate the 90-degree, 180-degree, 270-degree rotated versions of the input grid.
    2. Concatenate the original grid with the 90-degree rotated version (the top half)
    3. Concatenate the 180-degree rotated version with the 270-degree rotated version (the bottom half).
    4. Concatenate the top and bottom halves to form the final output grid.
    """
    input_grid = np.array(input_grid)

    rotate_90_cc = np.rot90(
        input_grid, k=1
    )  # Step 1: Rotate the input grid 90 degrees counterclockwise
    rotate_180_cc = np.rot90(
        input_grid, k=2
    )  # Step 1: Rotate the input grid 180 degrees counterclockwise
    rotate_270_cc = np.rot90(
        input_grid, k=3
    )  # Step 1: Rotate the input grid 270 degrees counterclockwise

    # Step 2: Concatenate the original grid with the 90-degree rotated version
    top_half = np.hstack([input_grid, rotate_90_cc])
    bottom_half = np.hstack([rotate_180_cc, rotate_270_cc])
    output_grid = np.vstack([top_half, bottom_half])

    return output_grid


def solve_46442a0e(input_grid):
    """
    Concepts: Rotate grid, concatenate or stack grids

    Transformation steps:
    1. Generate the 90-degree, 180-degree, 270-degree rotated versions of the input grid.
    2. Concatenate the original grid with the 90-degree rotated version (the top half)
    3. Concatenate the 270-degree rotated version with the 180-degree rotated version (the bottom half).
    4. Concatenate the top and bottom halves to form the final output grid.
    """
    input_grid = np.array(input_grid)

    rotate_90_c = np.rot90(input_grid, k=-1)  # Step 1: Rotate the input grid 90 degrees clockwise
    rotate_180_c = np.rot90(input_grid, k=-2)  # Step 1: Rotate the input grid 180 degrees clockwise
    rotate_270_c = np.rot90(input_grid, k=-3)  # Step 1: Rotate the input grid 270 degrees clockwise

    # Step 2: Concatenate the original grid with the 90-degree rotated version
    top_half = np.hstack([input_grid, rotate_90_c])
    # Step 3: Concatenate the 270-degree rotated version with the 180-degree rotated version
    bottom_half = np.hstack([rotate_270_c, rotate_180_c])
    # Step 4: Concatenate the top and bottom halves to form the final output grid
    output_grid = np.vstack([top_half, bottom_half])

    return output_grid


def solve_6e02f1e3(input_grid):
    """
    Concepts: unique values, diagonal, anti-diagonal, fill values

    Transformation steps:
    1. Identify unique values in the input grid.
    2. Based on the number of unique values, apply different transformations:
       - If only one unique value, fill the top row of the output grid with 5
       - If two unique values, fill the diagonal of the output grid with 5
       - If three unique values, fill the anti-diagonal of the output grid with 5
       - If more than three unique values, raise an error (unexpected case)
    """
    input_grid = np.array(input_grid)
    unique_vals = np.unique(input_grid)  # Step 1: Identify unique values in the grid
    nrows = input_grid.shape[0]

    output_grid = np.zeros_like(input_grid)

    if (
        len(unique_vals) == 1
    ):  # Step 2: If only one unique value, fill the top row of output grid with 5
        output_grid[0] = 5
    elif (
        len(unique_vals) == 2
    ):  # Step 2: If only two unique value, fill the diagonal of output grid with 5
        for i in range(nrows):
            output_grid[i][i] = 5
    elif (
        len(unique_vals) == 3
    ):  # Step 2: If three unique values, fill the anti-diagonal of output grid with 5
        for i in range(nrows):
            output_grid[i][nrows - 1 - i] = 5
    else:
        raise ValueError("Unexpected number of unique values in the grid.")

    return output_grid


def solve_f76d97a5(input_grid):
    """
    Concepts: unique values, value swapping, conditional masking

    Transformation steps:
    1. Identify the unique values in the grid. One of the values is always 5, and the other is the "other" value.
    2. Replace all occurrences of 5 with the other value.
    3. Replace all occurrences of the other value with 0.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Step 1: Identify unique values
    unique_vals = np.unique(input_grid)
    # There should be exactly two unique values: 5 and the "other" value.
    other_val = unique_vals[unique_vals != 5][0]

    # Step 2: Replace all occurrences of 5 with the other value
    output_grid[input_grid == 5] = other_val

    return output_grid


def solve_62c24649(input_grid):
    """
    Concepts: Grid flipping and concatenation (stacking)

    Transformation steps:
    1. Create three variants of the input grid:
       - Left-right flipped
       - Upside-down flipped
       - Both left-right and upside-down flipped
    2. Horizontally stack the original grid with its left-right flipped version to form the top half.
    3. Horizontally stack the upside-down flipped grid with the doubly flipped grid to form the bottom half.
    4. Vertically stack the top and bottom halves to produce the final output grid.
    """
    input_grid = np.array(input_grid)

    flipped_lr = np.fliplr(input_grid)  # Step 1: Left-right flip
    flipped_ud = np.flipud(input_grid)  # Step 1: Upside-down flip
    flipped_lr_ud = np.flipud(flipped_lr)  # Step 1: Left-right + upside-down flip

    # Step 2: Concatenate the original grid with the left-right flipped version
    top_half = np.hstack([input_grid, flipped_lr])
    # Step 3: Concatenate the upside-down flipped grid with the left-right + upside-down flipped version
    bottom_half = np.hstack([flipped_ud, flipped_lr_ud])
    # Step 4: Concatenate the top and bottom halves to form the final output grid
    output_grid = np.vstack([top_half, bottom_half])

    return output_grid


def solve_31d5ba1a(input_grid):
    """
    Concepts: Two halves of a grid, Double controlled gate logic using two halves of a grid

    Transformation steps:
    1. Split the grid into top_half and bottom_half
    Looing at training examples, we see that:
     - there are two halves of a grid, each have two unique values (0, 4) and (9, 0).
     - the following mapping
    2. For each cell in the top_half, pair it with the corresponding cell in the bottom_half.
    3. Use a mapping to determine the output value for each cell based on the pair:
       - (0, 0) -> 0
       - (0, 4) -> 6
       - (9, 0) -> 6
       - (9, 4) -> 0
    4. Construct the output grid using these mapped values.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    top_half = input_grid[: nrows // 2]  # Step 1: Get the top half
    bottom_half = input_grid[nrows // 2 :]  # Step 1: Get the bottom half

    # Step 2 and 3: Mapping for output values based on paired cells
    value_map = {(0, 0): 0, (0, 4): 6, (9, 0): 6, (9, 4): 0}
    output_grid = np.zeros_like(top_half, dtype=int)

    for r in range(top_half.shape[0]):
        for c in range(ncols):  # Step 4: Construct the output grid using the mapping
            output_grid[r, c] = value_map[(top_half[r, c], bottom_half[r, c])]

    return output_grid


def solve_fafffa47(input_grid):
    """
    Concepts: Two halves of a grid, addition of grid, conditional replacement of value

    Transformation steps:
    1. Split the grid into top_half and bottom_half
    2. Add the two halves together
    3. If the sum of the two halves is 0, then output 2, else output 0
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    top_half = input_grid[: nrows // 2]  # Step 1: Get the top half
    bottom_half = input_grid[nrows // 2 :]  # Step 1: Get the bottom half

    # Step 2: add the two halves together
    added = top_half + bottom_half
    # Step 3: If the sum of the two halves is 0, then output 2, else output 0
    output_grid = np.where(added == 0, 2, 0)

    return output_grid


def solve_5ad8a7c0(input_grid):
    """
    Concepts: 2D grid manipulation, mirroring, Pattern filling

    Transformation steps:
    1. Split the input grid into left and right halves.
    2. Find all positions of the color '2' in the left half.
    3. Identify the last column position of '2' in the left half.
    4. Create a copy of the left half input grid for output.
    5. For each row with '2' in the last column, fill all cells to the right with '2'.
    6. Mirror the left half to create the right half.
    7. Combine the left and right halves to form the output grid.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    half_ncols = ncols // 2
    # Step 1: Split the input grid into left and right halves
    left_half_input = input_grid[:, :half_ncols]

    # Step 2: Find all positions of the color '2' in the left half
    rows, cols = np.where(left_half_input == 2)

    # Step 3: Identify the last column position of '2' in the left half
    max_col = cols.max() if len(cols) > 0 else -1
    last_col_indices = np.where(cols == max_col)[0]

    # Step 4: Create a copy of the left half input grid for output
    left_half_output = left_half_input.copy()
    for idx in last_col_indices:
        r, c = rows[idx], cols[idx]
        left_half_output[r, c + 1 : half_ncols] = (
            2  # Step 5: Fill the right side of the row with '2'
        )

    right_half_output = np.fliplr(
        left_half_output
    )  # Step 6: Mirror the left half to create the right half

    # Step 7: Combine the left and right halves to form the output grid
    output_grid = np.hstack([left_half_output, right_half_output])

    return output_grid


def solve_a8610ef7(input_grid):
    """
    Concepts: vertical symmetry (up-down flip), value replacement based on symmetry

    Transformation steps:
    1. Loop through each cell in the grid.
    2. If value is 0, retain as 0.
    3. If value is 8:
        - Check vertically mirrored cell (i.e., up-down symmetric).
        - If mirrored cell also contains 8, change to 2.
        - Otherwise, change to 5.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros_like(input_grid)  # Initialize output grid with zeros

    for i in range(nrows):
        for j in range(ncols):
            if input_grid[i, j] == 8:  # Step 3: check for value 8
                mirror_i = nrows - 1 - i
                if input_grid[mirror_i, j] == 8:  # check for vertical symmetry
                    output_grid[i, j] = 2  # if symmetric, change to 2
                else:
                    output_grid[i, j] = 5  # if not symmetric, change to 5
            else:
                output_grid[i, j] = input_grid[i, j]

    return output_grid


def solve_1b2d62fb(input_grid):
    """
    Concepts: axis (column) to devide grid in two halves, Two halves of a grid, addition of grid, conditional replacement of value

    Transformation steps:
    1. Find the column containing the value 1; this acts as the axis to split the grid.
    2. Split the grid into left_half (left of the axis) and right_half (right of the axis).
    3. Add the two halves together
    4. If the sum of the two halves is 0, then output 8, else output 0
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Find the column with 1s (the axis)
    col_with_1 = None
    for i in range(ncols):
        if np.array_equal(input_grid[:, i], np.ones(nrows)):
            col_with_1 = i
            break

    left_half = input_grid[:, :col_with_1]  # Step 2: Get the left half from the axis
    right_half = input_grid[:, col_with_1 + 1 :]  # Step 2: Get the right half from the axis

    # Step 3: add the two halves together
    added = left_half + right_half
    # Step 4: If the sum of the two halves is 0, then output 8, else output 0
    output_grid = np.where(added == 0, 8, 0)

    return output_grid


def solve_a9f96cdd(input_grid):
    """
    Concepts: Pattern recognition, directional value placement

    Transformation steps:
    1. Identify the position (i, j) of the value 2 in the input grid.
    2. In a zero-initialized output grid of the same shape, place:
       - 3 at (i-1, j-1) [top-left]
       - 6 at (i-1, j+1) [top-right]
       - 8 at (i+1, j-1) [bottom-left]
       - 7 at (i+1, j+1) [bottom-right]
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Step 1: Find the position of 2 in the input grid
    i, j = np.argwhere(input_grid == 2)[0] if np.any(input_grid == 2) else []

    # Diagonal directions and corresponding values
    directions = [(-1, -1, 3), (-1, 1, 6), (1, -1, 8), (1, 1, 7)]
    # Step 2: Place values in the output grid based on the position of 2 and the defined directions
    for di, dj, val in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < nrows and 0 <= nj < ncols:  # Ensure we don't go out of bounds.
            output_grid[ni, nj] = val

    return output_grid


def solve_ce4f8723(input_grid):
    """
    Concepts: axis (row) to devide grid in two halves, combining halves of a grid, conditional value replacement

    Transformation steps:
    1. Find the row containing the value 4; this acts as the axis to split the grid.
    2. Split the grid into two halves: top half above the axis and bottom half below the axis.
    3. Add the two halves together element-wise.
    4. Initialize the output grid with 3s.
    5. In the added grid, find all positions where the value is 0.
    6. Set those positions to 0 in the output grid.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Find the row with 4s (the axis)
    row_with_4 = None
    for i in range(nrows):
        if np.array_equal(input_grid[i, :], 4 * np.ones(ncols)):
            row_with_4 = i
            break

    top_half = input_grid[:row_with_4]  # Step 2: Get the top half above the axis
    bottom_half = input_grid[row_with_4 + 1 :]  # Step 2: Get the bottom half below the axis

    # Step 3: Add the two halves together
    added = top_half + bottom_half

    # Step 4. Initialize output grid with 3s
    output_grid = 3 * np.ones_like(added)

    # Step 5: In the added grid, find all positions where the value is 0.
    # Step 6. Set those positions to 0 in the output grid.
    output_grid[added == 0] = 0

    return output_grid


def solve_67385a82(input_grid):
    """
    Concepts: copy input, local neighborhood check, change value based on neighbors

    Transformation steps:
    1. Initialize the output grid as a copy of the input grid.
    2. For each cell in the input grid:
        - 3. If the value is 3:
            - 4. Check its 4-connected neighbors (up, down, left, right).
            - 5. If any of them is not 0, set it to 8 in the output.
            - 6. Otherwise, retain 3.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()  # Step 1: Initialize output grid as a copy of the input grid

    # Step 2: Iterate through each cell in the input grid
    for i in range(nrows):
        for j in range(ncols):
            # Step 3: If the cell value is 3
            # Step 4: Check its neighbors
            # Step 5: If any neighbor is not 0, set it to 8
            # Step 6: Otherwise, retain 3
            if input_grid[i, j] == 3:
                neighbors = []
                if i > 0:
                    neighbors.append(input_grid[i - 1, j])
                if i < nrows - 1:
                    neighbors.append(input_grid[i + 1, j])
                if j > 0:
                    neighbors.append(input_grid[i, j - 1])
                if j < ncols - 1:
                    neighbors.append(input_grid[i, j + 1])

                if any(val != 0 for val in neighbors):
                    output_grid[i, j] = 8
    return output_grid


def solve_e133d23d(input_grid):
    """
    Concepts: axis (column) to devide grid in two halves, Two halves of a grid, addition of grid, conditional replacement of value

    Transformation steps:
    1. Find the column containing the value 4; this acts as the axis to split the grid.
    2. Split the grid into left_half (left of the axis) and right_half (right of the axis).
    3. Add the two halves together
    4. If the sum of the two halves is 0, then output 0, else output 2
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Find the column containing the value 4s (the axis)
    col_with_4 = None
    for i in range(ncols):
        if np.array_equal(input_grid[:, i], 4 * np.ones(nrows)):
            col_with_4 = i
            break

    left_half = input_grid[:, :col_with_4]  # Step 2: Get the left half from the axis
    right_half = input_grid[:, col_with_4 + 1 :]  # Step 2: Get the right half from the axis

    # Step 3: add the two halves together
    added = left_half + right_half
    # Step 4: If the sum of the two halves is 0, then output 0, else output 2
    output_grid = np.where(added == 0, 0, 2)

    return output_grid


def solve_9565186b(input_grid):
    """
    Concepts: frequency count, masking, conditional replacement

    Transformation steps:
    1. Count the frequency of each number in the input grid.
    2. Identify the most frequent number(s).
    3. Retain values that match the most frequent number; replace all others with 5.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Step 1: Flatten the grid and count frequency
    unique, counts = np.unique(input_grid, return_counts=True)
    freq_dict = dict(zip(unique, counts))

    # Step 2: Find the number(s) with the maximum frequency
    max_freq = max(freq_dict.values())
    most_frequent = [val for val, cnt in freq_dict.items() if cnt == max_freq]

    # Step 3: Replace all non-most-frequent values with 5
    output_grid = np.where(np.isin(input_grid, most_frequent), input_grid, 5)

    return output_grid


def solve_4c4377d9(input_grid):
    """
    Concepts: Flip grid, concatenate or stack grids

    Transformation steps:
    1. Flip the input grid upside down
    2. Stack the flipped grid on top of the original grid
    """
    input_grid = np.array(input_grid)
    # Step 1: Flip the input grid upside down
    flipped_ud = np.flipud(input_grid)

    # Step 2: Stack the flipped grid on top of the original grid
    output_grid = np.vstack([flipped_ud, input_grid])

    return output_grid


def solve_59341089(input_grid):
    """
    Concepts: Flip grid, repeat parts, stack grids

    Transformation steps:
    1. Flip the input grid left to right.
    2. Concatenate the flipped grid and the original grid horizontally and get the output part.
    3. Horizontally stack the output part with itself to form the final output grid.
    """
    input_grid = np.array(input_grid)

    # Step 1: Flip the input grid left to right
    flipped_lr = np.fliplr(input_grid)

    # Step 2: Concatenate the flipped grid and the original grid horizontally to get the output part
    output_part = np.hstack([flipped_lr, input_grid])

    # Step 3: Horizontally stack the output part with itself to form the final output grid
    output_grid = np.hstack([output_part, output_part])

    return output_grid


def solve_bc1d5164(input_grid):
    """
    Concepts: split grid in left-right or top-bottom parts, compute element-wise maximum of parts

    Transformation steps:
    1. Split the input grid into left and right parts.
    2. Compute the element-wise maximum of the two parts.
    3. Extract the top and bottom 3 rows from the maximum part.
    4. Compute the element-wise maximum of the top and bottom parts.
    """
    input_grid = np.array(input_grid)

    # Step 1: Split the input grid into left and right parts, each with 3 columns.
    left_part = input_grid[:, :3]
    right_part = input_grid[:, -3:]

    # Step 2: Compute the element-wise maximum of the two parts.
    max_part = np.max([left_part, right_part], axis=0)  # Element-wise max of the two parts

    # Step 3: Extract the top and bottom 3 rows from the maximum part.
    top_part = max_part[:3, :]
    bottom_part = max_part[-3:, :]

    # Step 4: Compute the element-wise maximum of the top and bottom parts.
    output_grid = np.max([top_part, bottom_part], axis=0)
    return output_grid


def solve_b1fc8b8e(input_grid):
    """
    Concepts: topology, pattern recognition, pattern extraction, spatial reasoning

    # In the input grid, 8s are either making four 2x2 square or four flipped L shapes.
    # if they are squares, then number of 8s will be 4*4 = 16
    # if they are flipped L, then number of 8s will be 3*4 = 12
    # based on that we can form a 5x5 output grid with four squares or flipped L shapes at the corners.

    Transformation steps:
    1. Initialize a 5x5 output grid with zeros.
    2. Count the number of 8s in the input grid.
    3. If there are 16 8s, they form four squares at the four corners of the output grid.
       If there are 12 8s, they form four flipped L shapes at the four corners of the output grid.
    """
    input_grid = np.array(input_grid)
    # Step 1: Initialize a 5x5 output grid with zeros.
    output_grid = np.zeros((5, 5), dtype=int)

    # In the input grid, 8s are either making four 2x2 square or flipped L shapes.
    # if they are squares, then number of 8s will be 4*4 = 16
    # if they are flipped L, then number of 8s will be 3*4 = 12
    square = np.array([[8, 8], [8, 8]], dtype=int)
    flipped_L = np.array([[0, 8], [8, 8]], dtype=int)

    # Step 2: Count the number of 8s in the input grid.
    num_8s = len(np.where(input_grid == 8)[0])

    if (
        num_8s == 16
    ):  # Step 3: If there are 16 8s, they form four squares at the four corners of the output grid.
        output_grid[0:2, 0:2] = square  # top-left
        output_grid[0:2, 3:5] = square  # top-right
        output_grid[3:5, 0:2] = square  # bottom-left
        output_grid[3:5, 3:5] = square  # bottom-right
    elif (
        num_8s == 12
    ):  # Step 3: If there are 12 8s, they form four flipped L shapes at the four corners of the output grid.
        output_grid[0:2, 0:2] = flipped_L  # top-left
        output_grid[0:2, 3:5] = flipped_L  # top-right
        output_grid[3:5, 0:2] = flipped_L  # bottom-left
        output_grid[3:5, 3:5] = flipped_L  # bottom-right

    return output_grid


def solve_d4469b4b(input_grid):
    """
    Concepts: topological out, value or color recognition

    Transformation: Based on the unique non-zero value in the input grid, output of a specific topological shape is given.

    Transformation steps:
    1. Define (or collect from train examples) the output grids of different topological shapes for different cases.
    2. Find the unique non-zero element (value or color) in the input grid.
    3. Based on the unique non-zero value, select the corresponding output grid.
    """
    input_grid = np.array(input_grid)

    # Step 1: Define (or collect from train examples) the output grids of different topological shapes for different cases.
    plus_output = np.array([[0, 5, 0], [5, 5, 5], [0, 5, 0]])  # plus (+) shaped output
    T_output = np.array([[5, 5, 5], [0, 5, 0], [0, 5, 0]])  # T shaped output
    flipped_L_output = np.array([[0, 0, 5], [0, 0, 5], [5, 5, 5]])  # flipped L shaped output

    # Step 2: find the unique non-zero element (value or color) in the input grid.
    non_zero_value = np.unique(input_grid[input_grid != 0])

    # Step 3: Based on the unique non-zero value, select the corresponding output grid.
    if non_zero_value == 1:
        output_grid = plus_output
    elif non_zero_value == 2:
        output_grid = T_output
    elif non_zero_value == 3:
        output_grid = flipped_L_output

    return output_grid


def solve_e345f17b(input_grid):
    """
    Concepts: Two halves of a grid, addition of grid, conditional replacement of value

    Transformation steps:
    1. Split the grid into top_half and bottom_half
    2. Add the two halves together
    3. If the sum of the two halves is 0, then output 4, else output 0
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    left_half = input_grid[:, : ncols // 2]  # Step 1: Get the left half
    right_half = input_grid[:, ncols // 2 :]  # Step 1: Get the right half

    # Step 2: add the two halves together
    added = left_half + right_half
    # Step 3: If the sum of the two halves is 0, then output 4, else output 0
    output_grid = np.where(added == 0, 4, 0)
    return output_grid


def solve_794b24be(input_grid):
    """
    Concepts: num occurrences, value or color recognition,

    Transformation: Based on the number of occurrences of 1 in the input grid, a specific output is given

    Transformation steps:
    1. Define (or collect from train examples) the 3x3 output grids for different cases.
    2. Count the number of occurrences of 1 in the input grid.
    3. Based on the number of occurrences, select the corresponding output grid.
    """

    input_grid = np.array(input_grid)

    # Step 1: Define (or collect from train examples) the 3x3 output grids for different cases.
    one_occ_output = np.array([[2, 0, 0], [0, 0, 0], [0, 0, 0]])
    two_occ_output = np.array([[2, 2, 0], [0, 0, 0], [0, 0, 0]])
    three_occ_output = np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]])
    four_occ_output = np.array([[2, 2, 2], [0, 2, 0], [0, 0, 0]])

    # Step 2: Count the number of occurrences of 1 in the input grid.
    num_occurrences = np.count_nonzero(input_grid == 1)

    # Step 3: Based on the number of occurrences, select the corresponding output grid.
    if num_occurrences == 1:
        output_grid = one_occ_output
    elif num_occurrences == 2:
        output_grid = two_occ_output
    elif num_occurrences == 3:
        output_grid = three_occ_output
    elif num_occurrences == 4:
        output_grid = four_occ_output

    return output_grid


def solve_4cd1b7b2(input_grid):
    """
    Concepts: Latin square completion, backtracking

    Transformation steps:
    1. Identify positions of zeros (unfilled cells).
    2. Use backtracking to assign numbers 1–4 to each zero
       such that each row and column contains all numbers 1–4 exactly once.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Create the set of digits (colors) to fill in the grid
    digits = {1, 2, 3, 4}

    # Recursive backtracking function to fill the grid (Latin square)
    def solve(grid):
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 0:  # Step 1: Identify positions of zeros (unfilled cells).
                    row_vals = set(grid[i])
                    col_vals = set(grid[:, j])
                    candidates = digits - row_vals - col_vals
                    for val in candidates:
                        grid[i][j] = val
                        if solve(grid):  # Step 2: Recursively try to fill the rest of the grid
                            return True
                        grid[i][j] = 0  # Backtrack if no valid assignment found
                    return False  # No valid value found
        return True  # All cells filled

    output_grid = input_grid.copy()
    solve(output_grid)
    return output_grid


def solve_746b3537(input_grid):
    """
    Concepts: Deduplication of adjacent identical rows and columns, remove duplicates.

    Transformation steps:
    1. Remove adjacent duplicate rows.
    2. Remove adjacent duplicate columns.
    3. Repeat until no adjacent duplicates remain.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    changed = True
    while changed:
        changed = False

        # Step 1: Remove adjacent duplicate rows
        new_rows = [output_grid[0]]
        for i in range(1, len(output_grid)):
            if not np.array_equal(output_grid[i], output_grid[i - 1]):
                new_rows.append(output_grid[i])
            else:
                changed = True
        output_grid = np.array(new_rows)

        # Step 2: Remove adjacent duplicate columns
        output_grid = output_grid.T
        new_cols = [output_grid[0]]
        for i in range(1, len(output_grid)):
            if not np.array_equal(output_grid[i], output_grid[i - 1]):
                new_cols.append(output_grid[i])
            else:
                changed = True
        output_grid = np.array(new_cols).T

    return output_grid


def solve_f2829549(input_grid):
    """
    Concepts: axis (column) to divide grid in two halves, Two halves of a grid around an axis, addition of halves, conditional replacement of values

    Transformation steps:
    1. Find the column containing the value 1; this acts as the axis to split the grid.
    2. Split the grid into top_half (above the axis) and bottom_half (below the axis).
    3. Add the two halves together
    4. If the sum of the two halves is 0, then output 3, else output 0
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Find the column with 1s (the axis)
    col_with_1 = None
    for i in range(ncols):
        if np.array_equal(input_grid[:, i], np.ones(nrows)):
            col_with_1 = i
            break

    left_half = input_grid[:, :col_with_1]  # Step 2: Get the left half
    right_half = input_grid[:, col_with_1 + 1 :]  # Step 2: Get the right half

    # Step 3: add the two halves together
    added = left_half + right_half
    # Step 4: If the sum of the two halves is 0, then output 3, else output 0
    output_grid = np.where(added == 0, 3, 0)
    return output_grid


def solve_8d5021e8(input_grid):
    """
    Concepts: flipping, stacking, mirroring

    Transformation steps:
    1. Create a central part by flipping the input grid horizontally and stacking it with itself
    2. Create a top and bottom part by flipping the central part vertically
    3. Stack the top, central, and bottom parts to form the final output grid
    """

    input_grid = np.array(input_grid)
    # Step 1: Create a central part by flipping the input grid horizontally and stacking it with itself
    central_part = np.hstack([np.fliplr(input_grid), input_grid])
    # Step 2: Create a top and bottom part by flipping the central part vertically
    part = np.flipud(central_part)
    # Step 3: Stack the top, central, and bottom parts to form the final output grid
    output_grid = np.vstack([part, central_part, part])

    return output_grid


def solve_2072aba6(input_grid):
    """
    Concepts:

    Transformation steps:
    1. Initialize an output grid of size (2×nrows, 2×ncols) filled with zeros.
       - This will be twice the size of the input grid.
    2. For each cell in the input grid,
       - if it contains non-zero value 5, replace the corresponding block in the output grid with 2x2 non-zero block [[1, 2], [2, 1]].
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Initialize output grid of size (2×nrows, 2×ncols)
    output_grid = np.zeros((2 * nrows, 2 * ncols), dtype=int)

    non_zero_block = np.array([[1, 2], [2, 1]], dtype=int)

    for i in range(nrows):
        for j in range(ncols):
            r, c = 2 * i, 2 * j
            if input_grid[i, j] == 5:  # Step 2: if the input cell is 5
                # Place the non-zero block in the corresponding position in the output grid
                output_grid[r : r + 2, c : c + 2] = non_zero_block

    return output_grid


def solve_88a62173(input_grid):
    """
    Concepts: Odd-One-Out Pattern Recognition, Corner Subgrid Comparison

    Transformation steps:
    1. Extract 2x2 subgrids from each of the four corners of the input grid.
    2. Compare the subgrids to find the one that differs from the others and return it as the output.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros((2, 2), dtype=input_grid.dtype)

    # Step 1: Extract 2x2 subgrids from each corner
    top_left = input_grid[:2, :2]
    top_right = input_grid[:2, -2:]
    bottom_left = input_grid[-2:, :2]
    bottom_right = input_grid[-2:, -2:]

    subgrids = [top_left, top_right, bottom_left, bottom_right]

    # Flatten for easy comparison
    flat_grids = [sg.flatten() for sg in subgrids]

    # Step 2: Count how many times each unique subgrid appears
    counts = {}
    for i, g in enumerate(flat_grids):
        key = tuple(g)
        counts[key] = counts.get(key, []) + [i]

    # Step 2: Find the key with only one index — the odd one out
    for key, indices in counts.items():
        if len(indices) == 1:
            odd_index = indices[0]
            output_grid = subgrids[odd_index]
            break

    return output_grid


def solve_9af7a82c(input_grid):
    """
    Concepts: Odd-One-Out Pattern Recognition, Corner Subgrid Comparison

    Transformation steps:
    1. Extract 2x2 subgrids from each of the four corners of the input grid.
    2. Compare the subgrids to find the one that differs from the others and return it as the output.
    """
    input_grid = np.array(input_grid)
    flat = input_grid.flatten()

    # Step 1: Get unique values and their counts
    unique_vals, counts = np.unique(flat, return_counts=True)

    # Sort values by frequency (count) descending
    sorted_indices = np.argsort(-counts)
    sorted_vals = unique_vals[sorted_indices]
    sorted_counts = counts[sorted_indices]

    max_rows = sorted_counts[0]
    ncols = len(sorted_vals)
    # Initialize output grid with zeros
    output_grid = np.zeros((max_rows, ncols), dtype=int)

    # Fill the output grid with sorted values based on their frequency
    for col, (val, freq) in enumerate(zip(sorted_vals, sorted_counts)):
        output_grid[:freq, col] = val

    return output_grid


def solve_dae9d2b5(input_grid):
    """
    Concepts: adding halves of a grid, creating a mask based on zero, non-zero values.

    Transformation steps:
    1. Get the left and right halves of the input grid.
    2. Add the two halves together element-wise.
    3. In the added grid, find all positions where the values are non-zeros.
    4. Set those positions to 6 in the output grid.
    """
    input_grid = np.array(input_grid)
    nrow, ncol = input_grid.shape

    # Step 1: Split into left and right halves
    left_half = input_grid[:, : ncol // 2]
    right_half = input_grid[:, ncol // 2 :]

    # Step 3: Add the two halves together
    added = left_half + right_half

    output_grid = np.zeros_like(added)  # initialize output grid with zeros

    # Step 4: In the added grid, find all positions where the values are non-zeros.
    # Set those positions to 6 in the output grid.
    output_grid[added != 0] = 6

    return output_grid


def solve_c8cbb738(input_grid):
    """
    Concepts: finding backround (most frequent value), putting non-background values like russian dolls while keeping common center.

    Transformation: It extracts all non-background shapes and centers them in a new grid like Russian dolls, preserving their relative forms.
    The output grid is just large enough to fit the largest shape, and all shapes share a common center.

    Transformation steps:
    1. Convert input to a NumPy array.
    2. Identify the background value as the most frequent element using np.unique with return_counts.
    3. Get positions of non-background values and dimensions (H, W) of the output grid.
    4. Center coordinates of output grid of size HxW.
    5. Initialize output grid with background value.
    6. Copy non-background values to output by matching their center to output grid center.
    """
    input_grid = np.array(input_grid)

    # Step 1: Find the most frequent value (background)
    unique_vals, counts = np.unique(input_grid, return_counts=True)
    background_val = unique_vals[np.argmax(counts)]

    # Step 2: Identify non-background values
    non_background_vals = unique_vals[unique_vals != background_val]

    # Step 3: Get positions (rows, cols) of non-background values and dimensions (H, W) of the output grid
    Rows, Cols = [], []
    H, W = 0, 0
    for nbv in non_background_vals:
        rows, cols = np.where(input_grid == nbv)
        min_row, min_col = rows.min(), cols.min()
        max_row, max_col = rows.max(), cols.max()

        H = max(H, (max_row - min_row) + 1)
        W = max(W, (max_col - min_col) + 1)

        Rows.append(rows)
        Cols.append(cols)

    # Step 4: Center coordinates of output grid of size HxW
    center_H, center_W = H // 2, W // 2

    # Step 5: Initialize output grid with background value
    output_grid = np.full((H, W), background_val)

    # Step 5: Copy non-background values to output by matching their center to output grid center
    # For each non-background value, translate its positions to center around the output grid center
    # This ensures that the non-background values are placed correctly in the output grid.
    # This effectively creates a "Russian doll" effect where each shape is centered in the output grid.
    for i, nbv in enumerate(non_background_vals):
        rows, cols = Rows[i], Cols[i]
        min_row, min_col = rows.min(), cols.min()
        max_row, max_col = rows.max(), cols.max()
        center_row = (max_row + min_row) // 2
        center_col = (max_col + min_col) // 2

        for r, c in zip(rows, cols):
            rr = r - center_row + center_H
            cc = c - center_col + center_W
            output_grid[rr, cc] = nbv

    return output_grid


def solve_8e1813be(input_grid):
    """
    Concepts: extracting horizontal or vertical strips of unique values.

    Transformation:
    - Detect and extract horizontal or vertical strips of unique values
      (excluding the background of 0s and the block of 5s).
    - Preserve the order of appearance: top-to-bottom for horizontal, left-to-right for vertical.
    - Output square grid of strips by following the order and of the same strip type.

    Transformation Steps:
    1. Extract the unique values (excluding 0 and 5)
    2. Determine strip type (horizontal or vertical) and positions for each of the unique value
    3. Sort by appearance order (row or column index) of the unique values in the input grid
    4. Create output grid of strips by following the order and of the same strip type
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Extract the unique values excluding 0 and 5
    unique_vals = list(set(np.unique(input_grid)) - {0, 5})

    # Step 2: Determine strip type (horizontal or vertical) and positions for each of the unique value
    strip_type = None
    positions = []

    for val in unique_vals:
        rows, cols = np.where(input_grid == val)
        if len(np.unique(rows)) == 1:
            # Horizontal strip
            strip_type = "horizontal"
            positions.append(rows[0])
        elif len(np.unique(cols)) == 1:
            # Vertical strip
            strip_type = "vertical"
            positions.append(cols[0])

    # Step 3: Sort by appearance order (row or column index) of the unique values in the input grid
    order = np.argsort(positions)
    num_strips = len(unique_vals)

    # Step 4: Create output grid of strips by following the order and of the same strip type
    output_grid = np.zeros((num_strips, num_strips), dtype=int)
    if strip_type == "horizontal":
        for i, o in enumerate(order):
            output_grid[i, :] = unique_vals[o]
    elif strip_type == "vertical":
        for i, o in enumerate(order):
            output_grid[:, i] = unique_vals[o]

    return output_grid


def solve_a699fb00(input_grid):
    """
    Concepts: Pattern detection and local value replacement in a 2D grid.

    Transformation: Fill 2 in between two 1s in each row of the grid.

    Transformation steps:
    1. Iterate through each row of the grid.
    2. For each row, check for the pattern [1, 0, 1].
    3. Replace the center 0 with 2 if the pattern is found.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    for r in range(nrows):
        for c in range(1, ncols - 1):
            if input_grid[r, c - 1] == 1 and input_grid[r, c] == 0 and input_grid[r, c + 1] == 1:
                output_grid[r, c] = 2

    return output_grid


def solve_20fb2937(input_grid):
    """
    Concepts: Grid partitioning into rule part (top) and work part (bottom), rule: vale to 3x3 block mapping, in-place replacement.

     Transformation Summary
     a. The input grid is divided into two parts:
        - Top part (before the first full row of 6s):
          This part provides mapping rules: each rule consists of a 1×1 value and its corresponding 3×3 block (pattern).
        - Bottom part (after the row of 6s): This is where the replacement happens.
           Each 1×1 value is replaced with its corresponding 3×3 block, as defined in the top part.
     b. The replacement happens in-place in the bottom grid:
        - At each cell in the bottom part: if the value is one of the mapping values, replace it with the corresponding 3×3 block centered at that cell.
        - The output grid is constructed with these replaced blocks (note: blocks can overwrite each other; latest ones persist).

    Transformation steps:
    1. Find the dividing row (partition row full of 6s). The background is represented by 7s.
    2. Extract rule part (top) and work part (bottom)
    3. Get 3 pairs of 3x3 block and value from the rule part.
    4. For each cell in the bottom part of the grid, if it matches a mapped value, replace it with the corresponding 3x3 block centered at that cell.
    5. Construct the output grid with these replacements, ensuring to fill in the background (7s) where no replacements occur.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Find the dividing row (partition row full of 6s)
    partition_row = np.where(np.all(input_grid == 6, axis=1))[0][0]

    # Step 2: Extract rule part (top) and work part (bottom)
    rule_grid = input_grid[:partition_row]
    work_grid = input_grid[partition_row + 1 :]

    # Step 3: Get 3 pairs of value and 3x3 block
    block_to_value_map = {}
    value_to_block_map = {}

    for col in range(0, ncols, 4):  # step by 4: 3x3 block + 1 col gap
        if col + 3 > ncols:
            continue
        block = rule_grid[0:3, col : col + 3]
        value = rule_grid[4, col + 1]  # center cell in row 4 (value location)
        block_to_value_map[value] = block
        value_to_block_map[value] = block

    # Step 4 and 5: Prepare output grid (same shape as bottom part) and of the background of 7s
    output_grid = np.full_like(work_grid, 7)

    # Step 4 and 5: Replace values with corresponding 3x3 blocks
    h, w = work_grid.shape
    for r in range(h):
        for c in range(w):
            val = work_grid[r, c]
            if val in value_to_block_map:
                block = value_to_block_map[val]
                for i in range(3):
                    for j in range(3):
                        rr = r + i - 1
                        cc = c + j - 1
                        if 0 <= rr < h and 0 <= cc < w:
                            output_grid[rr, cc] = block[i, j]

    return output_grid


def solve_5c2c9af4(input_grid):
    """
    Concepts: square side and center detection, concentric square drawing.

    Transformation steps:
    1. Identify the non-background value.
    2. Get positions of the non-background value.
    3. Find center for all the squares.
    4. Get distance from center to the first square corner.
    5. Draw concentric square borders around the center using the non-background value.
    6. Repeat until the maximum size of the grid is reached.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Identify non-background value
    unique_vals, counts = np.unique(input_grid, return_counts=True)
    background_val = unique_vals[np.argmax(counts)]
    non_background_val = unique_vals[np.argmin(counts)]

    # Step 2: Get positions of the non-background value
    rows, cols = np.where(input_grid == non_background_val)
    min_row, max_row = rows.min(), rows.max()
    min_col, max_col = cols.min(), cols.max()

    # Step 3: Find center for all the squares
    center_row = (set(rows) - {min_row, max_row}).pop()
    center_col = (set(cols) - {min_col, max_col}).pop()

    # Step 4: Distance from center to first square's edge
    distance = abs(center_row - min_row)

    # Step 5: Prepare output grid
    output_grid = np.full_like(input_grid, background_val)

    def draw_square(grid, center_row, center_col, side_len, value):
        """Draws the perimeter of a square centered at (center_row, center_col)."""
        nrows, ncols = grid.shape
        half = side_len // 2

        top = center_row - half
        bottom = center_row + half
        left = center_col - half
        right = center_col + half

        # Draw top and bottom edges
        for col in range(left, right + 1):
            if 0 <= top < nrows and 0 <= col < ncols:
                grid[top, col] = value
            if 0 <= bottom < nrows and 0 <= col < ncols:
                grid[bottom, col] = value

        # Draw left and right edges
        for row in range(top, bottom + 1):
            if 0 <= row < nrows and 0 <= left < ncols:
                grid[row, left] = value
            if 0 <= row < nrows and 0 <= right < ncols:
                grid[row, right] = value

    # Step 6: Draw concentric squares
    max_half_side = max(center_row, nrows - 1 - center_row, center_col, ncols - 1 - center_col)
    num_squares = max_half_side // distance + 1

    for k in range(num_squares):
        side_len = distance * 2 * k + 1
        draw_square(output_grid, center_row, center_col, side_len, non_background_val)

    return output_grid


def solve_f0afb749(input_grid):
    """
    Concepts: value expansion, diagonal patterning

    Transformation: Expand each non-zero cell to a 2×2 block, then extend diagonally with 2×2 [[1,0], [0,1]] patterns.

    Transformation steps:
    1. Identify all non-background (non-zero) values and their positions (r, c) in the input grid.
    2. Create an output grid of size (2*nrows, 2*ncols) filled with zeros.
    3. For each non-background value v:
       a. Place a 2×2 block filled with v at position (2*r, 2*c).
       b. From the center of that block, move along both diagonal directions:
          - (-1, -1), (-2, -2), ... upward-left
          - (+1, +1), (+2, +2), ... downward-right
         At each such position, place the fixed pattern [[1, 0], [0, 1]] (without overwriting existing non-zero values).
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Initialize output grid with double the size of input grid to the background value (0)
    output_grid = np.zeros((nrows * 2, ncols * 2), dtype=int)

    # Step 1: find all non-zero (non-background) positions
    nonzero_positions = np.argwhere(input_grid != 0)

    for r, c in nonzero_positions:
        v = input_grid[r, c]
        # Step 3a: expand original cell to 2×2 block with value v
        output_grid[2 * r : 2 * r + 2, 2 * c : 2 * c + 2] = v

        # Step 3b: place diagonal [[1,0],[0,1]] patterns
        for dr, dc in [(-1, -1), (1, 1)]:
            rr, cc = r + dr, c + dc
            while 0 <= rr < nrows and 0 <= cc < ncols:
                R, C = 2 * rr, 2 * cc
                pattern = np.array([[1, 0], [0, 1]])
                mask = output_grid[R : R + 2, C : C + 2] == 0
                output_grid[R : R + 2, C : C + 2] = np.where(
                    mask, pattern, output_grid[R : R + 2, C : C + 2]
                )
                rr += dr
                cc += dc

    return output_grid


def solve_94414823(input_grid):
    """
    Concepts:
        - Frame detection
        - Diagonal 2×2 block placement

    Transformation: Replace the two corner-adjacent numbers outside a 5-frame with 2×2 blocks of the same values placed in the frame’s diagonally.

    Transformation steps:
    1. Identify the outer frame of '5's in the grid.
    2. Detect the nonzero values just outside each corner of the frame.
    3. Place 2×2 squares of these values inside the frame along the diagonal that passes through the corner where the value was detected.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Step 1: Find frame bounds (assuming perfect rectangle of 5s)
    rows, cols = np.where(input_grid == 5)
    rmin, rmax = rows.min(), rows.max()
    cmin, cmax = cols.min(), cols.max()

    # Step 2: Detect nonzero values just outside frame corners
    vals = {}
    if rmin - 1 >= 0 and cmin - 1 >= 0 and input_grid[rmin - 1, cmin - 1] != 0:
        vals["top_left"] = input_grid[rmin - 1, cmin - 1]
    if rmin - 1 >= 0 and cmax + 1 < input_grid.shape[1] and input_grid[rmin - 1, cmax + 1] != 0:
        vals["top_right"] = input_grid[rmin - 1, cmax + 1]
    if rmax + 1 < input_grid.shape[0] and cmin - 1 >= 0 and input_grid[rmax + 1, cmin - 1] != 0:
        vals["bottom_left"] = input_grid[rmax + 1, cmin - 1]
    if (
        rmax + 1 < input_grid.shape[0]
        and cmax + 1 < input_grid.shape[1]
        and input_grid[rmax + 1, cmax + 1] != 0
    ):
        vals["bottom_right"] = input_grid[rmax + 1, cmax + 1]

    # Place 2×2 squares of these values inside the frame along the diagonal that passes through the corner where the value was detected.
    if "top_left" in vals:
        output_grid[rmin + 1 : rmin + 3, cmin + 1 : cmin + 3] = vals["top_left"]
        output_grid[rmin + 3 : rmin + 5, cmin + 3 : cmin + 5] = vals["top_left"]
    if "bottom_right" in vals:
        output_grid[rmin + 1 : rmin + 3, cmin + 1 : cmin + 3] = vals["bottom_right"]
        output_grid[rmin + 3 : rmin + 5, cmin + 3 : cmin + 5] = vals["bottom_right"]
    if "top_right" in vals:
        output_grid[rmin + 1 : rmin + 3, cmax - 2 : cmax] = vals["top_right"]
        output_grid[rmin + 3 : rmin + 5, cmin + 1 : cmin + 3] = vals["top_right"]
    if "bottom_left" in vals:
        output_grid[rmin + 1 : rmin + 3, cmax - 2 : cmax] = vals["bottom_left"]
        output_grid[rmin + 3 : rmin + 5, cmin + 1 : cmin + 3] = vals["bottom_left"]

    return output_grid


def solve_23581191(input_grid):
    """
    Concepts: row/column propagation of non-background values with special intersection rule.

    Transformation steps:
    1. Identify all non-zero (non-background) values and their coordinates.
    2. For each such value, fill its entire row and column with the same value.
    3. If multiple values intersect at a cell, set that cell to 2.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Step 1: Find positions of non-background cells. 0s are considered background.
    non_bg_positions = [
        (r, c, val) for r, c in zip(*np.nonzero(input_grid)) for val in [input_grid[r, c]]
    ]

    # Step 2 and 3: Fill rows and columns
    for r, c, val in non_bg_positions:
        output_grid[r, :] = np.where(
            output_grid[r, :] == 0, val, np.where(output_grid[r, :] != val, 2, val)
        )
        output_grid[:, c] = np.where(
            output_grid[:, c] == 0, val, np.where(output_grid[:, c] != val, 2, val)
        )

    return output_grid


def solve_dc2e9a9d(input_grid):
    """
    Concepts:
    - Connected component detection (flood fill)
    - Symmetry-based reflection and value assignment

    Transformation steps:
    1. Find all connected components of cells with value 3.
    2. For each component, determine if the "extra" cell is along a row or column edge.
    3. Reflect the component across the axis opposite the extra cell, with an extra gap.
    4. Assign value 8 for row-based reflections, and 1 for column-based reflections.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    nrows, ncols = input_grid.shape
    visited = np.zeros_like(input_grid, dtype=bool)

    def get_component(r, c):
        """Return list of coordinates for connected 3's starting from (r, c)."""
        stack = [(r, c)]
        visited[r, c] = True
        coords = []
        while stack:
            rr, cc = stack.pop()
            coords.append((rr, cc))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = rr + dr, cc + dc
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    if not visited[nr, nc] and input_grid[nr, nc] == 3:
                        visited[nr, nc] = True
                        stack.append((nr, nc))
        return coords

    # Step 1: Find all components of 3's
    components = []
    for r in range(nrows):
        for c in range(ncols):
            if not visited[r, c] and input_grid[r, c] == 3:
                components.append(get_component(r, c))

    # Step 2–4: Process each component
    for coords in components:
        rs = np.array([r for r, _ in coords])
        cs = np.array([c for _, c in coords])

        r_unique, r_counts = np.unique(rs, return_counts=True)
        c_unique, c_counts = np.unique(cs, return_counts=True)

        flag = None
        r_extra_cell = c_extra_cell = None

        if np.any(r_counts == 1):
            r_extra_cell = r_unique[r_counts == 1][0]
            c_extra_cell = cs[rs == r_extra_cell][0]
            flag = "extra cell (row) above or below"
        if np.any(c_counts == 1):
            c_extra_cell = c_unique[c_counts == 1][0]
            r_extra_cell = rs[cs == c_extra_cell][0]
            flag = "extra cell (column) left or right"

        rmin, rmax = rs.min(), rs.max()
        cmin, cmax = cs.min(), cs.max()

        # Decide reflection direction and compute target coordinates
        if flag == "extra cell (row) above or below":
            if r_extra_cell == rmin:
                # Extra cell above → mirror below with one extra row in between
                target_r = [rmax + 2 + (rmax - r) for r in rs]
                target_c = cs
            elif r_extra_cell == rmax:
                # Extra cell below → mirror above with one extra row in between
                target_r = [rmin - 2 - (r - rmin) for r in rs]
                target_c = cs
        elif flag == "extra cell (column) left or right":
            if c_extra_cell == cmin:
                # Extra cell left → mirror right with one extra column in between
                target_r = rs
                target_c = [cmax + 2 + (cmax - c) for c in cs]
            elif c_extra_cell == cmax:
                # Extra cell right → mirror left with one extra column in between
                target_r = rs
                target_c = [cmin - 2 - (c - cmin) for c in cs]
        else:
            continue  # Skip if no extra cell found

        # Apply mirrored values: 8 for row-based, 1 for column-based
        for rr, cc in zip(target_r, target_c):
            if 0 <= rr < nrows and 0 <= cc < ncols:
                if flag == "extra cell (row) above or below":
                    output_grid[rr, cc] = 8
                elif flag == "extra cell (column) left or right":
                    output_grid[rr, cc] = 1

    return output_grid


def solve_a644e277(input_grid):
    """
    Concepts:
    - Region extraction based on dominant and secondary values
    - Subgrid cropping using row/column frequency analysis

    Transformation steps:
    1. Identify the background value (most frequent) and the marked value (second most frequent) in the grid.
    2. Find all the rows dominated by the marked value
    3. Find all the columns dominated by the marked value
    4. For each intersection of these rows and columns, check if the cell contains the background value.
    5. Collect all such row and column indices to define the bounding box.
    6. Crop the input grid to the rectangle defined by these rows and columns.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Identify background and marked values
    unique_vals, counts = np.unique(input_grid, return_counts=True)
    counts_sorted = np.argsort(counts)
    background_val = unique_vals[counts_sorted[-1]]
    marked_val = unique_vals[counts_sorted[-2]]

    # Step 2: Find rows dominated by the marked value
    output_rows = []
    for r in range(nrows):
        uni_vals, cs = np.unique(input_grid[r], return_counts=True)
        most_freq_val = uni_vals[np.argmax(cs)]
        if most_freq_val == marked_val:
            output_rows.append(r)

    # Step 3: Find columns dominated by the marked value
    output_cols = []
    for c in range(ncols):
        uni_vals, cs = np.unique(input_grid[:, c], return_counts=True)
        most_freq_val = uni_vals[np.argmax(cs)]
        if most_freq_val == marked_val:
            output_cols.append(c)

    # Step 4: Find intersections where the cell is background
    output_corner_rows, output_corner_cols = set(), set()
    for r in output_rows:
        for c in output_cols:
            if input_grid[r, c] == background_val:
                output_corner_rows.add(r)
                output_corner_cols.add(c)

    # Step 5: Sort and crop
    output_corner_rows = sorted(output_corner_rows)
    output_corner_cols = sorted(output_corner_cols)

    # Step 6: Crop the grid to the bounding box
    output_grid = input_grid[
        output_corner_rows[0] : output_corner_rows[1] + 1,
        output_corner_cols[0] : output_corner_cols[1] + 1,
    ]

    return output_grid


def solve_f83cb3f6(input_grid):
    """
    Concepts: barrier-based sliding, directional movement toward barrier.

    Transformation: Slide all non-zero, non-8 values toward the nearest side of a continuous 8-barrier until adjacent,
    with any barrier gaps letting them fall off the grid.

    Transformation steps:
    1. Identify whether the barrier (8s) is vertical or horizontal.
    2. For each marked value (≠0, ≠8), slide it toward the nearest side of the barrier
       in its row/column until adjacent to an 8, stopping early if blocked by the grid edge
       or falling off through barrier gaps.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Find barrier position
    barrier_pos = np.argwhere(input_grid == 8)

    if len(barrier_pos) == 0:
        return input_grid.copy()

    # Check if barrier is vertical (same col) or horizontal (same row)
    if np.all(barrier_pos[:, 1] == barrier_pos[0, 1]):
        # Vertical barrier
        barrier_col = barrier_pos[0, 1]
        for r in range(nrows):
            if input_grid[r, barrier_col] != 8:  # skip gaps
                continue
            # Move from left
            for c in range(barrier_col - 1, -1, -1):
                if input_grid[r, c] != 0 and input_grid[r, c] != 8:
                    output_grid[r, barrier_col - 1] = input_grid[r, c]
                # Move from right
            for c in range(barrier_col + 1, input_grid.shape[1]):
                if input_grid[r, c] != 0 and input_grid[r, c] != 8:
                    output_grid[r, barrier_col + 1] = input_grid[r, c]
        output_grid[input_grid == 8] = 8

    elif np.all(barrier_pos[:, 0] == barrier_pos[0, 0]):
        # Horizontal barrier
        barrier_row = barrier_pos[0, 0]
        for c in range(ncols):
            if input_grid[barrier_row, c] != 8:
                continue
            # Move from above
            for r in range(barrier_row - 1, -1, -1):
                if input_grid[r, c] != 0 and input_grid[r, c] != 8:
                    output_grid[barrier_row - 1, c] = input_grid[r, c]
            # Move from below
            for r in range(barrier_row + 1, input_grid.shape[0]):
                if input_grid[r, c] != 0 and input_grid[r, c] != 8:
                    output_grid[barrier_row + 1, c] = input_grid[r, c]
        output_grid[input_grid == 8] = 8

    return output_grid


def solve_baf41dbf(input_grid):
    """
    Concepts: Region growth, without changing topology, the direction of marks until they are hit.

    Transformation steps:
    1. Identify connected components of 3s.
    2. Extend the grid of 3s outward in the direction of every mark 6 until it is hit.
    3. Ensure all interior rows and columns containing 3s are fully expanded.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Step 1: Identify rows and columns containing 6
    rows_with_6, cols_with_6 = np.where(input_grid == 6)

    def expand(grid, r, c):
        """
        Expands the region of 3s outward from the given row and column (r, c) of a mark 6.
        """
        rows_with_3, cols_with_3 = np.where(grid == 3)
        if len(rows_with_3) == 0 or len(cols_with_3) == 0:
            return grid  # No 3s to expand

        row_min_3, row_max_3 = rows_with_3.min(), rows_with_3.max()
        col_min_3, col_max_3 = cols_with_3.min(), cols_with_3.max()

        # Expand upwards
        if r < row_min_3:
            c_positions = np.where(grid[row_min_3 + 1] == 3)[0]
            cmin, cmax = c_positions.min(), c_positions.max()
            grid[row_min_3, cmin : cmax + 1] = 0  # Clear the original row
            grid[r + 1, cmin : cmax + 1] = 3  # Fill the row adjacent to the mark 6
            for cc in c_positions:
                grid[r + 1 : row_min_3 + 1, cc] = 3  # Fill the column-parts

        # Expand downwards
        if r > row_max_3:
            c_positions = np.where(grid[row_max_3 - 1] == 3)[0]
            cmin, cmax = c_positions.min(), c_positions.max()
            grid[row_max_3, cmin : cmax + 1] = 0  # Clear the original row
            grid[r - 1, cmin : cmax + 1] = 3  # Fill the row adjacent to the mark 6
            for cc in c_positions:
                grid[row_max_3:r, cc] = 3  # Fill the column-parts

        # Expand leftwards
        if c < col_min_3:
            r_positions = np.where(grid[:, col_min_3 + 1] == 3)[0]
            rmin, rmax = r_positions.min(), r_positions.max()
            grid[rmin : rmax + 1, col_min_3] = 0  # Clear the original column
            grid[rmin : rmax + 1, c + 1] = 3  # Fill the column adjacent to the mark 6
            for rr in r_positions:
                grid[rr, c + 1 : col_min_3 + 1] = 3  # Fill the row-parts

        # Expand rightwards
        if c > col_max_3:
            r_positions = np.where(grid[:, col_max_3 - 1] == 3)[0]
            rmin, rmax = r_positions.min(), r_positions.max()
            grid[rmin : rmax + 1, col_max_3] = 0  # Clear the original column
            grid[rmin : rmax + 1, c - 1] = 3  # Fill the column adjacent to the mark 6
            for rr in r_positions:
                grid[rr, col_max_3:c] = 3  # Fill the row-parts

        return grid

    # Step 2: Extend the grid of 3s outward in the direction of every mark 6 until it is hit
    for r, c in zip(rows_with_6, cols_with_6):
        output_grid = expand(output_grid, r, c)

    return output_grid


def solve_6cbe9eb8(input_grid):
    """
    Concepts:
    - Detect and extract rectangular frames (may be given in parts) or rectangular filled region.
    - Put these frames/filled regions into each other like russian dolls.

    Steps:
    1. Identify unique values in the input grid.
    2. For each unique value, determine if it forms a rectangular frame or a filled rectangle.
    3. Sort the identified frames/filled rectangles by size (area).
    4. Create an output grid that nests the largest rectangle first, followed by smaller ones
       in a top-left aligned manner.
    """
    input_grid = np.array(input_grid)

    unique_vals, _ = np.unique(input_grid, return_counts=True)

    def check_frame(pos):
        """Return True if `pos` belongs to different parts of a rectangular frame"""
        rows = [p[0] for p in pos]
        cols = [p[1] for p in pos]
        min_r, max_r = min(rows), max(rows)
        min_c, max_c = min(cols), max(cols)

        frame_positions = set()
        # Top and bottom edges
        for c in range(min_c, max_c + 1):
            frame_positions.add((min_r, c))
            frame_positions.add((max_r, c))
        # Left and right edges
        for r in range(min_r, max_r + 1):
            frame_positions.add((r, min_c))
            frame_positions.add((r, max_c))

        return frame_positions.intersection(set(map(tuple, pos))) == set(map(tuple, pos))

    def check_filled(pos):
        """Return True if `pos` forms a completely filled rectangle."""
        rows = [p[0] for p in pos]
        cols = [p[1] for p in pos]
        min_r, max_r = min(rows), max(rows)
        min_c, max_c = min(cols), max(cols)
        return len(pos) == (max_r - min_r + 1) * (max_c - min_c + 1)

    special_vals, positions, types = [], [], []

    for val in unique_vals:
        pos = np.argwhere(input_grid == val).tolist()
        if check_frame(pos):
            special_vals.append(val)
            positions.append(pos)
            types.append("frame")
        elif check_filled(pos):
            special_vals.append(val)
            positions.append(pos)
            types.append("filled")

    # Compute sizes for sorting by largest area
    sizes = []
    for pos in positions:
        rows = [p[0] for p in pos]
        cols = [p[1] for p in pos]
        sizes.append((max(rows) - min(rows) + 1, max(cols) - min(cols) + 1))

    sorted_indices = np.argsort([h * w for h, w in sizes])[::-1]  # largest area first

    largest_h, largest_w = sizes[sorted_indices[0]]
    output_grid = np.zeros(
        (largest_h, largest_w), dtype=int
    )  # Initialize output grid with zeros of size of largest component

    # Fill the output grid with the largest components first and then nest smaller components inside
    # all components are placed close to the top-left corner of the output grid
    indicator = 0
    for idx in sorted_indices:
        val = special_vals[idx]
        pos = positions[idx]
        kind = types[idx]

        rows = np.array([p[0] for p in pos])
        cols = np.array([p[1] for p in pos])
        min_r, max_r = rows.min(), rows.max()
        min_c, max_c = cols.min(), cols.max()
        height = max_r - min_r + 1
        width = max_c - min_c

        if kind == "filled":
            output_grid[
                largest_h - height - indicator : largest_h - indicator,
                indicator : width + 1 + indicator,
            ] = val
        else:  # frame
            top, bottom = largest_h - height - indicator, largest_h - 1 - indicator
            left, right = indicator, width + indicator
            output_grid[top, left:right] = val
            output_grid[bottom, left:right] = val
            output_grid[top : bottom + 1, left] = val
            output_grid[top : bottom + 1, right] = val
            indicator += 1

    return output_grid


# ===========================================================


def solve_f9012d9b(input_grid):
    """
    Concepts: translational symmetry, pattern completion

    Transformation steps:
    1. Find the smallest square non-zero tile that can generate the input grid (excluding the zero block) by tiling.
    2. Identify the bounding rectangle of the zero block.
    3. Extract the corresponding region from the tiled pattern and return it as the output (the missing pattern).
    """
    input_grid = np.array(input_grid)

    def find_min_square_tile(grid):
        """
        Find the smallest square non-zero block that can generate the entire input
        (excluding the rectangle with 0s) by tiling left-to-right and top-to-bottom.
        """
        grid = np.array(grid)
        nrows, ncols = grid.shape

        # Locate the zero block bounds
        zero_rows, zero_cols = np.where(grid == 0)
        if zero_rows.size > 0:
            rmin, rmax = zero_rows.min(), zero_rows.max() + 1
            cmin, cmax = zero_cols.min(), zero_cols.max() + 1
        else:
            rmin, rmax, cmin, cmax = nrows, nrows, ncols, ncols  # no zeros

        # Mask out the zero block
        mask = np.ones_like(grid, dtype=bool)
        mask[rmin:rmax, cmin:cmax] = False

        # Search for the minimal square size
        max_tile_size = min(nrows, ncols)
        for size in range(1, max_tile_size + 1):
            tile = grid[0:size, 0:size]
            if np.any(tile == 0):
                continue  # tile must be non-zero

            # Build tiled grid
            reps_row = -(-nrows // size)  # ceil division
            reps_col = -(-ncols // size)
            tiled = np.tile(tile, (reps_row, reps_col))[:nrows, :ncols]

            # Compare only where mask is True (ignore 0-block)
            if np.all(tiled[mask] == grid[mask]):
                return tile, tiled

        return None, None  # no valid tile found

    # Find the minimal square tile that can generate the input grid
    tile, tiled = find_min_square_tile(input_grid)
    # Locate zero block bounds
    zero_rows, zero_cols = np.where(input_grid == 0)
    rmin, rmax = zero_rows.min(), zero_rows.max() + 1
    cmin, cmax = zero_cols.min(), zero_cols.max() + 1

    output_grid = tiled[rmin:rmax, cmin:cmax]
    return output_grid


def solve_4258a5f9(input_grid):
    """
    Concepts: padding, surrounding

    Steps:
    1. Find positions of non-background (non-zero) elements (5s) in the input grid.
    2. Padding of 1s: Surround each 5 with 1s in the output grid.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    # Find positions of non-background (non-zero) elements in the input grid
    rows, cols = np.where(input_grid != 0)

    # Padding of 1s: Surround each 5 with 1s in the output grid.
    for r, c in zip(rows, cols):
        output_grid[r, c + 1] = 1
        output_grid[r, c - 1] = 1
        output_grid[r + 1, c] = 1
        output_grid[r - 1, c] = 1
        output_grid[r + 1, c + 1] = 1
        output_grid[r + 1, c - 1] = 1
        output_grid[r - 1, c + 1] = 1
        output_grid[r - 1, c - 1] = 1

    return output_grid


def solve_d06dbe63(input_grid):
    """
    Concepts: Staircase pattern drawing

    Transformation steps:
    1. Identify the starting position (cells with value 8).
    2. From the starting position, draw staircase patterns:
       - Up and right (alternating steps)
       - Down and left (alternating steps)
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Step 1: Identify the starting position (cells with value 8).
    positions = np.argwhere(input_grid == 8)

    def draw_staircase_up_right(grid, r, c):
        nr, nc = r, c
        counter = 0
        while 0 <= nr < nrows and 0 <= nc < ncols:
            if counter % 2 == 0:
                grid[max(nr - 2, 0) : nr, nc] = 5  # Move Up
                nr -= 2
            else:
                grid[nr, nc + 1 : min(nc + 3, ncols)] = 5  # Move Right
                nc += 2
            counter += 1
        return grid

    def draw_staircase_down_left(grid, r, c):
        nr, nc = r, c
        counter = 0
        while 0 <= nr < nrows and 0 <= nc < ncols:
            if counter % 2 == 0:
                grid[nr + 1 : min(nr + 3, nrows), nc] = 5  # Move Down
                nr += 2
            else:
                grid[nr, max(nc - 2, 0) : nc] = 5  # Move Left
                nc -= 2
            counter += 1
        return grid

    # Step 2: From each starting position, draw the staircase patterns.
    for pos in positions:
        r, c = pos
        output_grid = draw_staircase_up_right(output_grid, r, c)
        output_grid = draw_staircase_down_left(output_grid, r, c)

    return output_grid


def solve_8403a5d5(input_grid):
    """
    Concepts: vertical repetition, alternating marker placement

    Description:
    Given a grid with a single marked value at the bottom,
    draw vertical bars of the marked value starting from that marked value column
    and repeating every 2 columns to the right. In the columns between bars,
    place a '5' alternately at the top and bottom rows.

    Transformation steps:
    1. Identify the marked value (non-zero) and its column position.
    2. Fill every second column from this position with the marked value.
    3. In the alternating columns, place a '5' at the top or bottom, switching each time.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Identify marked value and column
    marked_val = np.unique(input_grid[input_grid != 0])[0]
    marked_col = np.argwhere(input_grid == marked_val)[0][1]

    # Create bars and alternate 5 placement
    top = True
    for col in range(marked_col, ncols):
        if (col - marked_col) % 2 == 0:
            output_grid[:, col] = marked_val
        else:
            output_grid[0 if top else nrows - 1, col] = 5
            top = not top

    return output_grid


def solve_6e19193c(input_grid):
    """
    Concepts: adding tail to arrowheads

    Description:
    In the input, you will see several objects of the same color that are in
    an arrowhead shape and facing different directions.
    The goal is to find the directions of the arrowheads and draw its tail in the opposite
    direction until reaching the grid boundary.

    Transformation steps:
    1. Identify all cells containing the marked value (non-zero).
    2. Group these cells into connected components (arrowheads).
    3. For each arrowhead, determine its direction and add a diagonal tail in the opposite
    direction until reaching the grid boundary.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Step 1: Identify marked (non-zero) value and its positions
    marked_val = np.unique(input_grid[input_grid != 0])[0]
    positions = np.argwhere(input_grid == marked_val)

    def group_connected_positions(positions, connectivity=4):
        """
        Group positions into connected components.

        Args:
            positions (ndarray): Array of [row, col] positions.
            connectivity (int): 4 or 8 for neighbor definition.

        Returns:
            List of lists of positions (connected components).
        """
        positions = np.array(positions)
        visited = set()
        groups = []

        # Neighbor offsets
        if connectivity == 4:
            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        elif connectivity == 8:
            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        else:
            raise ValueError("Connectivity must be 4 or 8")

        pos_set = set(map(tuple, positions))

        for pos in pos_set:
            if pos not in visited:
                group = []
                stack = [pos]
                visited.add(pos)
                while stack:
                    r, c = stack.pop()
                    group.append([r, c])
                    for dr, dc in neighbors:
                        nbr = (r + dr, c + dc)
                        if nbr in pos_set and nbr not in visited:
                            visited.add(nbr)
                            stack.append(nbr)
                groups.append(group)
        return groups

    # Step 2: Group into arrowhead objects
    connected_parts = group_connected_positions(positions, connectivity=4)

    # Step 3: For each arrowhead, find direction and add a diagonal tail in the opposite direction until reaching the grid boundary.
    for arrowhead in connected_parts:
        rows = [pos[0] for pos in arrowhead]
        cols = [pos[1] for pos in arrowhead]
        unique_rows, count_row = np.unique(rows, return_counts=True)
        unique_cols, count_col = np.unique(cols, return_counts=True)
        arrowhead_row = unique_rows[np.argmax(count_row)]
        arrowhead_col = unique_cols[np.argmax(count_col)]

        # Estimate tail direction as the sum of vectors from center to all points
        tail_direction = np.sum(
            np.array(arrowhead) - np.array([arrowhead_row, arrowhead_col]), axis=0
        )
        arrowtail_row = arrowhead_row + 2 * tail_direction[0]
        arrowtail_col = arrowhead_col + 2 * tail_direction[1]

        for _ in range(max(nrows, ncols)):
            if 0 <= arrowtail_row < nrows and 0 <= arrowtail_col < ncols:
                output_grid[arrowtail_row, arrowtail_col] = marked_val
                arrowtail_row += tail_direction[0]
                arrowtail_col += tail_direction[1]
            else:
                break
    return output_grid


def solve_4c5c2cf0(input_grid):
    """
    Concepts: Flip around symmetry center

    Transformation steps:
    1. Locate the symmetric 3x3 block with a non-zero 'x'-shaped pattern.
    2. Find its center cell coordinates (r, c).
    3. Flip the grid vertically around row r and combine with the original using max.
    4. Flip the result horizontally around column c and combine with the previous output using max.
    5. Return the final output grid.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Step 1: Find center of 3x3 block containing non-zero 'x' pattern
    r, c = None, None
    for i in range(1, nrows - 1):
        for j in range(1, ncols - 1):
            block = input_grid[i - 1 : i + 2, j - 1 : j + 2]
            if (
                np.count_nonzero(block) > 0
                and block[0, 0] == block[0, 2] == block[2, 0] == block[2, 2] == block[1, 1] != 0
            ):
                r, c = i, j
                break
        if r is not None:
            break

    if r is None or c is None:
        # No symmetric block found, return input as is
        return output_grid

    # Step 3: Vertical flip around row r
    output_flippedud = np.flipud(output_grid)
    output_flippedud = np.roll(output_flippedud, shift=(r - (nrows - 1 - r)), axis=0)
    output_grid = np.maximum(output_grid, output_flippedud)

    # Step 4: Horizontal flip around col c
    output_flippedlr = np.fliplr(output_grid)
    output_flippedlr = np.roll(output_flippedlr, shift=(c - (ncols - 1 - c)), axis=1)
    output_grid = np.maximum(output_grid, output_flippedlr)

    return output_grid


def solve_025d127b(input_grid):
    """
    Concepts: translational symmetry, pattern shifting

    Transformation steps:
    1. Identify all unique non-zero values in the input grid.
    2. For each value, find all positions and compute their bounding box.
    3. Shift positions left if they are on the right/bottom edge of the bounding box.
    4. Place the shifted positions in a new grid.
    5. Finally, shift the entire grid left by one column.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    non_zero_vals = np.unique(input_grid[input_grid != 0])

    positions = []
    for val in non_zero_vals:
        pos = np.argwhere(input_grid == val)
        positions.append(pos)

    new_positions = []
    for pos in positions:
        max_row = max(p[0] for p in pos)
        max_col = max(p[1] for p in pos)

        new_pos = []
        for p in pos:
            if p[0] == max_row:
                new_pos.append([p[0], p[1] - 1])  # Shift left
            elif p[1] == max_col:
                new_pos.append([p[0], p[1] - 1])  # Shift left
            else:
                new_pos.append([p[0], p[1]])
        new_positions.append(new_pos)

    for val, pos in zip(non_zero_vals, new_positions):
        for p in pos:
            output_grid[p[0], p[1]] = val

    output_grid = np.roll(output_grid, shift=1, axis=1)  # Shift left by one column

    return output_grid


# ===========================================================


def solve_f0100645(input_grid):
    """
    Concepts: Stack parts on leftmost and rightmost sides based on their value (color).

    Aligns horizontally separated connected components on the leftmost and rightmost sides
    by shifting the nearest disconnected part toward the extreme part until they touch.

    Trasformation steps:
    1. Identify the unique values in the leftmost and rightmost columns.
    2. For each side, while multiple connected components exist for that side's value:
       - Shift the closest non-extreme component horizontally until it touches the extreme component.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    nrows, ncols = input_grid.shape

    # Most frequent value in the grid is considered the background
    vals, counts = np.unique(input_grid, return_counts=True)
    background_val = vals[np.argmax(counts)]

    left_value = np.unique(input_grid[:, 0])[0]
    right_value = np.unique(input_grid[:, -1])[0]

    def shift_component(value, direction, current_grid):
        """
        Shifts a non-extreme connected component toward the extreme side.
        direction = -1 for left, +1 for right
        """
        current_grid = current_grid.copy()
        positions = np.argwhere(current_grid == value)
        components = group_connected_positions(positions, connectivity=8)

        if len(components) <= 1:
            return current_grid, False

        # Choose extreme and moving parts based on direction
        if direction == -1:
            sort_key = lambda comp: min(c[1] for c in comp)  # smallest col first
        else:
            sort_key = lambda comp: max(c[1] for c in comp)  # largest col first

        sorted_indices = sorted(range(len(components)), key=lambda i: sort_key(components[i]))
        extreme_idx = sorted_indices[0 if direction == -1 else -1]
        moving_idx = sorted_indices[1 if direction == -1 else -2]

        extreme_part = set(map(tuple, components[extreme_idx]))
        moving_part = np.array(components[moving_idx])

        # Try shifting step by step until touching
        for shift in range(1, ncols):
            shifted_positions = moving_part + np.array([0, direction * shift])

            # Out of bounds check
            if direction == -1 and shifted_positions[:, 1].min() < 0:
                return current_grid, False
            if direction == 1 and shifted_positions[:, 1].max() >= ncols:
                return current_grid, False

            # Touching check
            if extreme_part & set(map(tuple, shifted_positions)):
                shift -= 1
                if shift <= 0:
                    return current_grid, False
                # Apply shift
                for r, c in moving_part:
                    current_grid[r, c] = background_val
                for r, c in moving_part + np.array([0, direction * shift]):
                    current_grid[r, c] = value
                return current_grid, True

        return current_grid, False

    # Process each side
    for value, direction in [(left_value, -1), (right_value, 1)]:
        changed = True
        while changed:
            output_grid, changed = shift_component(value, direction, output_grid)

    return output_grid


def solve_93b4f4b3(input_grid):
    """
    Concepts: Connected component matching based on their shapes.

    Fill the color (value) in the left part based from the right part by matching shapes.

    Transformation steps:
    2. Split the grid into left and right parts.
    3. Extract connected components from the right part with their values and normalize their positions.
    4. Match shapes and transfer values from the right part to corresponding empty spaces in the left part.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Convert input to a NumPy array
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Split the grid into left and right parts
    left_part = input_grid[:, : ncols // 2]
    right_part = input_grid[:, ncols // 2 :]

    # Initialize the output grid as a copy of the left part
    output_grid = left_part.copy()

    # Step 2: Extract unique non-background (non-zero) values from the right part
    unique_vals = np.unique(right_part[right_part != 0])

    # Step 2: Normalize positions of connected components in the right part
    positions_in_right = []
    for val in unique_vals:
        pos = np.argwhere(right_part == val)
        min_row, min_col = pos[:, 0].min(), pos[:, 1].min()
        pos_norm = pos - np.array([min_row, min_col])
        positions_in_right.append(pos_norm)

    # Find empty spaces (with 0s) in the left part
    empty_positions = np.argwhere(left_part == 0)
    empty_parts = group_connected_positions(empty_positions, connectivity=8)

    # Step 3: Match shapes and transfer values from the right part to the left part
    for empty_part in empty_parts:
        empty_part = np.array(empty_part)
        min_row, min_col = empty_part[:, 0].min(), empty_part[:, 1].min()
        empty_norm = empty_part - np.array([min_row, min_col])

        for val, pos_norm in zip(unique_vals, positions_in_right):
            if set(map(tuple, pos_norm)) == set(map(tuple, empty_norm)):
                for r, c in empty_part:
                    output_grid[r, c] = val

    return output_grid


def solve_ff72ca3e(input_grid):
    """
    Concepts: BFS region growth, obstacle blocking.

    Breadth-First Search (BFS) — it’s a graph traversal algorithm.
    In simple terms:
    You start at a point (like your 4 cell).
    You visit all the neighbors at distance 1 first,
    Then all neighbors at distance 2,
    And so on — layer by layer.

    It’s like dropping a pebble in water — the ripples expand outward evenly,

    Transformation steps:
    1. For each cell containing the value 4, expand outward.
    2. Mark expansion cells with the value 2 until a cell containing 5 is reached, which blocks further growth.
    """
    # Convert input to a NumPy array and initialize variables
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Step 1: Find all positions containing the value 4
    positions_with_4 = np.argwhere(input_grid == 4)

    # Process each position containing 4
    for pos in positions_with_4:
        row, col = tuple(pos)

        # Expand outward from the current position
        for radius in range(1, max(nrows, ncols)):
            min_row, max_row = row - radius, row + radius
            min_col, max_col = col - radius, col + radius

            # Check bounds and ensure no blocking cell (value 5) is within the expansion area
            if (
                0 <= min_row < nrows
                and 0 <= min_col < ncols
                and 0 <= max_row < nrows
                and 0 <= max_col < ncols
                and not np.any(input_grid[min_row : max_row + 1, min_col : max_col + 1] == 5)
            ):
                # Collect positions to mark in the current expansion radius
                pad_positions = set()
                for c in [min_col, max_col]:
                    pad_positions.update((r, c) for r in range(min_row, max_row + 1))
                for r in [min_row, max_row]:
                    pad_positions.update((r, c) for c in range(min_col, max_col + 1))

                # Step 2: Mark the positions with the value 2
                for r, c in pad_positions:
                    output_grid[r, c] = 2
            else:
                # Stop expansion if bounds are exceeded or a blocking cell is encountered
                break

    return output_grid


def solve_50f325b5(input_grid):
    """
    Concepts: Pattern growth, template matching, multi-directional filling.

    Transformation steps:
    1. Identify all positions with value 8 and normalize their coordinates.
    2. For each possible placement in the grid, check if the normalized template fits and is surrounded by value 3.
    3. If so, fill the template region with 8.
    4. Repeat the process after rotating and transposing the grid to cover all directions.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find and normalize all positions with value 8
    pos_with_8 = np.argwhere(input_grid == 8)
    if pos_with_8.size == 0:
        return output_grid
    min_row, min_col = pos_with_8.min(axis=0)
    template = pos_with_8 - np.array([min_row, min_col])

    def fill_template(grid):
        nrows, ncols = grid.shape
        for r in range(nrows):
            for c in range(ncols):
                pos = template + np.array([r, c])
                # Check if template fits within grid bounds
                if (
                    pos[:, 0].min() < 0
                    or pos[:, 0].max() >= nrows
                    or pos[:, 1].min() < 0
                    or pos[:, 1].max() >= ncols
                ):
                    continue
                # Check if all positions in template are surrounded by value 3
                values = [output_grid[p[0], p[1]] for p in pos]
                if len(set(values)) == 1 and values[0] == 3:
                    for p in pos:
                        grid[p[0], p[1]] = 8
        return grid

    # Apply filling in all four rotations and both transposes
    for _ in range(4):
        output_grid = fill_template(output_grid)
        output_grid = np.rot90(output_grid)
    output_grid = np.transpose(output_grid)
    output_grid = fill_template(output_grid)
    output_grid = np.transpose(output_grid)

    return output_grid


def solve_46c35fc7(input_grid):
    """
    Concepts: Connected component extraction, block rotation, selective masking.

    Transformation steps:
    1. Identify non-background regions using connected components.
    2. For each 3x3 block, mask and rotate corners and edges separately.
    3. Combine rotated blocks and restore the center value.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    background_val = 7
    positions = np.argwhere(input_grid != background_val)

    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Group non-background positions into connected components
    parts = group_connected_positions(positions, connectivity=4)
    for part in parts:
        part = np.array(part)
        min_row, min_col = part.min(axis=0)
        max_row, max_col = part.max(axis=0)
        block = output_grid[min_row : max_row + 1, min_col : max_col + 1]

        # Define indices for corners and edges in a 3x3 block
        corner_indices = [(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)]
        edge_indices = [(0, 1), (1, 0), (1, 2), (2, 1), (1, 1)]

        # Mask and rotate corners
        corner_block = block.copy()
        for r, c in edge_indices:
            corner_block[r, c] = 0
        corner_block = np.rot90(corner_block)

        # Mask and rotate edges
        edge_block = block.copy()
        for r, c in corner_indices:
            edge_block[r, c] = 0
        edge_block = np.rot90(edge_block, k=-1)

        # Combine rotated blocks and restore center
        output_block = corner_block + edge_block
        output_block[1, 1] = block[1, 1]

        output_grid[min_row : max_row + 1, min_col : max_col + 1] = output_block

    return output_grid


def solve_60a26a3e(input_grid):
    """
    Concepts: object of certain shape and it center detection, line filling, connecte component.

    Transformation steps:
    1. Find all positions with value 2 and group them into connected components (8-connectivity).
    2. For each component, compute its center.
    3. For all centers sharing the same row, fill horizontal lines between them with value 1 (excluding endpoints).
    4. For all centers sharing the same column, fill vertical lines between them with value 1 (excluding endpoints).
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    positions = np.argwhere(input_grid == 2)
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Step 1: Group positions into connected components (they will be of same shape like +)
    parts = group_connected_positions(positions, connectivity=8)

    # Step 2: Compute centers of each component
    centers = []
    for part in parts:
        part = np.array(part)
        min_row, min_col = part.min(axis=0)
        max_row, max_col = part.max(axis=0)
        center_row = (min_row + max_row) // 2
        center_col = (min_col + max_col) // 2
        centers.append([center_row, center_col])

    centers = np.array(centers)
    cen_rows = np.unique(centers[:, 0])
    cen_cols = np.unique(centers[:, 1])

    # Step 3: Fill horizontal lines between centers in the same row
    for r in cen_rows:
        r_pos = np.where(centers[:, 0] == r)[0]
        if r_pos.size > 1:
            r_cen = centers[r_pos]
            sorted_idx = np.lexsort((r_cen[:, 1], r_cen[:, 0]))
            r_cen = r_cen[sorted_idx]
            for i in range(len(r_cen) - 1):
                cen1, cen2 = r_cen[i], r_cen[i + 1]
                min_c, max_c = min(cen1[1], cen2[1]), max(cen1[1], cen2[1])
                output_grid[r, min_c + 2 : max_c - 1] = 1

    # Step 4: Fill vertical lines between centers in the same column
    for c in cen_cols:
        c_pos = np.where(centers[:, 1] == c)[0]
        if c_pos.size > 1:
            c_cen = centers[c_pos]
            sorted_idx = np.lexsort((c_cen[:, 1], c_cen[:, 0]))
            c_cen = c_cen[sorted_idx]
            for i in range(len(c_cen) - 1):
                cen1, cen2 = c_cen[i], c_cen[i + 1]
                min_r, max_r = min(cen1[0], cen2[0]), max(cen1[0], cen2[0])
                output_grid[min_r + 2 : max_r - 1, c] = 1

    return output_grid


def solve_14754a24(input_grid):
    """
    Concepts: Cross (+) shape detection and completion.

    Transformation steps:
    1. Identify positions with value 4 and group them into connected components (8-connectivity).
    2. For each component, determine possible 3x3 boxes that can contain the cross shape.
    3. Identify missing positions in the cross shape and fill them with value 2 if the surrounding positions are valid (value 5).
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    positions = np.argwhere(input_grid == 4)
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Step 1: Group positions into connected components
    parts = group_connected_positions(positions, connectivity=8)

    def complete_plus_boxes(given_positions):
        """
        given_positions: List of (row, col) absolute coordinates.
        Returns: List of dicts with keys:
            - "box": (r0, c0) top-left of 3x3 box.
            - "missing": Set of absolute coordinates needed to complete the cross.
        """
        PLUS = {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}  # Local 3x3 coordinates of cross shape.

        given_positions = set(map(tuple, given_positions))
        results = []

        # Bounding box of given positions
        rows = [r for r, c in given_positions]
        cols = [c for r, c in given_positions]
        min_r, max_r = min(rows), max(rows)
        min_c, max_c = min(cols), max(cols)

        # Possible 3x3 boxes that can contain all given positions
        for r0 in range(max_r - 2, min_r + 1):  # Top-left row
            for c0 in range(max_c - 2, min_c + 1):  # Top-left column
                box = (r0, c0)
                # Map given positions to local 3x3 coordinates
                local = {(r - r0, c - c0) for r, c in given_positions}
                if local.issubset(PLUS):
                    # Find missing coordinates
                    missing_local = PLUS - local
                    missing_global = {(r0 + r, c0 + c) for r, c in missing_local}
                    results.append({"box": box, "missing": missing_global})
        return results

    # Step 2: Process each connected component
    for part in parts:
        res = complete_plus_boxes(part)
        for box_info in res:
            missing_positions = box_info["missing"]
            # Filter valid positions in the grid
            valid_positions = [
                input_grid[p[0], p[1]]
                for p in missing_positions
                if 0 <= p[0] < nrows and 0 <= p[1] < ncols
            ]

            # Step 3: Fill missing positions if all are valid (value 5)
            if np.all(np.array(valid_positions) == 5):
                for p in missing_positions:
                    if 0 <= p[0] < nrows and 0 <= p[1] < ncols and input_grid[p[0], p[1]] == 5:
                        output_grid[p[0], p[1]] = 2

    return output_grid


def solve_fc4aaf52(input_grid):
    """
    Concepts: color flipping, grid partitioning, and connected component analysis.

    Transformation steps:
    1. Initialize output with background (8).
    2. Flip non-background colors.
    3. Split into top and bottom halves around the vertical midpoint of non-background cells.
    4. Shift the top half horizontally until top+bottom form more than one connected component.
    5. Return the last valid connected configuration.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    background = 8

    # Step 1: initialize with background
    output_grid = np.full((nrows, ncols), background)

    # Step 2: flip non-background values (colors)
    values = np.unique(input_grid[input_grid != background])
    if len(values) > 0:
        mapping = {v: values[(i + 1) % len(values)] for i, v in enumerate(values)}
        for r, c in np.argwhere(input_grid != background):
            output_grid[r, c] = mapping[input_grid[r, c]]

    # Step 3: split into top and bottom halves
    non_bg_positions = np.argwhere(output_grid != background)
    min_r, max_r = non_bg_positions[:, 0].min(), non_bg_positions[:, 0].max()
    mid = (min_r + max_r) // 2
    top, bottom = output_grid[: mid + 1], output_grid[mid + 1 :]

    # Step 4 + 5: shift top horizontally, track connectivity
    for _ in range(ncols):
        candidate = np.vstack((top, bottom))
        positions = np.argwhere(candidate != background)
        pieces = group_connected_positions(positions, connectivity=8)

        if len(pieces) == 1:  # valid fully connected
            output_grid = candidate
        else:  # connectivity breaks → stop
            break

        # cyclic right shift of top
        top = np.hstack((top[:, -1:], top[:, :-1]))

    return output_grid


def solve_4ff4c9da(input_grid):
    """
    Concepts: disconnected components, shape matching and value transfer

    Transformation steps:
    1. Identify shapes formed by the marked value (8), normalize them.
    2. Identify the non-zero and non-8 value that has more than one disconnected component
    3. If any disconnected part matches the normalized shape of 8,
       replace that part's value with 8 in the output grid.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Collect unique non-zero values (excluding background 0 and marker 8)
    unique_vals = set(input_grid[input_grid != 0])
    marked_value = 8
    if marked_value in unique_vals:
        unique_vals.remove(marked_value)

    # Step 1: Normalize shapes of 8s
    pos_with_8 = np.argwhere(input_grid == marked_value)
    parts_with_8 = group_connected_positions(pos_with_8)

    parts_with_8_norm = set()
    for part in parts_with_8:
        part = np.array(part)
        min_row, min_col = part[:, 0].min(), part[:, 1].min()
        part_norm = part - np.array([min_row, min_col])
        parts_with_8_norm.add(frozenset(map(tuple, part_norm)))  # frozenset for hashability

    # Step 2 & 3: Find disconnected parts of the non-zero and non-8 value that has more than one disconnected component
    for val in unique_vals:
        pos_with_val = np.argwhere(input_grid == val)
        parts = group_connected_positions(pos_with_val)

        # Only consider that value if it has more than one disconnected component
        if len(parts) > 1:
            for part in parts:
                part = np.array(part)
                min_row, min_col = part[:, 0].min(), part[:, 1].min()
                part_norm = part - np.array([min_row, min_col])
                if frozenset(map(tuple, part_norm)) in parts_with_8_norm:
                    # Replace matched part with marker 8
                    for r, c in part:
                        output_grid[r, c] = marked_value

    return output_grid


def solve_305b1341(input_grid):
    """
    Concepts: Value mapping and neighborhood transformation.

    Transformation steps:
    1. Identify unique values in the grid that appear more than once, excluding zeros.
    2. Extract a mapping grid from top-left corner of the input grid.
    3. Replace values in the neighboring cells based on the mapping.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Step 1: Identify unique values with counts greater than 1, excluding zeros
    unique, counts = np.unique(input_grid, return_counts=True)
    unique_vals = unique[counts > 1]
    unique_vals = unique_vals[unique_vals != 0]

    # Step 2: Extract a mapping grid from top-left corner of the input grid
    num_unique_vals = len(unique_vals)
    map_grid = input_grid[:num_unique_vals, :2]

    # Clear the mapping region in the output grid
    output_grid[:num_unique_vals, :2] = 0
    input_without_map = input_grid.copy()
    input_without_map[:num_unique_vals, :2] = 0

    # Step 3: Replace values in the neighboring cells based on the mapping.
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(num_unique_vals):
        val_to_replace = map_grid[i, 0]
        replacement_val = map_grid[i, 1]
        positions = np.argwhere(input_without_map == val_to_replace)

        for pos in positions:
            r, c = pos[0], pos[1]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    if output_grid[nr, nc] == 0:
                        output_grid[nr, nc] = replacement_val

    return output_grid


def solve_fe45cba4(input_grid):
    """
    Concepts: fit key into its lock by matching patterns and number (color)

    Transformation steps:
    1. Identify left 'key' region and right 'lock' region by distinct numbers.
    2. Slide/extend the key shape horizontally and vertically until it perfectly fills the lock cavity.
    3. Replace overlaps so the joined pattern has no gaps.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    background_val = 7
    unique_values = np.unique(input_grid[input_grid != background_val])

    for val in unique_values:
        # Find connected parts for the current value
        positions = np.argwhere(input_grid == val)
        parts = group_connected_positions(positions)

        # Only proceed if there are multiple (two) disconnected parts
        if len(parts) > 1:
            key_shape, key_height, key_width = None, None, None

            # Identify the key (the part touching the left edge)
            for part in parts:
                part = np.array(part)
                min_row, min_col = np.min(part, axis=0)
                max_row, max_col = np.max(part, axis=0)

                if min_col == 0:  # leftmost part → key
                    # Remove the key from the output grid temporarily
                    for r, c in part:
                        output_grid[r, c] = background_val

                    # Normalize key coordinates relative to top-left corner
                    key_shape = part - np.array([min_row, min_col])
                    key_height = max_row - min_row + 1
                    key_width = max_col - min_col + 1
                    break  # found the key, no need to check others

            if key_shape is None:
                continue  # no valid key found

            initial_output = output_grid.copy()

            # Try sliding the key over possible positions
            for r in range(nrows - key_height + 1):
                for c in range(ncols - key_width + 1):
                    candidate_positions = key_shape + np.array([r, c])
                    max_row = candidate_positions[:, 0].max()

                    # Place the key temporarily
                    for rr, cc in candidate_positions:
                        output_grid[rr, cc] = val

                    # Check if key fits perfectly (lock is filled without gaps)
                    block = output_grid[r : max_row + 1, c:]
                    if np.all(block == val):
                        return output_grid  # successful fit

                    # Reset and try next position
                    output_grid = initial_output.copy()

    return output_grid


def solve_f9d67f8b(input_grid):
    """
    Concepts: mirror symmetry detection and masked value filling based on mirror symmetry and rotation.

    Transformation steps:
    1. Detect vertical and horizontal mirror symmetry axes (if they exist).
    2. Fill cells with the mask value (9) using their mirror counterparts along the symmetry axes.
    3. If any mask values remain, apply rotation to fill them.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()
    mask_val = 9

    def fill_missing_part(input_grid, output_grid, mask_val=9):

        def find_vertical_symmetry(grid, mask_val=9):
            nrows, ncols = grid.shape
            for col in range(1, ncols - 1):
                left = grid[:, :col]
                right = grid[:, col:]
                width = min(left.shape[1], right.shape[1])

                left_part = left[:, -width:]
                right_part_flipped = np.flip(right[:, :width], axis=1)

                mask = (left_part == mask_val) | (right_part_flipped == mask_val)

                if np.all((left_part == right_part_flipped) | mask):
                    return col
            return None

        def find_horizontal_symmetry(grid, mask_val=9):
            nrows, ncols = grid.shape
            for row in range(1, nrows - 1):
                top = grid[:row, :]
                bottom = grid[row:, :]
                height = min(top.shape[0], bottom.shape[0])

                top_part = top[-height:, :]
                bottom_part_flipped = np.flip(bottom[:height, :], axis=0)

                mask = (top_part == mask_val) | (bottom_part_flipped == mask_val)

                if np.all((top_part == bottom_part_flipped) | mask):
                    return row
            return None

        # --- Fill vertical symmetry ---
        sym_col = find_vertical_symmetry(input_grid)
        if sym_col is not None:
            left = output_grid[:, :sym_col]
            right = output_grid[:, sym_col:]
            width = min(left.shape[1], right.shape[1])

            for r in range(nrows):
                for c in range(width):
                    lc = sym_col - width + c
                    rc = sym_col + (width - 1 - c)
                    if output_grid[r, lc] == mask_val and output_grid[r, rc] != mask_val:
                        output_grid[r, lc] = output_grid[r, rc]
                    elif output_grid[r, rc] == mask_val and output_grid[r, lc] != mask_val:
                        output_grid[r, rc] = output_grid[r, lc]

        # --- Fill horizontal symmetry ---
        sym_row = find_horizontal_symmetry(input_grid)
        if sym_row is not None:
            top = output_grid[:sym_row, :]
            bottom = output_grid[sym_row:, :]
            height = min(top.shape[0], bottom.shape[0])

            for r in range(height):
                tr = sym_row - height + r
                br = sym_row + (height - 1 - r)
                for c in range(ncols):
                    if output_grid[tr, c] == mask_val and output_grid[br, c] != mask_val:
                        output_grid[tr, c] = output_grid[br, c]
                    elif output_grid[br, c] == mask_val and output_grid[tr, c] != mask_val:
                        output_grid[br, c] = output_grid[tr, c]
        return output_grid, (sym_col, sym_row)

    output_grid, (sym_col, sym_row) = fill_missing_part(input_grid, output_grid, mask_val=9)

    # If these are still positions with 9 to be filled
    pos_with_9 = np.argwhere(output_grid == 9)

    if pos_with_9.size == 0:  # No positions with 9 found.
        return output_grid

    elif pos_with_9.size > 0:
        row_with_9, col_with_9 = set(pos_with_9[:, 0]), set(pos_with_9[:, 1])

        if 0 in row_with_9:  # 9s are in the top
            if sym_col > (ncols // 2):
                output_grid_rot = np.rot90(output_grid, k=-1)  # rotate clockwise (left -> top)
                for r, c in pos_with_9:
                    shifted_c = c - min(col_with_9) + ncols - sym_col - 3
                    output_grid[r, c] = output_grid_rot[r, shifted_c]
            else:
                output_grid_rot = np.rot90(
                    output_grid, k=1
                )  # rotate counter-clockwise (right -> top)
                for r, c in pos_with_9:
                    shifted_c = c - min(col_with_9) + ncols - sym_col - 3
                    output_grid[r, c] = output_grid_rot[r, shifted_c]

        if nrows - 1 in row_with_9:  # 9s are in the bottom
            if sym_col > (ncols // 2):
                output_grid_rot = np.rot90(output_grid, k=1)  # rotate counter-clockwise
                for r, c in pos_with_9:
                    shifted_c = c - min(col_with_9) + ncols - sym_col - 3
                    output_grid[r, c] = output_grid_rot[r, shifted_c]
            else:
                output_grid_rot = np.rot90(output_grid, k=-1)  # rotate clockwise (right -> bottom)
                for r, c in pos_with_9:
                    shifted_c = c - min(col_with_9) + ncols - sym_col - 3
                    output_grid[r, c] = output_grid_rot[r, shifted_c]

        if 0 in col_with_9:  # 9s are in the left
            if sym_row > (nrows // 2):
                output_grid_rot = np.rot90(
                    output_grid, k=1
                )  # rotate counter-clockwise (top -> left)
                for r, c in pos_with_9:
                    shifted_r = r - min(row_with_9) + nrows - sym_row - 3
                    output_grid[r, c] = output_grid_rot[shifted_r, c]
            else:
                output_grid_rot = np.rot90(output_grid, k=-1)  # rotate clockwise (bottom -> left)
                for r, c in pos_with_9:
                    shifted_r = r - min(row_with_9) + nrows - sym_row - 3
                    output_grid[r, c] = output_grid_rot[shifted_r, c]

        if ncols - 1 in col_with_9:  # 9s are in the right
            if sym_row > (nrows // 2):
                output_grid_rot = np.rot90(output_grid, k=-1)  # rotate clockwise (top -> right)
                for r, c in pos_with_9:
                    shifted_r = r - min(row_with_9) + nrows - sym_row - 3
                    output_grid[r, c] = output_grid_rot[shifted_r, c]
            else:
                output_grid_rot = np.rot90(
                    output_grid, k=1
                )  # rotate counter-clockwise (bottom -> right)
                for r, c in pos_with_9:
                    shifted_r = r - min(row_with_9) + nrows - sym_row - 3
                    output_grid[r, c] = output_grid_rot[shifted_r, c]

    return output_grid


def solve_67e8384a(input_grid):
    """
    Concepts: Grid flipping and concatenation (stacking)

    Transformation steps:
    1. Create three variants of the input grid:
       - Left-right flipped
       - Upside-down flipped
       - Both left-right and upside-down flipped
    2. Horizontally stack the original grid with its left-right flipped version to form the top half.
    3. Horizontally stack the upside-down flipped grid with the doubly flipped grid to form the bottom half.
    4. Vertically stack the top and bottom halves to produce the final output grid.
    """
    input_grid = np.array(input_grid)

    flipped_lr = np.fliplr(input_grid)  # Step 1: Left-right flip
    flipped_ud = np.flipud(input_grid)  # Step 1: Upside-down flip
    flipped_lr_ud = np.flipud(flipped_lr)  # Step 1: Left-right + upside-down flip

    # Step 2: Concatenate the original grid with the left-right flipped version
    top_half = np.hstack([input_grid, flipped_lr])
    # Step 3: Concatenate the upside-down flipped grid with the left-right + upside-down flipped version
    bottom_half = np.hstack([flipped_ud, flipped_lr_ud])
    # Step 4: Concatenate the top and bottom halves to form the final output grid
    output_grid = np.vstack([top_half, bottom_half])

    return output_grid


def solve_8731374e(input_grid):
    """
    Concepts: Majority filtering and largest rectangle detection, drawing horizontal and vertical lines.

    Transformation steps:
    1. Apply a majority filter to fill each cell with the most frequent value among its neighbors.
       - If no majority exists, fill with 0.
    2. Identify the largest axis-aligned rectangle in the grid where all cells have the same nonzero value.
    3. Extract the rectangle and fill rows and columns containing the least frequent value with that value.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    def majority_filter(grid, connectivity, threshold_counts):
        """
        Fill each cell with the majority value among itself and its neighbors.
        If no majority exists, fill with 0.
        """
        grid = np.array(grid)
        nrows, ncols = grid.shape
        output = np.zeros_like(grid)

        # Define neighbor offsets
        if connectivity == 4:
            neighbors = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
        elif connectivity == 8:
            neighbors = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1)]
        else:
            raise ValueError("connectivity must be 4 or 8")

        for r in range(nrows):
            for c in range(ncols):
                values = []
                for dr, dc in neighbors:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < nrows and 0 <= cc < ncols:
                        values.append(grid[rr, cc])
                unique, counts = np.unique(values, return_counts=True)
                max_count_pos = np.argmax(counts)
                max_counts = counts[max_count_pos]
                if max_counts > threshold_counts:
                    output[r, c] = unique[max_count_pos]
        return output

    def largest_rectangle_same_value(grid):
        """
        Finds the largest axis-aligned rectangle in the grid where all cells have the same nonzero value.

        Args:
            grid (2D array): numpy array

        Returns:
            (value, (r1, c1, r2, c2), area): value of the rectangle,
                                            top-left and bottom-right coordinates,
                                            and its area
        """
        grid = np.array(grid)
        nrows, ncols = grid.shape
        best_area = 0
        best_rect = None
        best_val = None

        # Check all values except 0
        unique_vals = np.unique(grid)
        unique_vals = unique_vals[unique_vals != 0]

        for val in unique_vals:
            # Create binary mask for this value
            mask = (grid == val).astype(int)

            # Solve "largest rectangle of 1s" in binary matrix using histogram method
            heights = np.zeros(ncols, dtype=int)
            for r in range(nrows):
                # Update histogram heights
                heights = heights + mask[r] if r > 0 else mask[r]

                # Reset heights where mask is 0
                heights = heights * mask[r]

                # Largest rectangle in histogram (standard stack algo)
                stack = []
                for c in range(ncols + 1):
                    h = heights[c] if c < ncols else 0
                    start = c
                    while stack and stack[-1][0] > h:
                        height, col = stack.pop()
                        area = height * (c - col)
                        if area > best_area:
                            best_area = area
                            best_val = val
                            best_rect = (r - height + 1, col, r, c - 1)
                        start = col
                    stack.append((h, start))

        return best_val, best_rect, best_area

    # Step 1: Apply majority filter
    output_grid = majority_filter(output_grid, connectivity=4, threshold_counts=2)

    # Step 2: Find the largest rectangle with the same value
    best_val, best_rect, best_area = largest_rectangle_same_value(output_grid)
    min_row, min_col, max_row, max_col = best_rect

    # Step 3: Extract the rectangle and fill rows/columns with the least frequent value
    output_grid = input_grid[min_row : max_row + 1, min_col : max_col + 1]
    unique_vals, counts = np.unique(output_grid[output_grid != 0], return_counts=True)
    least_frequent_val = unique_vals[np.argmin(counts)]
    positions = np.argwhere(output_grid == least_frequent_val)
    for r, c in positions:
        output_grid[r, :] = least_frequent_val
        output_grid[:, c] = least_frequent_val

    return output_grid


def solve_5ffb2104(input_grid):
    """
    Concepts: horizontally shift connected non-zero blocks (connectivity=4)
              to the right until they hit either the grid boundary
              or another non-zero block.

    Transformation steps:
    1. Identify connected non-zero blocks for each unique value.
    2. Process blocks in order of their rightmost column (rightmost first).
    3. For each block, compute the maximum feasible right shift.
    4. Clear original positions and place the block at its shifted location.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Step 1: Identify connected non-zero blocks
    non_zero_vals = np.unique(input_grid[input_grid != 0])
    all_parts = []
    max_cols = []
    for val in non_zero_vals:
        position = np.argwhere(input_grid == val)
        parts = group_connected_positions(position, connectivity=4)
        for part in parts:
            part = np.array(part)
            max_col = part[:, 1].max()  # Get the maximum column index of the part
            all_parts.append(part)
            max_cols.append(max_col)

    # Step 2: Process each block in the order: from rightmost to leftmost
    order = np.argsort(max_cols)[::-1]
    for i in order:
        part = all_parts[i]
        min_row, max_row = min(part[:, 0]), max(part[:, 0])
        max_col = max_cols[i]
        # If the block is already at the rightmost position, skip it
        if max_col == ncols - 1:
            continue
        else:  # Step 3: Compute maximum feasible right shift
            final_shift = 0
            for shift in range(1, ncols):
                if max_col + shift >= ncols:
                    break
                else:
                    if (
                        output_grid[min_row : max_row + 1, max_col + shift].any() != 0
                    ):  # Check for collisions
                        break
                    else:
                        final_shift += 1
            # Step 4: Apply shift
            for r, c in part:
                output_grid[r, c] = 0
                output_grid[r, c + final_shift] = input_grid[r, c]

    return output_grid


def solve_ecdecbb3(input_grid):
    """
    Concepts: Extend horizontal or vertical lines to the nearest columns or rows of specific value (8).

    Transformation steps:
    1. Identify positions of cells with values 2 and 8.
    2. Determine unique rows and columns containing the value 8.
    3. For each cell with value 2:
       - Extend horizontal or vertical lines to the nearest columns or rows with value 8.
       - Update surrounding cells of intersection with value 8.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Identify positions of cells with values 2 and 8
    pos_with_2 = np.argwhere(input_grid == 2)
    pos_with_8 = np.argwhere(input_grid == 8)

    # Determine unique rows and columns containing the value 8
    unique_rows_with_8 = np.sort(np.unique(pos_with_8[:, 0]))
    unique_cols_with_8 = np.sort(np.unique(pos_with_8[:, 1]))

    # Define directions for updating surrounding cells
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # Case 1: we have columns of 8s (horizontal extension)
    if len(unique_rows_with_8) > len(unique_cols_with_8):
        for r, c2 in pos_with_2:
            left_to_c2, right_to_c2 = -1, ncols
            for c8 in unique_cols_with_8:
                if c8 < c2 and c8 > left_to_c2:  # Find the nearest column of 8s to the left
                    left_to_c2 = c8
                elif c2 < c8 and c8 < right_to_c2:  # Find the nearest column of 8s to the right
                    right_to_c2 = c8

            # Extend horizontal line from 2 to the nearest column of 8s to the left
            if left_to_c2 != -1:
                output_grid[r, left_to_c2 : c2 + 1] = 2
                for (
                    dr,
                    dc,
                ) in directions:  # Update surrounding cells of the intersection with value 8.
                    rr, cc = r + dr, left_to_c2 + dc
                    if 0 <= rr < nrows and 0 <= cc < ncols:
                        output_grid[rr, cc] = 8
            # Extend horizontal line from 2 to the nearest column of 8s to the right
            if right_to_c2 != ncols:
                output_grid[r, c2 + 1 : right_to_c2 + 1] = 2
                for (
                    dr,
                    dc,
                ) in directions:  # Update surrounding cells of the intersection with value 8.
                    rr, cc = r + dr, right_to_c2 + dc
                    if 0 <= rr < nrows and 0 <= cc < ncols:
                        output_grid[rr, cc] = 8

    # Case 2: we have rows of 8s (vertical extension)
    elif len(unique_cols_with_8) > len(unique_rows_with_8):
        for r2, c in pos_with_2:
            top_to_r2, bottom_to_r2 = -1, nrows
            for r8 in unique_rows_with_8:
                if r8 < r2 and r8 > top_to_r2:  # Find the nearest row of 8s above
                    top_to_r2 = r8
                elif r2 < r8 and r8 < bottom_to_r2:  # Find the nearest row of 8s below
                    bottom_to_r2 = r8

            # Extend vertical line from 2 to the nearest row of 8s above
            if top_to_r2 != -1:
                output_grid[top_to_r2:r2, c] = 2
                for (
                    dr,
                    dc,
                ) in directions:  # Update surrounding cells of the intersection with value 8.
                    rr, cc = top_to_r2 + dr, c + dc
                    if 0 <= rr < nrows and 0 <= cc < ncols:
                        output_grid[rr, cc] = 8
            # Extend vertical line from 2 to the nearest row of 8s below
            if bottom_to_r2 != nrows:
                output_grid[r2 + 1 : bottom_to_r2 + 1, c] = 2
                for (
                    dr,
                    dc,
                ) in directions:  # Update surrounding cells of the intersection with value 8.
                    rr, cc = bottom_to_r2 + dr, c + dc
                    if 0 <= rr < nrows and 0 <= cc < ncols:
                        output_grid[rr, cc] = 8

    return output_grid


def solve_2037f2c7(input_grid):
    """
    Extracts two connected nonzero blocks from the grid, compares them,
    and outputs the minimal bounding subgrid highlighting differences.

    Steps:
    1. Identify connected nonzero components using `group_connected_positions`.
    2. Extract bounding blocks for each component.
    3. Compute elementwise difference between the two blocks.
    4. Extract the minimal subgrid containing differences.
    5. Return a grid filled with marker value (8) for differing positions.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)

    # Step 1: find connected components of nonzero entries
    positions = np.argwhere(input_grid != 0)
    parts = group_connected_positions(positions)
    if len(parts) < 2:
        raise ValueError("Expected at least two connected components.")

    # Step 2: extract blocks from bounding boxes
    blocks = []
    for part in parts[:2]:  # only need first two components
        part = np.array(part)
        min_row, min_col = part.min(axis=0)
        max_row, max_col = part.max(axis=0)
        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]
        blocks.append(block)

    block1, block2 = blocks

    # Ensure both blocks are the same shape
    if block1.shape != block2.shape:
        raise ValueError(f"Block shape mismatch: {block1.shape} vs {block2.shape}")

    # Step 3: compute elementwise differences
    diff_mask = (block1 != block2).astype(int)

    # Step 4: extract bounding subgrid of differences
    differing_positions = np.argwhere(diff_mask == 1)
    if differing_positions.size == 0:
        return np.zeros((1, 1), dtype=int)  # no differences found

    min_row, min_col = differing_positions.min(axis=0)
    max_row, max_col = differing_positions.max(axis=0)
    subgrid = diff_mask[min_row : max_row + 1, min_col : max_col + 1]

    # Step 5: highlight differences with marker value 8
    output_grid = subgrid * 8
    return output_grid


def solve_00dbd492(input_grid):
    """
    Concepts: ring detection, interior filling

    Steps:
    1. Identify connected rings of 2s.
    2. Compute bounding box and radius of each ring.
    3. Fill the enclosed interior with a value based on radius,
       while preserving the original center cell as it carries 2.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # find all connected rings formed by 2s
    rings = group_connected_positions(np.argwhere(input_grid == 2))

    for ring in rings:
        ring = np.array(ring)
        min_row, max_row = ring[:, 0].min(), ring[:, 0].max()
        min_col, max_col = ring[:, 1].min(), ring[:, 1].max()
        center_row, center_col = (min_row + max_row) // 2, (min_col + max_col) // 2
        radius = max(max_row - center_row, max_col - center_col) - 1

        # decide fill value by radius
        fill_map = {1: 8, 2: 4, 3: 3}
        if radius in fill_map:
            output_grid[min_row + 1 : max_row, min_col + 1 : max_col] = fill_map[radius]
            # restore center cell
            output_grid[center_row, center_col] = input_grid[center_row, center_col]

    return output_grid


def solve_9c1e755f(input_grid):
    """
    Concepts: Block replication using guide row or column of a particular value (5).

    Steps:
    1. Identify connected blocks of non-zero cells, the process each block independently.
    2. For each block, detect whether 5s form a boundary row or column.
    3. Extract the interior piece (non-0, non-5 values).
    4. Replicate the piece across the block in the direction suggested by the 5s.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    def fill_block(block):
        filled = block.copy()
        pos_5 = np.argwhere(block == 5)
        if pos_5.size == 0:
            return filled

        min_r5, min_c5 = pos_5.min(axis=0)
        max_r5, max_c5 = pos_5.max(axis=0)

        pos_core = np.argwhere((block != 0) & (block != 5))
        if pos_core.size == 0:
            return filled
        min_r, min_c = pos_core.min(axis=0)
        max_r, max_c = pos_core.max(axis=0)
        piece = block[min_r : max_r + 1, min_c : max_c + 1]

        h, w = piece.shape
        H, W = block.shape

        # Top row of 5s → tile piece downward
        if min_r5 == max_r5 == 0:
            reps = H // h
            tiled = np.tile(piece, (reps, W // w))[:H, :W]
            filled = np.vstack([block[min_r5, :].reshape(1, -1), tiled])

        # Bottom row of 5s → tile piece upward
        elif min_r5 == max_r5 == H - 1:
            reps = H // h
            tiled = np.tile(piece, (reps, W // w))[-H:, :W]
            filled = np.vstack([tiled, block[max_r5, :].reshape(1, -1)])

        # Left column of 5s → tile piece rightward
        elif min_c5 == max_c5 == 0:
            reps = W // w
            tiled = np.tile(piece, (H // h, reps))[:H, :W]
            filled = np.hstack([block[:, min_c5].reshape(-1, 1), tiled])

        # Right column of 5s → tile piece leftward
        elif min_c5 == max_c5 == W - 1:
            reps = W // w
            tiled = np.tile(piece, (H // h, reps))[:H, -W:]
            filled = np.hstack([tiled, block[:, max_c5].reshape(-1, 1)])

        return filled

    # Process each connected block
    for part in group_connected_positions(np.argwhere(input_grid != 0)):
        part = np.array(part)
        min_r, min_c = part.min(axis=0)
        max_r, max_c = part.max(axis=0)
        block = input_grid[min_r : max_r + 1, min_c : max_c + 1]
        filled_block = fill_block(block)
        output_grid[min_r : max_r + 1, min_c : max_c + 1] = filled_block

    return output_grid


def solve_37ce87bb(input_grid):
    """
    Concepts: Counting and marking based on cell values.

    Steps:
    1. Count the number of cells with value 8 and value 2.
    2. Compute the difference (num_5s = num_8s - num_2s).
    3. Fill the last 'num_5s' rows in the second-to-last column with 5.
    """

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Step 1: Find positions of 8s and 2s
    pos_with_8 = np.argwhere(input_grid == 8)
    pos_with_2 = np.argwhere(input_grid == 2)

    # Step 2: Count occurrences
    num_8s = pos_with_8.shape[0]
    num_2s = pos_with_2.shape[0]

    # Step 3: Compute number of 5s to fill
    num_5s = num_8s - num_2s

    # Step 4: Fill the last 'num_5s' rows in the second-to-last column with 5
    if num_5s > 0:
        output_grid[-num_5s:, -2] = 5

    return output_grid


def solve_6a11f6da(input_grid):
    """
    Concepts: grid partitioning into three parts, merged by overlapping.
    Non-zero values overwrite zeros sequentially.

    Steps:
    1. Split input grid into 3 equal vertical sections.
    2. Rearrange sections in order: last → first → second.
    3. Build output by filling zeros with values from each section in sequence.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    part_size = nrows // 3
    # Step 1 and 2: Partition rows into three equal parts and rearrange them in the order
    parts = [
        input_grid[2 * part_size :],  # last part
        input_grid[:part_size],  # first part
        input_grid[part_size : 2 * part_size],  # second part
    ]

    # Step 3: Build output by filling zeros with values from each section
    output_grid = np.zeros((part_size, ncols), dtype=input_grid.dtype)
    for part in parts:
        mask = output_grid == 0
        output_grid[mask] = part[mask]

    return output_grid


def solve_e760a62e(input_grid):
    """
    Concepts: grid partitioning with connectors.

    Steps:
    1. Find the first row and column fully filled with 8s (block size).
    2. Partition the grid into blocks of this size.
    3. Identify blocks containing 2 or 3.
    4. Connect same-valued blocks horizontally/vertically by filling paths.
    5. Overlaps of 2 and 3 become 6.
    """

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    nrows, ncols = input_grid.shape

    # Step 1: Block size from fully-8 row/col
    first_row_8 = next(r for r in range(nrows) if np.all(input_grid[r, :] == 8))
    first_col_8 = next(c for c in range(ncols) if np.all(input_grid[:, c] == 8))
    block_h, block_w = first_row_8, first_col_8

    # Step 2: Partition grid into blocks
    blocks_with_2, blocks_with_3 = [], []
    for r in range(0, nrows, block_h + 1):
        for c in range(0, ncols, block_w + 1):
            block = input_grid[r : r + block_h, c : c + block_w]
            if np.any(block == 2):
                blocks_with_2.append((r, c))
            elif np.any(block == 3):
                blocks_with_3.append((r, c))

    def fill_blocks(grid, val, block_corners):
        filled = []
        for r, c in block_corners:
            for rr, cc in block_corners:
                if r == rr and c != cc:  # horizontal connection
                    for cc_ in range(min(c, cc), max(c, cc) + 1, block_w + 1):
                        grid[r : r + block_h, cc_ : cc_ + block_w] = val
                        filled.append((r, cc_))
                elif c == cc and r != rr:  # vertical connection
                    for rr_ in range(min(r, rr), max(r, rr) + 1, block_h + 1):
                        grid[rr_ : rr_ + block_h, c : c + block_w] = val
                        filled.append((rr_, c))
        return grid, set(filled)

    # Step 3: Connect blocks with 2s and 3s
    output_grid, corners_2 = fill_blocks(output_grid, 2, blocks_with_2)
    output_grid, corners_3 = fill_blocks(output_grid, 3, blocks_with_3)

    # Step 4: Overlapping connections → 6
    for r, c in corners_2 & corners_3:
        output_grid[r : r + block_h, c : c + block_w] = 6

    return output_grid


def solve_ba97ae07(input_grid):
    """
    Concepts: Strip detection, intersection, and value flipping.

    Transformation steps:
    1. Identify non-zero values and determine if they form vertical or horizontal strips using bounding boxes.
    2. Find the intersection region of these strips.
    3. At the intersection, flip the values:
       - if vertical strip appears on top in the input, then horizontal strip will appear on top in the output, and vice versa.
    """

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    non_zero_vals = np.unique(input_grid[input_grid != 0])
    intersect_rows, intersect_cols = None, None

    # Detect strips and their bounding boxes
    for val in non_zero_vals:
        pos = np.argwhere(input_grid == val)
        min_r, max_r = pos[:, 0].min(), pos[:, 0].max()
        min_c, max_c = pos[:, 1].min(), pos[:, 1].max()

        if (max_r - min_r) > (max_c - min_c):  # vertical strip
            intersect_cols = np.arange(min_c, max_c + 1)
        else:  # horizontal strip
            intersect_rows = np.arange(min_r, max_r + 1)

    # Ensure intersection arrays are not None
    if intersect_rows is None or intersect_cols is None:
        return output_grid

    # Flip values at intersection
    for r in intersect_rows:
        for c in intersect_cols:
            if input_grid[r, c] == non_zero_vals[0]:
                output_grid[r, c] = non_zero_vals[1]
            elif input_grid[r, c] == non_zero_vals[1]:
                output_grid[r, c] = non_zero_vals[0]

    return output_grid


def solve_d93c6891(input_grid):
    """
    Concepts: Filling 7-blocks using available 5s attached in the direction opposite to the wall of 0s.

    Transformation steps:
    1. Extract connected components, ignoring 0s and 4s.
    2. For each component:
       - Identify bounding box of 7-blocks and count attached 5s.
       - Fill the 7-block with 5s in the direction opposite to the wall of 0s.
       - Change original 5s to 4s.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find positions not 0 or 4
    positions = np.argwhere((input_grid != 0) & (input_grid != 4))
    parts = group_connected_positions(positions)

    for part in parts:
        part = np.array(part)
        pos_with_7s = [p for p in part if input_grid[tuple(p)] == 7]
        pos_with_5s = [p for p in part if input_grid[tuple(p)] == 5]
        pos_with_7s = np.array(pos_with_7s)
        pos_with_5s = np.array(pos_with_5s)
        num_5s = len(pos_with_5s)

        if pos_with_7s.size == 0:
            continue

        min_row, min_col = np.min(pos_with_7s, axis=0)
        max_row, max_col = np.max(pos_with_7s, axis=0)

        # Fill direction logic
        if min_row > 0 and np.all(input_grid[min_row - 1, min_col : max_col + 1] == 0):
            counter = 0
            for r in range(min_row, max_row + 1):
                for c in range(min_col, max_col + 1):
                    if counter < num_5s:
                        output_grid[r, c] = 5
                        counter += 1
        elif max_row < input_grid.shape[0] - 1 and np.all(
            input_grid[max_row + 1, min_col : max_col + 1] == 0
        ):
            counter = 0
            for r in range(max_row, min_row - 1, -1):
                for c in range(min_col, max_col + 1):
                    if counter < num_5s:
                        output_grid[r, c] = 5
                        counter += 1
        elif min_col > 0 and np.all(input_grid[min_row : max_row + 1, min_col - 1] == 0):
            counter = 0
            for c in range(min_col, max_col + 1):
                for r in range(min_row, max_row + 1):
                    if counter < num_5s:
                        output_grid[r, c] = 5
                        counter += 1
        elif max_col < input_grid.shape[1] - 1 and np.all(
            input_grid[min_row : max_row + 1, max_col + 1] == 0
        ):
            counter = 0
            for c in range(max_col, min_col - 1, -1):
                for r in range(min_row, max_row + 1):
                    if counter < num_5s:
                        output_grid[r, c] = 5
                        counter += 1

        # Change original 5s to 4s
        if num_5s > 0 and pos_with_5s.size > 0:
            output_grid[pos_with_5s[:, 0], pos_with_5s[:, 1]] = 4

    return output_grid


def solve_7bb29440(input_grid):
    """
    Concepts: Extraction of minimal block with least non-1 values.

    Transformation steps:
    1. Identify all connected non-zero blocks in the grid.
    2. For each block, extract its bounding box.
    3. Count the number of cells in the box that are not 1.
    4. Return the block with the minimal count of non-1 cells.
    """

    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)

    # Step 1: Identify all connected non-zero blocks in the grid.
    positions = np.argwhere(input_grid != 0)
    parts = group_connected_positions(positions)

    min_count = float("inf")
    output_grid = None

    for part in parts:
        part = np.array(part)
        # Step 2: For each block, extract its bounding box.
        min_row, min_col = part.min(axis=0)
        max_row, max_col = part.max(axis=0)
        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]
        # Step 3: Count the number of cells in the box that are not 1.
        count_not_1 = np.sum(block != 1)
        # Step 4: If this block has fewer non-1 cells than the current minimum, update the output.
        if count_not_1 < min_count:
            min_count = count_not_1
            output_grid = block

    return output_grid


def solve_19bb5feb(input_grid):
    """
    Concepts: Bounding box detection, Subgrid extraction, Unique value identification,
    Anchor-based positioning, Canonical mapping (normalization to 2×2 grid

    Transformation steps:
    1. Find the bounding box of all cells with value 8.
    2. Extract the block within this bounding box.
    3. Identify all unique values in the block that are not 8.
    4. For each unique value, find its top-left position in the block.
    5. Place each value in the corresponding corner of a 2x2 output grid:
       - Top-left, Top-right, Bottom-left, Bottom-right.
    """

    input_grid = np.array(input_grid)

    # Step 1: Find the bounding box of all cells with value 8.
    pos_with_8 = np.argwhere(input_grid == 8)
    min_row, min_col = pos_with_8.min(axis=0)
    max_row, max_col = pos_with_8.max(axis=0)
    # Step 2: Extract the block within this bounding box.
    block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

    # Step 3: Identify all unique values in the block that are not 8.
    unique_vals = np.unique(block[block != 8])

    # Step 4: For each unique value, find its top-left position in the block.
    corners = []
    for val in unique_vals:
        pos = np.argwhere(block == val)
        min_r, min_c = pos.min(axis=0)
        corners.append([min_r, min_c])
    corners = np.array(corners)

    # Step 5: Place each value in the corresponding corner of a 2x2 output grid.
    output_grid = np.zeros((2, 2), dtype=int)
    min_r, min_c = corners.min(axis=0)
    max_r, max_c = corners.max(axis=0)
    for i, (r, c) in enumerate(corners):
        if r == min_r and c == min_c:
            output_grid[0, 0] = unique_vals[i]
        if r == min_r and c == max_c:
            output_grid[0, 1] = unique_vals[i]
        if r == max_r and c == min_c:
            output_grid[1, 0] = unique_vals[i]
        if r == max_r and c == max_c:
            output_grid[1, 1] = unique_vals[i]

    return output_grid


def solve_6ad5bdfd(input_grid):
    """
    Concepts: Shift connected non-zero blocks (connectivity=4) horizontally or vertically
    until they hit the grid boundary or another non-zero block.

    Transformation steps:
    1. Identify the direction to move (based on a row or column of 2s at the grid edge).
    2. Find all connected non-zero blocks for each unique value.
    3. Process blocks in the correct order for the direction.
    4. For each block, compute the maximum feasible shift.
    5. Clear original positions and place the block at its shifted location.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions, move_parts

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Determine movement direction from edge 2s
    pos_with_2 = np.argwhere(input_grid == 2)
    uniq_rows = np.unique(pos_with_2[:, 0])
    uniq_cols = np.unique(pos_with_2[:, 1])
    direction = None
    if uniq_cols.size == 1:
        if uniq_cols[0] == ncols - 1:
            direction = "left to right"
        elif uniq_cols[0] == 0:
            direction = "right to left"
    elif uniq_rows.size == 1:
        if uniq_rows[0] == nrows - 1:
            direction = "top to bottom"
        elif uniq_rows[0] == 0:
            direction = "bottom to top"

    # Find all connected non-zero blocks
    non_zero_vals = np.unique(input_grid[input_grid != 0])
    all_parts = []
    for val in non_zero_vals:
        positions = np.argwhere(input_grid == val)
        parts = group_connected_positions(positions, connectivity=4)
        for part in parts:
            all_parts.append(np.array(part))

    output_grid = move_parts(all_parts, direction, output_grid, input_grid)

    return output_grid


def solve_77fdfe62(input_grid):
    """
    Concepts: Cropping interior and corner-based value assignment.

    Crop interior region bounded by 1-filled rows/cols.
    Replace 8s with values from corresponding corners of input grid.

    Transformation steps:
    1. Identify all rows and columns fully filled with 1s.
    2. Initialize the output grid as the interior block bounded by these rows and columns.
    3. For each cell with value 8 in the cropped grid, assign a value from the corresponding corner of the input grid:
       - Top-left, Top-right, Bottom-left, Bottom-right.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    rows_with_1 = [r for r in range(nrows) if np.all(input_grid[r, :] == 1)]
    cols_with_1 = [c for c in range(ncols) if np.all(input_grid[:, c] == 1)]

    min_row, min_col = min(rows_with_1), min(cols_with_1)
    max_row, max_col = max(rows_with_1), max(cols_with_1)

    output_grid = input_grid[min_row + 1 : max_row, min_col + 1 : max_col]
    H, W = output_grid.shape

    pos_with_8 = np.argwhere(output_grid == 8)
    for r, c in pos_with_8:
        if r < H // 2 and c < W // 2:
            output_grid[r, c] = input_grid[0, 0]
        elif r < H // 2 and c >= W // 2:
            output_grid[r, c] = input_grid[0, -1]
        elif r >= H // 2 and c < W // 2:
            output_grid[r, c] = input_grid[-1, 0]
        else:
            output_grid[r, c] = input_grid[-1, -1]

    return output_grid


def solve_50cb2852(input_grid):
    """
    Concepts: Identify connected non-zero components and fill their interiors with 8s.

    Transformation steps:
    1. Find all connected non-zero components in the grid.
    2. For each component, fill its interior (excluding the border) with 8s.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Step 1: Find all connected non-zero components
    positions = np.argwhere(input_grid != 0)
    parts = group_connected_positions(positions)

    # Step 2: Fill the interior of each component with 8s
    for part in parts:
        part = np.array(part)
        row_min, col_min = part.min(axis=0)
        row_max, col_max = part.max(axis=0)
        # Fill interior (excluding border)
        output_grid[row_min + 1 : row_max, col_min + 1 : col_max] = 8

    return output_grid


def solve_cf5fd0ad(input_grid):
    """
    Concepts: duplication, rotation, and stacking of blocks.

    Transformation steps:
    1. Duplicate the input grid to form a larger block (bottom-right).
    2. Rotate this block to create top-right, top-left, and bottom-left blocks.
    3. Assemble the four blocks into a new grid by stacking and concatenation.
    """

    input_grid = np.array(input_grid)
    # Step 1: Create the bottom-right block by duplicating the input grid
    bottom_right_block = np.vstack(
        [np.hstack([input_grid, input_grid]), np.hstack([input_grid, input_grid])]
    )

    # Step 2: Generate rotated blocks for other corners
    top_right_block = np.rot90(bottom_right_block, k=-1)
    top_left_block = np.rot90(bottom_right_block, k=-2)
    bottom_left_block = np.rot90(bottom_right_block, k=1)

    # Step 3: Assemble the final output grid
    output_grid = np.vstack(
        [
            np.hstack([top_left_block, top_right_block]),
            np.hstack([bottom_left_block, bottom_right_block]),
        ]
    )

    return output_grid


def solve_d5d6de2d(input_grid):
    """
    Concepts: Connected component detection, interior filling, border clearing.

    Transformation steps:
    1. Identify all connected components of a unique non-zero value (2).
    2. For each component, fill its interior (excluding border) with 3.
    3. Set all border cells of the component to 0.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Step 1: Find the unique non-zero value and its positions
    unique_vals = np.unique(input_grid[input_grid != 0])
    if unique_vals.size == 0:
        return output_grid
    unique_val = unique_vals[0]
    positions = np.argwhere(input_grid == unique_val)

    # Step 2: Group connected positions
    parts = group_connected_positions(positions)

    # Step 3: For each part, fill interior with 3 and set border to 0
    for part in parts:
        part = np.array(part)
        min_row, min_col = part.min(axis=0)
        max_row, max_col = part.max(axis=0)
        # Fill interior (excluding border)
        if (max_row - min_row > 1) and (max_col - min_col > 1):
            output_grid[min_row + 1 : max_row, min_col + 1 : max_col] = 3
        # Set border cells to 0
        output_grid[part[:, 0], part[:, 1]] = 0

    return output_grid


def solve_b91ae062(input_grid):
    """
    Concepts: Grid expansion by unique value count.

    Transformation steps:
    1. Count unique non-zero values in the input grid.
    2. Expand the grid by duplicating each cell into a block of size (num_unique_val x num_unique_val).
    3. Fill each block with the original cell value.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Find the unique non-zero value and its positions
    unique_vals = np.unique(input_grid[input_grid != 0])
    num_unique_val = unique_vals.size

    # Step 2: Create the output grid
    output_grid = np.zeros((num_unique_val * nrows, num_unique_val * ncols), dtype=int)
    for r in range(nrows):
        for c in range(ncols):
            # Step 3: Fill each block with the original cell value
            output_grid[
                r * num_unique_val : (r + 1) * num_unique_val,
                c * num_unique_val : (c + 1) * num_unique_val,
            ] = input_grid[r, c]

    return output_grid


def solve_d037b0a7(input_grid):
    """
    Concepts: Column filling below non-zero values.

    Transformation steps:
    1. For each unique non-zero value in the grid:
       a. For every cell containing that value, fill all cells below in the same column with that value.
    """

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    non_zero_vals = np.unique(input_grid[input_grid != 0])
    for val in non_zero_vals:
        positions = np.argwhere(input_grid == val)
        for r, c in positions:
            output_grid[r:, c] = val

    return output_grid


def solve_93b581b8(input_grid):
    """
    Concepts: 2x2 grid of non-zero value detection, putting 2x2 grids or their parts outside the bounding box,
    where value is from diagonally opposite corners.

    Transformation steps:
    1. Find the 2x2 box of all non-zero cells in the input grid.
    2. Assign specific values to four clipped regions outside the bounding box corners:
       - Top-left, top-right, bottom-left, bottom-right.
       - Values are taken from the diagonally opposite corners of the bounding box.
    """

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Step 1: Find bounding box of non-zero cells
    positions = np.argwhere(input_grid != 0)
    min_row, min_col = positions.min(axis=0)
    max_row, max_col = positions.max(axis=0)

    # Step 2: Assign values to clipped regions around bounding box corners
    def assign_clip(grid, r0, r1, c0, c1, val):
        rs, re = max(0, r0), min(grid.shape[0], r1)
        cs, ce = max(0, c0), min(grid.shape[1], c1)
        if rs < re and cs < ce:
            grid[rs:re, cs:ce] = val

    assign_clip(
        output_grid, min_row - 2, min_row, min_col - 2, min_col, input_grid[max_row, max_col]
    )  # Top-left
    assign_clip(
        output_grid, min_row - 2, min_row, max_col + 1, max_col + 3, input_grid[max_row, min_col]
    )  # Top-right
    assign_clip(
        output_grid, max_row + 1, max_row + 3, min_col - 2, min_col, input_grid[min_row, max_col]
    )  # Bottom-left
    assign_clip(
        output_grid,
        max_row + 1,
        max_row + 3,
        max_col + 1,
        max_col + 3,
        input_grid[min_row, min_col],
    )  # Bottom-right

    return output_grid


def solve_292dd178(input_grid):
    """
    Concepts: Source is emitting substance (2)

    Transformation steps:
    1. Find connected blocks of 1s that form sources
    2. Fill their interior with 2s (substance)
    3. Detect the opening (cell with most frequent background value).
    4. Extend 2s as a stream of substance from the opening outward till the grid boundary is reached.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    values, counts = np.unique(input_grid, return_counts=True)
    background = values[np.argmax(counts)]  # most frequent value

    positions = np.argwhere(input_grid == 1)
    parts = group_connected_positions(positions)

    for part in parts:
        part = np.array(part)
        min_row, min_col = part.min(axis=0)
        max_row, max_col = part.max(axis=0)

        # fill interior
        output_grid[min_row + 1 : max_row, min_col + 1 : max_col] = 2

        block = output_grid[min_row : max_row + 1, min_col : max_col + 1]
        r, c = np.argwhere(block == background)[0]  # opening position

        if r == 0:
            output_grid[: min_row + 1, min_col + c] = 2  # stream of 2s from the opening to the top
        elif c == 0:
            output_grid[min_row + r, : min_col + 1] = 2  # stream of 2s from the opening to the left
        elif r == block.shape[0] - 1:
            output_grid[min_row + r :, min_col + c] = (
                2  # stream of 2s from the opening to the bottom
            )
        elif c == block.shape[1] - 1:
            output_grid[min_row + r, min_col + c :] = (
                2  # stream of 2s from the opening to the right
            )

    return output_grid


def solve_1d61978c(input_grid):
    """
    Concepts: Connected component analysis, mathematical property detection, component labeling.

    Steps:
    1. Find all connected groups of cells with value 5 (using 8-connectivity).
    2. For each group:
       - If its size is a power of an integer (a^b, a > 1, b > 1) or exactly 2, set those cells to 2.
       - Otherwise, set those cells to 8.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    positions = np.argwhere(input_grid == 5)
    parts = group_connected_positions(positions, connectivity=8)

    def is_power(n):
        """Check if n is a power a^b with a > 1, b > 1."""
        if n <= 1:
            return False
        max_base = int(np.sqrt(n)) + 1
        for base in range(2, max_base + 1):
            exp = np.round(np.log(n) / np.log(base))
            if base**exp == n and exp > 1:
                return True
        return False

    for part in parts:
        part = np.array(part)
        n = len(part)
        output_grid[part[:, 0], part[:, 1]] = 2 if is_power(n) or n == 2 else 8

    return output_grid


def solve_d2abd087(input_grid):
    """
    Concepts: Connected component labeling based on number of cells.

    Transformation Steps:
    1. Identify all connected groups of cells with value 5 (using 8-connectivity).
    2. For each group:
       - If the group size is 6, set those cells to 2.
       - Otherwise, set those cells to 1.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    positions = np.argwhere(input_grid == 5)
    parts = group_connected_positions(positions, connectivity=8)

    for part in parts:
        part = np.array(part)
        value = 2 if len(part) == 6 else 1
        output_grid[part[:, 0], part[:, 1]] = value

    return output_grid


def solve_825aa9e9(input_grid):
    """
    Concepts:
    - Identify connected components above a stopper row.
    - Gravity: Drop each component downward until it lands on either a row above the stopper value
      or another identical component.

    Steps:
    1. Find stopper value from bottom row (other than background value 7).
    2. Collect connected components (excluding 7 and stopper).
    3. Process components from bottom to top.
    4. Drop each component until it meets stopper or same value.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # stopper value (from bottom row, not 7)
    bottom_row = input_grid[-1, :]
    stopper_val = np.unique(bottom_row[bottom_row != 7])[0]

    # connected components excluding 7 and stopper
    positions = np.argwhere((input_grid != 7) & (input_grid != stopper_val))
    parts = group_connected_positions(positions, connectivity=8)

    # sort components by bottom-most row (descending)
    max_rows = [np.array(part).max(axis=0)[0] for part in parts]
    order = np.argsort(max_rows)[::-1]

    for i in order:
        part = np.array(parts[i])
        min_row, min_col = part.min(axis=0)
        max_row, max_col = part.max(axis=0)

        # check area underneath the block
        underneath = output_grid[max_row + 1 :, min_col : max_col + 1]
        pos_stopper = np.argwhere(underneath != 7)

        if pos_stopper.size > 0:
            min_row_stopper = pos_stopper[:, 0].min()
            stopping_val = underneath[min_row_stopper, 0]
        else:
            min_row_stopper = nrows - 1 - max_row
            stopping_val = stopper_val

        # clear original block
        output_grid[part[:, 0], part[:, 1]] = 7

        # drop block
        if stopping_val == stopper_val:
            shift = min_row_stopper - 1
        else:  # landed on identical value
            shift = min_row_stopper
        output_grid[part[:, 0] + shift, part[:, 1]] = input_grid[part[:, 0], part[:, 1]]

    return output_grid


def solve_28bf18c6(input_grid):
    """
    Concepts: Bounding box extraction, horizontal duplication.

    Steps:
    1. Find the minimal bounding box containing all non-zero cells.
    2. Extract this block from the input grid.
    3. Concatenate the block with itself horizontally to form the output grid.
    """

    input_grid = np.array(input_grid)
    positions = np.argwhere(input_grid != 0)
    min_row, min_col = positions.min(axis=0)
    max_row, max_col = positions.max(axis=0)

    block = input_grid[min_row : max_row + 1, min_col : max_col + 1]
    output_grid = np.hstack((block, block))

    return output_grid


def solve_278e5215(input_grid):
    """
    Concept: Subgrid extraction and column-wise filling based on a reference block.

    Transformation Steps:
    1. Extract the bounding box containing all 5s (defines the output region).
    2. Identify the minimal block of non-5, non-0 values (used for fill colors).
    3. Use the bottom row of this block as the background reference.
    4. For each column in the cropped 5-region, fill with the common value from the corresponding column in the block,
    5. Replace all positions of 0s inside the cropped 5-region with the background value.
    """

    input_grid = np.array(input_grid)

    # 1. Bounding box of 5s
    pos_with_5 = np.argwhere(input_grid == 5)
    min_row_5, min_col_5 = pos_with_5.min(axis=0)
    max_row_5, max_col_5 = pos_with_5.max(axis=0)
    output_grid = input_grid[min_row_5 : max_row_5 + 1, min_col_5 : max_col_5 + 1].copy()
    pos_0 = np.argwhere(output_grid == 0)

    # 2. Bounding box of non-5, non-0 block
    positions = np.argwhere((input_grid != 5) & (input_grid != 0))
    min_row, min_col = positions.min(axis=0)
    max_row, max_col = positions.max(axis=0)
    block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

    # 3. Background value (color) reference from bottom row
    background = np.unique(block[-1, :])[0]
    top_part = block[:-1, :]

    # 4. Fill columns in cropped 5-region
    for c in range(top_part.shape[1]):
        val = np.unique(top_part[:, c])[0]
        output_grid[:, c] = val

    # 5. Replace all positions of zeros (old background) with new background value
    output_grid[pos_0[:, 0], pos_0[:, 1]] = background

    return output_grid


def solve_94be5b80(input_grid):
    """
    Concept:
    Align and stack identical-shaped objects vertically in a grid
    based on a reference ordering.

    Transformation Logic:
    1. Identify connected components of non-zero values using connected component analysis.
    2. Find the component that contains all unique non-zero values.
       - This component is used as the "reference order" of objects.
       - Remove this reference component from the grid.
    3. Identify the other component(s) that only contain a subset of the values.
    4. Reorder these subset components to match the reference order.
    5. Stack missing objects above and/or below the subset so the final arrangement
       reproduces the full ordered stack vertically.

    Effect:
    - The grid is transformed so that all identical-shaped objects appear stacked
      on top of each other in the correct order, as dictated by the reference.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Identify unique non-zero values and connected components
    unique_vals = np.unique(output_grid[output_grid != 0])
    parts = group_connected_positions(np.argwhere(output_grid != 0), connectivity=8)

    order, other_part, other_vals = None, None, None

    # Process each connected component
    for part in parts:
        part = np.array(part)
        min_row, min_col = part.min(axis=0)
        max_row, max_col = part.max(axis=0)
        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]
        vals = np.unique(block[block != 0])

        if set(vals) == set(unique_vals):
            # Find the component that contains all unique non-zero values. This component is used as the "reference order" of objects.
            output_grid[part[:, 0], part[:, 1]] = 0
            order = block[0, :]
        else:
            # Identify the other component(s) that only contain a subset of the values.
            other_part, other_vals = part.copy(), vals.copy()

    # Reorder other components to match the reference order
    place = np.array([np.where(order == v)[0][0] if v in order else -1 for v in other_vals])
    place = place - place.min()
    other_vals_sort = np.array(other_vals)[place]

    # Stack missing objects above the subset
    val = other_vals_sort[0]
    pos = np.argwhere(output_grid == val)
    min_r, min_c = pos.min(axis=0)
    max_r, max_c = pos.max(axis=0)
    pos_norm = pos - np.array([min_r, min_c])

    plc = np.argwhere(order == val)[0][0]
    val_before = order[:plc] if plc > 0 else None

    counter = 1
    for v in val_before[::-1]:
        posit = pos_norm + np.array([min_r - counter * (max_r - min_r + 1), min_c])
        counter += 1
        output_grid[posit[:, 0], posit[:, 1]] = v

    # Stack missing objects below the subset so the final arrangement reproduces the full ordered stack vertically.
    val = other_vals_sort[-1]
    pos = np.argwhere(output_grid == val)
    min_r, min_c = pos.min(axis=0)
    max_r, max_c = pos.max(axis=0)
    pos_norm = pos - np.array([min_r, min_c])

    plc = np.argwhere(order == val)[0][0]
    val_after = order[plc + 1 :] if plc > 0 else None

    counter = 0
    for v in val_after:
        posit = pos_norm + np.array([max_r + 1 + counter * (max_r - min_r + 1), min_c])
        counter += 1
        output_grid[posit[:, 0], posit[:, 1]] = v

    return output_grid


def solve_ce8d95cc(input_grid):
    """
    Concepts: Grid compression by collapsing consecutive identical rows/columns.

    Transformation steps:
    1. Remove duplicate consecutive rows.
    2. Remove duplicate consecutive columns.
    """

    input_grid = np.array(input_grid)

    # Step 1: remove consecutive duplicate rows
    mask_rows = np.any(input_grid[1:] != input_grid[:-1], axis=1)
    keep_rows = np.r_[True, mask_rows]
    reduced = input_grid[keep_rows]

    # Step 2: remove consecutive duplicate columns
    mask_cols = np.any(reduced[:, 1:] != reduced[:, :-1], axis=0)
    keep_cols = np.r_[True, mask_cols]
    output_grid = reduced[:, keep_cols]

    # Alternative approach: using a loop to remove duplicates
    # for r in range(output_grid.shape[0] - 1):
    #     if np.array_equal(output_grid[r], output_grid[r + 1]):
    #         output_grid = np.delete(output_grid, r, axis=0)

    # for c in range(output_grid.shape[1] - 1):
    #     if np.array_equal(output_grid[:, c], output_grid[:, c + 1]):
    #         output_grid = np.delete(output_grid, c, axis=1)

    return output_grid


def solve_9f236235(input_grid):
    """
    Concepts: Grid compression by collapsing consecutive identical rows/columns,
    then removing uniform partitions and left-right flipping.

    Transformation steps:
    1. Remove duplicate consecutive rows.
    2. Remove duplicate consecutive columns.
    3. Identify the first uniform row as partition value.
    4. Remove rows/columns filled with the partition value.
    5. Flip the grid horizontally.
    """

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Step 1: remove consecutive duplicate rows
    keep_rows = np.r_[True, np.any(output_grid[1:] != output_grid[:-1], axis=1)]
    output_grid = output_grid[keep_rows]

    # Step 2: remove consecutive duplicate columns
    keep_cols = np.r_[True, np.any(output_grid[:, 1:] != output_grid[:, :-1], axis=0)]
    output_grid = output_grid[:, keep_cols]

    # Step 3: find partition value (first uniform row)
    partition_val = None
    for row in output_grid[:-1]:
        if np.all(row == row[0]):
            partition_val = row[0]
            break

    if partition_val is not None:
        # Step 4: remove rows/cols filled with partition_val
        output_grid = output_grid[~np.all(output_grid == partition_val, axis=1)]
        output_grid = output_grid[:, ~np.all(output_grid == partition_val, axis=0)]

    # Step 5: horizontal flip
    output_grid = np.fliplr(output_grid)
    return output_grid


def solve_72a961c9(input_grid):
    """
    Concepts: Build columns (towers) of different heights above certain values (2 and 8).

    Transformation steps:
    1. Identify all positions of the value 8 in the input grid.
       - Replace the two rows above each position with 1s.
       - Set the value at three rows above to 8.
    2. Identify all positions of the value 2 in the input grid.
       - Replace the three rows above each position with 1s.
       - Set the value at four rows above to 2.
    """

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Process positions with value 8
    pos_with_8 = np.argwhere(input_grid == 8)
    for r, c in pos_with_8:
        output_grid[r - 2 : r, c] = 1
        output_grid[r - 3, c] = 8

    # Process positions with value 2
    pos_with_2 = np.argwhere(input_grid == 2)
    for r, c in pos_with_2:
        output_grid[r - 3 : r, c] = 1
        output_grid[r - 4, c] = 2

    return output_grid


def solve_c3e719e8(input_grid):
    """
    Concepts: Grid expansion based on the most frequent value.

    Transformation steps:
    1. Identify the most frequent non-zero value in the input grid.
    2. Locate all positions of this value in the input grid.
    3. Expand the grid by placing the input grid at scaled positions corresponding to the identified locations.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Initialize the output grid with zeros for the expanded size
    output_grid = np.zeros((nrows * nrows, ncols * ncols), dtype=int)

    # Step 1: Find the most frequent non-zero value
    unique, counts = np.unique(input_grid, return_counts=True)
    most_frequent_val = unique[np.argmax(counts)]

    # Step 2: Get positions of the most frequent value
    pos_most_frequent = np.argwhere(input_grid == most_frequent_val)

    # Scale positions and place the input grid at each scaled position
    for r, c in pos_most_frequent * np.array([nrows, ncols]):
        output_grid[r : r + nrows, c : c + ncols] = input_grid

    return output_grid


def solve_6f473927(input_grid):
    """
    Concepts: Grid transformation (negative of the positive photograph) with flipping and stacking.

    Transformation steps:
    1. Identify positions of zero and non-zero values in the input grid.
    2. Replace zeros with 8 and non-zero values with 0 in a copy of the input grid.
    3. Flip the modified grid horizontally.
    4. Depending on the position of non-zero values:
       - If non-zero values are on the left in input, stack the flipped grid to the left of the original grid.
       - If non-zero values are on the right in input, stack the flipped grid to the right of the original grid.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Identify positions of zeros and non-zeros
    pos_with_0 = np.argwhere(input_grid == 0)
    pos_without_0 = np.argwhere(input_grid != 0)
    min_col, max_col = pos_without_0[:, 1].min(), pos_without_0[:, 1].max()

    # Create a modified version of the input grid (negative of the positive photograph)
    half_output = input_grid.copy()
    half_output[pos_with_0[:, 0], pos_with_0[:, 1]] = 8
    half_output[pos_without_0[:, 0], pos_without_0[:, 1]] = 0

    # Flip the modified grid horizontally
    half_output = np.fliplr(half_output)

    # Stack grids based on the position of non-zero values
    if min_col == 0:  # Non-zero values are on the left
        output_grid = np.hstack([half_output, input_grid])
    elif max_col == ncols - 1:  # Non-zero values are on the right
        output_grid = np.hstack([input_grid, half_output])

    return output_grid


def solve_6855a6e4(input_grid):
    """
    Concepts: Move blocks of 5s between the square brackets of 2s

    Transformation steps:
    1. Identify orientation of square brackets of '2' → vertical or horizontal.
    2. Detect connected components of '5'.
    3. Remove each '5' block, then flip and shift it between the square brackets of 2s
       - Vertical: flip up/down and move above or below to bring it between the brackets.
       - Horizontal: flip left/right and move left or right to bring it between the brackets.
    """

    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # orientation of the square brackets of 2s
    pos_with_2 = np.argwhere(input_grid == 2)
    min_row_2, min_col_2 = np.min(pos_with_2, axis=0)
    max_row_2, max_col_2 = np.max(pos_with_2, axis=0)
    direction = (
        "vertical"
        if len(np.unique(pos_with_2[:, 0])) < len(np.unique(pos_with_2[:, 1]))
        else "horizontal"
    )

    # process blocks of 5
    for part in group_connected_positions(np.argwhere(input_grid == 5)):
        part = np.array(part)
        min_r, min_c = np.min(part, axis=0)
        max_r, max_c = np.max(part, axis=0)
        block = input_grid[min_r : max_r + 1, min_c : max_c + 1]

        # clear original 5-block
        output_grid[part[:, 0], part[:, 1]] = 0

        if direction == "vertical":
            shift = (max_r - min_r) + 4
            if min_r > max_row_2:  # move upward
                output_grid[min_r - shift : max_r + 1 - shift, min_c : max_c + 1] = np.flipud(block)
            elif max_r < min_row_2:  # move downward
                output_grid[min_r + shift : max_r + 1 + shift, min_c : max_c + 1] = np.flipud(block)

        else:  # horizontal
            shift = (max_c - min_c) + 4
            if min_c > max_col_2:  # move left
                output_grid[min_r : max_r + 1, min_c - shift : max_c + 1 - shift] = np.fliplr(block)
            elif max_c < min_col_2:  # move right
                output_grid[min_r : max_r + 1, min_c + shift : max_c + 1 + shift] = np.fliplr(block)

    return output_grid


def solve_7837ac64(input_grid):
    """
    Concepts: Block partitioning and corner-based reduction.

    Transformation steps:
    1. Identify block size from the first row's nonzero spacing.
    2. Find the most frequent nonzero value (grid partition marker).
    3. Extract the minimal bounding box containing all other non-frequent values.
    4. Partition the bounding box into square blocks.
    5. For each block:
       - If all 4 corners match (and ≠ most frequent), keep that value.
       - Else assign 0.
    6. Return the reduced grid.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: block size from first row spacing
    first_row = input_grid[0, :]
    pos_n0 = np.where(first_row != 0)[0]
    size = pos_n0[1] - pos_n0[0]

    # Step 2: find most frequent nonzero value (grid partition marker)
    non_zero_val, counts = np.unique(input_grid[input_grid != 0], return_counts=True)
    most_frequent = non_zero_val[np.argmax(counts)]

    # Step 3: bounding box of non-frequent values
    pos_non_frequent = np.argwhere((input_grid != 0) & (input_grid != most_frequent))
    min_row, min_col = np.min(pos_non_frequent, axis=0)
    max_row, max_col = np.max(pos_non_frequent, axis=0)
    block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

    # Step 4–5: partition + reduce
    output_grid = []
    for r in range(0, block.shape[0] - 1, size):
        row_vals = []
        for c in range(0, block.shape[1] - 1, size):
            square = block[r : r + size + 1, c : c + size + 1]
            corners = np.unique([square[0, 0], square[0, -1], square[-1, 0], square[-1, -1]])
            if len(corners) == 1 and corners[0] != most_frequent:
                row_vals.append(corners[0])
            else:
                row_vals.append(0)
        output_grid.append(row_vals)

    return np.array(output_grid)


def solve_13f06aa5(input_grid):
    """
    Concepts: Source firing objects to the grid wall, Directional propagation, unique value extension,

    Transformation steps:
    1. Identify unique values (appearing once) in the grid.
    2. For each, extend its value in the direction of adjacent background cells (up, down, left, right).
    3. Fill edge and corner cells according to overlap rules.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    unique, counts = np.unique(input_grid, return_counts=True)
    background = unique[np.argmax(counts)]
    selected_vals = unique[counts == 1]  # objects

    for val in selected_vals:
        pos = np.argwhere(input_grid == val)[0]
        r, c = pos

        # Shoot up
        if r > 0 and input_grid[r - 1, c] == background:
            for rr in range(r - 2, -1, -2):
                output_grid[rr, c] = val
            output_grid[0, 1:-1] = val
            for r_, c_ in [(0, 0), (0, ncols - 1)]:  # filling the corners
                output_grid[r_, c_] = val if output_grid[r_, c_] == background else 0

        # Shoot down
        elif r < nrows - 1 and input_grid[r + 1, c] == background:
            for rr in range(r + 2, nrows, 2):
                output_grid[rr, c] = val
            output_grid[-1, 1:-1] = val
            for r_, c_ in [(nrows - 1, 0), (nrows - 1, ncols - 1)]:
                output_grid[r_, c_] = val if output_grid[r_, c_] == background else 0

        # Shoot left
        elif c > 0 and input_grid[r, c - 1] == background:
            for cc in range(c - 2, -1, -2):
                output_grid[r, cc] = val
            output_grid[1:-1, 0] = val
            for r_, c_ in [(0, 0), (nrows - 1, 0)]:
                output_grid[r_, c_] = val if output_grid[r_, c_] == background else 0

        # Shoot right
        elif c < ncols - 1 and input_grid[r, c + 1] == background:
            for cc in range(c + 2, ncols, 2):
                output_grid[r, cc] = val
            output_grid[1:-1, -1] = val
            for r_, c_ in [(0, ncols - 1), (nrows - 1, ncols - 1)]:
                output_grid[r_, c_] = val if output_grid[r_, c_] == background else 0

    return output_grid


def solve_a68b268e(input_grid):
    """
    Concepts:
    - Grid partitioning in four blocks (quadrants), zero filling block by block


    Steps:
    1. Find the row and column fully filled with 1s, they partition the grid.
    2. Partition the grid into four blocks.
    3. Define a helper to fill zeros in a block.
    4. Apply the filling to each block in the order: top-left, top-right, bottom-left, bottom-right.
    5. Return the modified grid.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Find the first row and column fully filled with 1s, they partition the grid
    row_with_1 = next((r for r in range(nrows) if np.all(input_grid[r, :] == 1)), None)
    col_with_1 = next((c for c in range(ncols) if np.all(input_grid[:, c] == 1)), None)

    # Partition the grid into four blocks
    top_left = input_grid[:row_with_1, :col_with_1]
    top_right = input_grid[:row_with_1, col_with_1 + 1 :]
    bottom_left = input_grid[row_with_1 + 1 :, :col_with_1]
    bottom_right = input_grid[row_with_1 + 1 :, col_with_1 + 1 :]

    def fill_zeros(grid, block):
        """Fill zeros in grid with corresponding values from block."""
        zero_positions = np.argwhere(grid == 0)
        for pos in zero_positions:
            r, c = tuple(pos)
            grid[r, c] = block[r, c]
        return grid

    # Apply filling to each block in the order: top-left, top-right, bottom-left, bottom-right
    output_grid = top_left
    output_grid = fill_zeros(output_grid, top_right)
    output_grid = fill_zeros(output_grid, bottom_left)
    output_grid = fill_zeros(output_grid, bottom_right)

    return output_grid


def solve_5c0a986e(input_grid):
    """
    Concepts: making tail of a kite, extending values diagonally

    Steps:
    1. Find unique non-zero values.
    2. For each value, locate its bounding box: min/max positions.
    3. Extend the value diagonally up-left for value 1 and down-right for value 2.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    non_zero_vals = np.unique(input_grid[input_grid != 0])
    for val in non_zero_vals:
        positions = np.argwhere(input_grid == val)
        min_row, min_col = positions.min(axis=0)
        max_row, max_col = positions.max(axis=0)

        if val == 1:
            # If value is 1, extend diagonally up-left
            for i in range(1, max(nrows, ncols)):
                r, c = min_row - i, min_col - i
                if r >= 0 and c >= 0:
                    output_grid[r, c] = val
                else:
                    break
        elif val == 2:
            # If value is 2, extend diagonally down-right
            for i in range(1, max(nrows, ncols)):
                r, c = max_row + i, max_col + i
                if r < nrows and c < ncols:
                    output_grid[r, c] = val
                else:
                    break

    return output_grid


def solve_890034e9(input_grid):
    """
    Concepts:
    - Given a frame and its interior, if the same interior is found elsewhere in the grid, place the frame around it.

    Steps:
    1. Identify the frame value and its position.
    2. Extract the interior of the frame.
    3. Search for matching interiors in the grid.
    4. Place the frame around any matching interior found.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Identify frame value (least frequent value)
    unique, counts = np.unique(input_grid, return_counts=True)
    frame_value = unique[np.argmin(counts)]

    # Get frame position
    frame_positions = np.argwhere(input_grid == frame_value)
    min_row, min_col = frame_positions.min(axis=0)
    max_row, max_col = frame_positions.max(axis=0)

    # Extract frame interior
    frame_interior = input_grid[min_row + 1 : max_row, min_col + 1 : max_col]
    H, W = frame_interior.shape

    # Search for matching interiors and place frame
    for r in range(nrows - H):
        for c in range(ncols - W):
            block = output_grid[r : r + H, c : c + W]
            if np.array_equal(block, frame_interior):
                # Place frame around the block
                output_grid[r - 1, c - 1 : c + W + 1] = frame_value
                output_grid[r + H, c - 1 : c + W + 1] = frame_value
                output_grid[r - 1 : r + H + 1, c - 1] = frame_value
                output_grid[r - 1 : r + H + 1, c + W] = frame_value

    return output_grid


def solve_18419cfa(input_grid):
    """
    Concepts:
    - Detect connected components of value 8 that form mirror frames.
    - For each component, determine mirror orientation by 8's distribution.
    - Create the mirror image by flipping and combining with the original.

    Steps:
    1. Convert input to numpy array.
    2. Find all positions containing value 8.
    3. Group connected positions of 8s (mirror frames).
    4. For each group:
        - Determine orientation (horizontal/vertical) by 8's distribution.
        - Apply the appropriate flip (horizontal/vertical).
        - Combine original and flipped block using maximum values to fill the empty places of 0s.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find and group connected 8s (mirror frames)
    positions_with_8 = np.argwhere(input_grid == 8)
    connected_8_groups = group_connected_positions(positions_with_8)

    # Process each mirror frame
    for group in connected_8_groups:
        group = np.array(group)
        min_row, min_col = np.min(group, axis=0)
        max_row, max_col = np.max(group, axis=0)

        # Extract the block containing the mirror frame
        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

        # Determine mirror orientation by 8's distribution
        eights_in_row = np.sum(input_grid[min_row, :] == 8)
        eights_in_col = np.sum(input_grid[:, min_col] == 8)

        if eights_in_row > eights_in_col:
            # Horizontal mirror: flip left-right
            flipped_block = np.fliplr(block)
        else:
            # Vertical mirror: flip up-down
            flipped_block = np.flipud(block)

        # Combine original and flipped block using maximum values
        output_grid[min_row : max_row + 1, min_col : max_col + 1] = np.maximum(block, flipped_block)

    return output_grid


def solve_45bbe264(input_grid):
    """
    Concepts:
    - Expand non-zero values along their rows and columns.
    - Place value 2 at the intersections of expanded rows and columns.

    Steps:
    1. Find all non-zero positions.
    2. For each non-zero position, extend its value along its row and column.
    3. Place value 2 at intersections between the expanded rows and columns.
    """

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find positions of non-zero values
    positions_non_zero = np.argwhere(input_grid != 0)

    # Expand each non-zero value along its row and column
    for pos in positions_non_zero:
        r, c = tuple(pos)
        value = input_grid[r, c]
        output_grid[r, :] = value  # Fill row
        output_grid[:, c] = value  # Fill column

    # Place value 2 at intersections
    for i in range(len(positions_non_zero)):
        for j in range(i + 1, len(positions_non_zero)):
            r1, c1 = tuple(positions_non_zero[i])
            r2, c2 = tuple(positions_non_zero[j])
            # At the intersection points, place value 2
            output_grid[r1, c2] = 2
            output_grid[r2, c1] = 2

    return output_grid


def solve_7c8af763(input_grid):
    """
    Concepts: leakage from the neighboring values (colors) into the empty compartments
    - Find connected components of zeros in the grid, these are empty compartments.
    - For each component, examine neighboring values.
    - Fill the zero regions with the most common neighboring value out of 1 and 2.

    Steps:
    1. Find all positions containing zero.
    2. Group connected zero positions.
    3. For each group:
        - Determine the boundary of the zero region.
        - Collect all neighboring values around the boundary.
        - Count occurrences of values 1 and 2 among neighbors.
        - Fill the zero region with the more frequent value out of 1 and 2.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find and group connected zeros
    zero_positions = np.argwhere(input_grid == 0)
    connected_zero_groups = group_connected_positions(zero_positions)

    # Process each connected zero component (empty compartment)
    for group in connected_zero_groups:
        group = np.array(group)
        min_row, min_col = group.min(axis=0)
        max_row, max_col = group.max(axis=0)

        # Collect all neighboring values around the boundary
        neighbors = []

        # Top neighbors
        if min_row > 0:
            for c in range(max(0, min_col - 1), min(ncols, max_col + 2)):
                neighbors.append(input_grid[min_row - 1, c])

        # Bottom neighbors
        if max_row < nrows - 1:
            for c in range(max(0, min_col - 1), min(ncols, max_col + 2)):
                neighbors.append(input_grid[max_row + 1, c])

        # Left neighbors
        if min_col > 0:
            for r in range(max(0, min_row - 1), min(nrows, max_row + 2)):
                neighbors.append(input_grid[r, min_col - 1])

        # Right neighbors
        if max_col < ncols - 1:
            for r in range(max(0, min_row - 1), min(nrows, max_row + 2)):
                neighbors.append(input_grid[r, max_col + 1])

        # Count occurrences of values 1 and 2
        neighbors = np.array(neighbors)
        count_1s = np.sum(neighbors == 1)
        count_2s = np.sum(neighbors == 2)

        # Fill with the more frequent value out of 1 and 2 in the empty compartment
        if count_1s > count_2s:
            output_grid[min_row : max_row + 1, min_col : max_col + 1] = 1
        elif count_2s > count_1s:
            output_grid[min_row : max_row + 1, min_col : max_col + 1] = 2

    return output_grid


def solve_14b8e18c(input_grid):
    """
    Concepts:
    - Identify square compartments formed by non-background values.
    - For each square compartment, mark its corners with value 2.

    Steps:
    1. Find the non-background value (value different from 7).
    2. Group connected positions containing this value.
    3. For each group:
        - Determine if it forms a square compartment.
        - If it's a square with consistent border values, mark its corners with 2.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find the non-background value (value that is not 7)
    non_background_val = np.unique(input_grid[input_grid != 7])[0]

    # Find and group connected positions of non-background values
    positions_non_background = np.argwhere(input_grid == non_background_val)
    connected_groups = group_connected_positions(positions_non_background)

    # Process each connected group (potential compartment)
    for group in connected_groups:
        group = np.array(group)
        min_row, min_col = group.min(axis=0)
        max_row, max_col = group.max(axis=0)
        height, width = max_row - min_row + 1, max_col - min_col + 1

        # Extract frame values (border of the compartment)
        frame = []
        frame.extend(input_grid[min_row, min_col : max_col + 1])  # Top row
        frame.extend(input_grid[max_row, min_col : max_col + 1])  # Bottom row
        frame.extend(input_grid[min_row : max_row + 1, min_col])  # Left column
        frame.extend(input_grid[min_row : max_row + 1, max_col])  # Right column

        # Define corner positions around the compartment
        corner_positions = [
            (min_row, min_col - 1),
            (min_row - 1, min_col),  # Top-left corners
            (min_row, max_col + 1),
            (min_row - 1, max_col),  # Top-right corners
            (max_row + 1, min_col),
            (max_row, min_col - 1),  # Bottom-left corners
            (max_row + 1, max_col),
            (max_row, max_col + 1),  # Bottom-right corners
        ]

        # Check if it's a square compartment with consistent border
        if height == width and all(val == non_background_val for val in frame):
            # Mark all valid corner positions with value 2
            for r, c in corner_positions:
                if 0 <= r < nrows and 0 <= c < ncols:
                    output_grid[r, c] = 2

    return output_grid


def solve_f8be4b64(input_grid):
    """
    Concepts: Gift wrapping with ribbons — coloring rows and columns like tying ribbons on gift boxes.

    Transformation steps:
    1. Identify connected regions of value 3 (ribbon flowers).
    2. For each region, compute its center point (flower middle).
    3. From each center, extend its value horizontally, then vertically.
    4. Stop extension when another flower (3) is encountered or at grid boundary.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find all positions with value 3 (that make ribbon flowers)
    pos_with_3 = np.argwhere(input_grid == 3)

    # Group positions into connected components (ribbon flowers)
    parts_with_3 = group_connected_positions(pos_with_3)

    # Find middle points for each connected component
    middle_rows = []
    middle_cols = []
    middle_vals = []

    for part in parts_with_3:
        part = np.array(part)
        min_row, max_row = part[:, 0].min(), part[:, 0].max()
        min_col, max_col = part[:, 1].min(), part[:, 1].max()

        # Calculate center coordinates (flower middle color)
        middle_row = (min_row + max_row) // 2
        middle_col = (min_col + max_col) // 2

        middle_rows.append(middle_row)
        middle_cols.append(middle_col)

        # Get value at center position
        middle_val = input_grid[middle_row, middle_col]
        middle_vals.append(middle_val)

    # Process components by row order
    order = np.argsort(middle_rows)
    for i in order:
        middle_row = middle_rows[i]
        middle_col = middle_cols[i]
        middle_val = middle_vals[i]

        # Extend horizontally left until encountering another ribbon flower or grid boundary
        for c in range(middle_col - 2, -1, -1):
            if output_grid[middle_row, c] != 3:
                output_grid[middle_row, c] = middle_val
            else:
                break

        # Extend horizontally right until encountering another ribbon flower or grid boundary
        for c in range(middle_col + 2, ncols):
            if output_grid[middle_row, c] != 3:
                output_grid[middle_row, c] = middle_val
            else:
                break

    # Then Process components by column order
    order = np.argsort(middle_cols)
    for i in order:
        middle_row = middle_rows[i]
        middle_col = middle_cols[i]
        middle_val = middle_vals[i]

        # Extend vertically up until encountering another ribbon flower or grid boundary
        for r in range(middle_row - 2, -1, -1):
            if output_grid[r, middle_col] != 3:
                output_grid[r, middle_col] = middle_val
            else:
                break

        # Extend vertically down until encountering another ribbon flower or grid boundary
        for r in range(middle_row + 2, nrows):
            if output_grid[r, middle_col] != 3:
                output_grid[r, middle_col] = middle_val
            else:
                break

    return output_grid


def solve_bae5c565(input_grid):
    """
    Concepts: The Galton board — filling columns based on a reference row and a pivot point.

    Transformation steps:
    1. Identify a pivot column using the value 8 in the bottom row
    2. Count the number of 8s in the pivot column to determine fill depth
    3. Use the top row as a reference for values (colors) to fill into columns
    4. Fill values from the bottom up based on distance from pivot
    5. Replace the top reference row with background value 5
    """

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find the column with value 8 in the bottom row as pivot point
    pos_with_8 = np.argwhere(input_grid[-1] == 8)[0][0]
    col_with_8 = input_grid[:, pos_with_8]
    num_8s = np.sum(col_with_8 == 8)

    # Use the top row as the reference for column values
    top_row = input_grid[0]

    # Fill columns to the left of pivot
    for c, val in enumerate(top_row[:pos_with_8]):
        # Calculate fill height based on column distance from pivot
        fill_height = c + (num_8s - pos_with_8)
        # Fill from bottom up
        output_grid[-fill_height:, c] = val

    # Fill columns to the right of pivot
    for c, val in enumerate(top_row[pos_with_8 + 1 :]):
        # Calculate fill height based on column distance from pivot
        fill_height = num_8s - 1 - c
        # Fill from bottom up
        output_grid[-fill_height:, c + pos_with_8 + 1] = val

    # Replace the reference row with background value 5
    output_grid[0] = 5

    return output_grid


def solve_e7dd8335(input_grid):
    """
    Concepts: Shape identification and color transformation for vertical mirror symmetry.

    Transformation steps:
    1. Identify all positions containing value 1 in the grid
    2. Determine the bounding box of the shape formed by these positions
    3. Calculate the vertical midpoint of the shape
    4. Replace all values below the midpoint with color 2, creating a mirror image (two-tone) effect
    """

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find all positions with value 1
    pos_with_1 = np.argwhere(input_grid == 1)

    # Skip processing if no values of 1 are found
    if len(pos_with_1) == 0:
        return output_grid

    # Determine bounding box of the shape
    min_row, min_col = pos_with_1.min(axis=0)
    max_row, max_col = pos_with_1.max(axis=0)

    # Calculate dimensions of the bounding box
    height = max_row - min_row + 1
    width = max_col - min_col + 1

    # Calculate the vertical midpoint
    half_height = height // 2
    midpoint_row = min_row + half_height - 1

    # Replace values in the lower half of the shape with 2
    # This creates a mirror image (two-tone) effect with vertical symmetry
    for p in pos_with_1:
        r, c = p
        if r > midpoint_row:
            output_grid[r, c] = 2

    return output_grid


def solve_6cdd2623(input_grid):
    """
    Concepts: Connection detection and line drawing between least frequent values.

    Transformation steps:
    1. Find the least frequent value in the grid
    2. Connect pairs of points with the same least frequent value:
       - Horizontally (first preference) if two points are in the same row
       - Vertically (second preference) if two points are in the same column
    3. Each point can only be connected once (paired once)
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros_like(input_grid)  # initialize output grid to background color

    # Find the least frequent value
    unique, counts = np.unique(input_grid, return_counts=True)
    least_frequent_val = unique[np.argmin(counts)]

    # Get positions of all cells with the least frequent value
    pos_lfv = np.argwhere(input_grid == least_frequent_val)

    # Track which positions have been paired already
    paired_positions = []

    # First Try to find horizontal pairs (same row, different columns)
    for p1 in pos_lfv:
        if tuple(p1) in paired_positions:
            continue

        for p2 in pos_lfv:
            if tuple(p2) in paired_positions:
                continue

            r1, c1 = p1
            r2, c2 = p2

            # Check if same row but different column
            if r1 == r2 and c1 != c2:
                # Connect horizontally
                output_grid[r1, min(c1, c2) : max(c1, c2) + 1] = least_frequent_val
                paired_positions.append(tuple(p1))
                paired_positions.append(tuple(p2))
                break

    # Second Try to find vertical pairs (same column, different rows)
    for p1 in pos_lfv:
        if tuple(p1) in paired_positions:
            continue

        for p2 in pos_lfv:
            if tuple(p2) in paired_positions:
                continue

            r1, c1 = p1
            r2, c2 = p2

            # Check if same column but different row
            if c1 == c2 and r1 != r2:
                # Connect vertically
                output_grid[min(r1, r2) : max(r1, r2) + 1, c1] = least_frequent_val
                paired_positions.append(tuple(p1))
                paired_positions.append(tuple(p2))
                break

    return output_grid


def solve_36d67576(input_grid):
    """
    Concepts: Pattern matching and completion with the found template.

    Transformation steps:
    1. Identify non-zero elements in the input grid
    2. Group them into connected components
    3. Find the largest component (complete object)
    4. Use the complete object as a template
    5. Search for matching patterns in different orientations of the grid
    6. Replace matching areas with the template
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    def detect_replace_structure(big_grid, small_grid):
        """
        Detect whether small_grid structure exists inside big_grid.
        If yes, the big_grid will be modified to include small_grid.
        """
        big = np.array(big_grid)
        small = np.array(small_grid)

        br, bc = big.shape
        sr, sc = small.shape

        # Slide small grid over big grid
        for i in range(br - sr + 1):
            for j in range(bc - sc + 1):
                window = big[i : i + sr, j : j + sc]

                # Check match: values 2 and 4 in small grid must match exactly in big grid
                mask = (small == 2) | (small == 4)
                if mask.any() and np.array_equal(window[mask], small[mask]):
                    # Found a match, replace the window with the small grid
                    big[i : i + sr, j : j + sc] = small

        return big

    # Identify non-zero positions
    pos_non_zero = np.argwhere(input_grid != 0)

    # Group non-zero positions into connected components
    parts_non_zero = group_connected_positions(pos_non_zero)

    # Find the largest connected component (the template)
    complete_object = None
    incomplete_objects = []
    max_cells = 0

    for part in parts_non_zero:
        num_cells = len(part)
        if num_cells > max_cells:
            max_cells = num_cells
            complete_object = part
        else:
            incomplete_objects.append(part)

    # Extract the bounding box of the complete object (template)
    complete_object = np.array(complete_object)
    min_row, min_col = complete_object.min(axis=0)
    max_row, max_col = complete_object.max(axis=0)
    complete_block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

    # Try to find and replace matching patterns in different orientations

    # Check all 4 rotations
    for k in range(4):
        output_grid = np.rot90(output_grid, k=k)
        output_grid = detect_replace_structure(output_grid, complete_block)
        output_grid = np.rot90(output_grid, k=-k)  # Rotate back

    # Check vertical flip
    output_grid = np.flipud(output_grid)
    output_grid = detect_replace_structure(output_grid, complete_block)
    output_grid = np.flipud(output_grid)  # Flip back

    # Check horizontal flip
    output_grid = np.fliplr(output_grid)
    output_grid = detect_replace_structure(output_grid, complete_block)
    output_grid = np.fliplr(output_grid)  # Flip back

    return output_grid


def solve_103eff5b(input_grid):
    """
    Concepts:
    - grid rotation, scaling, and pattern matching,
    - color (fill value) in placeholder pattern as per given reference

    Steps:
    1. Extract reference pattern (non-zero, non-8 values).
    2. Extract placeholder pattern (pattern of 8s).
    3. Reduce placeholder by removing duplicate rows and columns.
    4. Find correct orientation by rotating reference pattern.
    5. Replace placeholders with scaled reference pattern.
    """

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Extract reference pattern (non-zero, non-8 values)
    reference_positions = np.argwhere((input_grid != 0) & (input_grid != 8))
    min_row, min_col = np.min(reference_positions, axis=0)
    max_row, max_col = np.max(reference_positions, axis=0)
    reference_pattern = input_grid[min_row : max_row + 1, min_col : max_col + 1]
    reference_mask = reference_pattern != 0

    # Extract placeholder pattern (pattern of 8s)
    placeholder_positions = np.argwhere(input_grid == 8)
    min_row_ph, min_col_ph = np.min(placeholder_positions, axis=0)
    max_row_ph, max_col_ph = np.max(placeholder_positions, axis=0)
    placeholder_pattern = input_grid[min_row_ph : max_row_ph + 1, min_col_ph : max_col_ph + 1]

    # Remove consecutive duplicate rows
    row_differences = np.any(placeholder_pattern[1:] != placeholder_pattern[:-1], axis=1)
    unique_rows = np.r_[True, row_differences]
    reduced_pattern = placeholder_pattern[unique_rows]

    # Remove consecutive duplicate columns
    col_differences = np.any(reduced_pattern[:, 1:] != reduced_pattern[:, :-1], axis=0)
    unique_cols = np.r_[True, col_differences]
    reduced_pattern = reduced_pattern[:, unique_cols]

    # Create mask of placeholder positions
    placeholder_mask = reduced_pattern == 8

    # Calculate scaling factor
    scaling_factor = (max_row_ph - min_row_ph + 1) // (max_row - min_row + 1)

    # Find correct orientation and replace placeholders
    for rotation in range(4):
        rotated_reference_mask = np.rot90(reference_mask, k=rotation)
        if np.array_equal(rotated_reference_mask, placeholder_mask):
            rotated_reference = np.rot90(reference_pattern, k=rotation)

            # Replace each cell in the placeholder with scaled reference cells
            ref_height, ref_width = rotated_reference.shape
            for r in range(ref_height):
                for c in range(ref_width):
                    r_start = min_row_ph + r * scaling_factor
                    r_end = min_row_ph + (r + 1) * scaling_factor
                    c_start = min_col_ph + c * scaling_factor
                    c_end = min_col_ph + (c + 1) * scaling_factor
                    output_grid[r_start:r_end, c_start:c_end] = rotated_reference[r, c]
            break

    return output_grid


def solve_87ab05b8(input_grid):
    """
    Concepts: Grid cleaning, fill (colored) the closest corner with identified value (color)

    Steps:
    1. Create a blank output grid filled with 6 (Grid cleaning)
    2. Find the position of value 2.
    3. Calculate distances from this position to all four corners.
    4. Identify the closest corner.
    5. Fill a 2x2 block in that corner with value 2.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Initialize output grid with all 6s
    output_grid = np.full((nrows, ncols), 6)

    # Find the position of value 2
    position_of_2 = np.argwhere(input_grid == 2)[0]

    # Define the four corners of the grid
    corners = [
        (0, 0),  # Top-left
        (0, ncols - 1),  # Top-right
        (nrows - 1, 0),  # Bottom-left
        (nrows - 1, ncols - 1),  # Bottom-right
    ]

    # Calculate Euclidean distances from value 2 to each corner
    distances_to_corners = []
    for corner in corners:
        distance = np.linalg.norm(np.array(corner) - position_of_2)
        distances_to_corners.append(distance)

    # Find the closest corner
    closest_corner_index = np.argmin(distances_to_corners)

    # Fill a 2x2 block in the closest corner with 2s
    if closest_corner_index == 0:  # Top-left corner
        output_grid[:2, :2] = 2
    elif closest_corner_index == 1:  # Top-right corner
        output_grid[:2, -2:] = 2
    elif closest_corner_index == 2:  # Bottom-left corner
        output_grid[-2:, :2] = 2
    elif closest_corner_index == 3:  # Bottom-right corner
        output_grid[-2:, -2:] = 2

    return output_grid


def solve_a57f2f04(input_grid):
    """
    Concepts:
    - Identify blocks in the grid (areas not containing value 8).
    - Extract the smallest meaningful sub-pattern within each block.
    - Repeat this sub-pattern to fill the entire block.

    Steps:
    2. Find and group connected non-8 positions in the grid
    3. For each group:
        - Extract the block defined by the group.
        - Find the smallest sub-pattern (non-zero elements) within the block.
        - Tile the sub-pattern to fill the entire block.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find and group non-8 positions
    non_8_positions = np.argwhere(input_grid != 8)
    connected_non_8_groups = group_connected_positions(non_8_positions)

    # Process each connected group
    for group in connected_non_8_groups:
        group = np.array(group)
        min_row, min_col = group.min(axis=0)
        max_row, max_col = group.max(axis=0)

        # Extract the block defined by this group
        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

        # Find the smallest sub-pattern (non-zero elements)
        non_zero_positions = np.argwhere(block != 0)
        if len(non_zero_positions) == 0:
            continue  # Skip empty blocks

        min_sub_row, min_sub_col = non_zero_positions.min(axis=0)
        max_sub_row, max_sub_col = non_zero_positions.max(axis=0)
        sub_pattern = block[min_sub_row : max_sub_row + 1, min_sub_col : max_sub_col + 1]

        # Calculate number of repetitions needed
        pattern_height, pattern_width = sub_pattern.shape
        vertical_repeats = block.shape[0] // pattern_height
        horizontal_repeats = block.shape[1] // pattern_width

        # Tile the sub-pattern to fill the block
        for r in range(vertical_repeats):
            for c in range(horizontal_repeats):
                row_start = r * pattern_height
                row_end = (r + 1) * pattern_height
                col_start = c * pattern_width
                col_end = (c + 1) * pattern_width
                block[row_start:row_end, col_start:col_end] = sub_pattern

        # Update the output grid with the filled block
        output_grid[min_row : max_row + 1, min_col : max_col + 1] = block

    return output_grid


def solve_52fd389e(input_grid):
    """
    Concepts: Frame (pad) every non-zero block with value (color) and thickness illustrated in the block.

    Steps:
    1. Find and group connected non-zero positions.
    2. For each group:
        - Extract the block defined by the group.
        - Find non-4 elements and their value.
        - Add a frame around the block with thickness equal to the count of non-4 elements.
        - Place the framed block back into the output grid.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find and group non-zero positions
    non_zero_positions = np.argwhere(input_grid != 0)
    connected_groups = group_connected_positions(non_zero_positions)

    # Process each connected group
    for group in connected_groups:
        group = np.array(group)
        min_row, min_col = group.min(axis=0)
        max_row, max_col = group.max(axis=0)

        # Extract the block defined by this group
        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

        # Find non-4 elements and their value
        non_4_positions = np.argwhere(block != 4)

        # Skip if there are no non-4 elements or multiple values
        if len(non_4_positions) == 0:
            continue

        # Get the unique non-4 value (assuming all non-4 elements have the same value)
        frame_value = np.unique(block[non_4_positions[:, 0], non_4_positions[:, 1]])[0]
        frame_thickness = len(non_4_positions)

        # Add a frame around the block with thickness equal to count of non-4 elements
        if frame_thickness > 0:
            framed_block = np.pad(
                block, pad_width=frame_thickness, mode="constant", constant_values=frame_value
            )

            # Place the framed block back into the output grid
            r_start = max(0, min_row - frame_thickness)
            r_end = min(nrows, max_row + 1 + frame_thickness)
            c_start = max(0, min_col - frame_thickness)
            c_end = min(ncols, max_col + 1 + frame_thickness)

            # Adjust framed block if it would go out of bounds
            fr_start = max(0, frame_thickness - min_row)
            fr_end = framed_block.shape[0] - max(0, (max_row + 1 + frame_thickness) - nrows)
            fc_start = max(0, frame_thickness - min_col)
            fc_end = framed_block.shape[1] - max(0, (max_col + 1 + frame_thickness) - ncols)

            output_grid[r_start:r_end, c_start:c_end] = framed_block[
                fr_start:fr_end, fc_start:fc_end
            ]

    return output_grid


def solve_9841fdad(input_grid):
    """
    Concepts:
    - Identify columns with unique values that act as separators.
    - Extract a reference block and a placeholder block separated by these columns.
    - Find patterns in the reference block and apply corresponding transformations
      to the placeholder block based on their positions and dimensions.

    Steps:
    1. Find columns with unique values (separators).
    2. Extract reference block and placeholder block.
    3. Find connected components of non-1 values in the reference block.
    4. For each component:
        - If it's a square:
            - If near left boundary, copy it to left side of placeholder block.
            - If near right boundary, copy it to right side of placeholder block.
        - If it's wider than tall, extend it across the placeholder block with same height.
    5. Update the output grid with the modified placeholder block.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find columns with unique values (separators)
    separator_columns = []
    for col in range(ncols):
        unique_values = set(input_grid[:, col])
        if len(unique_values) == 1:
            separator_columns.append(col)

    # Extract reference and placeholder blocks
    reference_block = input_grid[1 : nrows - 1, 1 : separator_columns[1]]
    placeholder_block = input_grid[1 : nrows - 1, separator_columns[1] + 1 : ncols - 1]

    # Find connected components of non-1 values in reference block
    non_1_positions = np.argwhere(reference_block != 1)
    non_1_components = group_connected_positions(non_1_positions)

    # Process each component
    for component in non_1_components:
        component = np.array(component)
        min_row, min_col = component.min(axis=0)
        max_row, max_col = component.max(axis=0)

        # Get the value of this component (assuming uniform value)
        component_value = np.unique(reference_block[min_row : max_row + 1, min_col : max_col + 1])[
            0
        ]

        # Calculate height and width
        height = max_row - min_row + 1
        width = max_col - min_col + 1

        # Apply transformations based on component shape and position
        if height == width:  # Square component
            if min_col == 1:  # Near left boundary
                # Copy square to left side of placeholder block for each row in component
                for row in np.unique(component[:, 0]):
                    placeholder_block[row, 1 : height + 1] = component_value

            elif max_col == reference_block.shape[1] - 2:  # Near right boundary
                # Copy square to right side of placeholder block for each row in component
                for row in np.unique(component[:, 0]):
                    placeholder_block[row, -height - 1 : -1] = component_value

        elif height < width:  # Rectangle wider than tall
            # Extend horizontally across placeholder block for each row in component
            placeholder_width = placeholder_block.shape[1] - 2
            for row in np.unique(component[:, 0]):
                placeholder_block[row, 1 : placeholder_width + 1] = component_value

    # Update output grid with modified placeholder block
    output_grid[1 : nrows - 1, separator_columns[1] + 1 : ncols - 1] = placeholder_block

    return output_grid


def solve_79cce52d(input_grid):
    """
    Concepts:
    - Use value 2 at the top and left edges as position markers.
    - Divide the grid into four quadrants based on these markers.
    - Rearrange the quadrants by rotating them to create the output_grid

    Steps:
    1. Remove the first row and column (border).
    2. Find the positions of markers (value 2) to determine quadrant sizes.
    3. Split the grid into four quadrants.
    4. Rearrange the quadrants in a new configuration.
    5. Return the rearranged grid.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Remove border (first row and column)
    inner_grid = input_grid[1:, 1:]

    # Find marker positions (value 2) to determine quadrant boundaries
    # Calculate from the end of grid to get quadrant heights/widths
    quadrant_height = nrows - np.argwhere(input_grid[:, 0] == 2)[0][0]
    quadrant_width = ncols - np.argwhere(input_grid[0, :] == 2)[0][0]

    # Split the grid into four quadrants
    top_left = inner_grid[:quadrant_height, :quadrant_width]
    top_right = inner_grid[:quadrant_height, quadrant_width:]
    bottom_left = inner_grid[quadrant_height:, :quadrant_width]
    bottom_right = inner_grid[quadrant_height:, quadrant_width:]

    # Rearrange the quadrants (rotate them)
    # Create new grid with: [bottom_right, bottom_left] on top and [top_right, top_left] on bottom
    output_grid = np.vstack(
        (np.hstack((bottom_right, bottom_left)), np.hstack((top_right, top_left)))
    )

    return output_grid


def solve_d8c310e9(input_grid):
    """
    Concept: Identifies the largest repeating pattern block in the input grid and uses it to fill the output grid.

    Steps:
    1. Search for the largest repeating block with minimal shift.
    2. Tile the identified pattern across the output grid from left to right.
    """

    # Convert input to numpy array and initialize output grid
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    repeating_pattern = None

    # Search for the largest repeating block with minimal shift
    for shift in range(ncols):  # Try different shifts to handle partial overlaps
        for width in range(1, ncols):  # Try different block widths
            # Extract the current block and the next block with the given shift
            block = input_grid[:, :width]
            next_block = input_grid[:, width + shift : width + shift + width]

            # Check if the blocks are equal
            if np.array_equal(block, next_block):
                # Update the repeating pattern to include the shift
                repeating_pattern = input_grid[:, : width + shift]

        # Exit the loop if a repeating pattern is found
        if repeating_pattern is not None:
            break

    # Tile the repeating pattern across the output grid
    pattern_height, pattern_width = repeating_pattern.shape
    for col_start in range(0, ncols, pattern_width):
        for offset in range(pattern_width):
            if col_start + offset < ncols:
                output_grid[:, col_start + offset] = repeating_pattern[:, offset]

    return output_grid


def solve_1f876c06(input_grid):
    """
    Concept: draw a line between two points in a grid.

    Steps:
    1. Identify all unique non-zero values in the grid.
    2. For each value, find its two positions in the grid.
    3. Draw a straight line between these positions using Bresenham-like algorithm.
    4. Return the grid with all connected lines.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Find all unique non-zero values
    non_zero_values = np.unique(input_grid[input_grid != 0])

    # Process each unique non-zero value
    for value in non_zero_values:
        # Find positions where this value appears (expecting exactly two)
        positions = np.argwhere(input_grid == value)

        # Skip if we don't have exactly two positions
        if len(positions) != 2:
            continue

        # Extract the start and end positions
        start_pos, end_pos = positions[0], positions[1]

        # Calculate direction vector and number of steps
        direction_vector = np.array(end_pos) - np.array(start_pos)
        num_steps = max(abs(direction_vector))

        # Normalize direction vector for even stepping
        if num_steps > 0:
            normalized_direction = direction_vector / num_steps
        else:
            normalized_direction = direction_vector

        # Draw the line connecting the two positions
        for step in range(num_steps + 1):
            # Calculate position at current step
            current_pos = start_pos + np.round(step * normalized_direction).astype(int)
            row, col = current_pos

            # Place the value at the current position
            output_grid[row, col] = value

    return output_grid


def solve_7d1f7ee8(input_grid):
    """
    Concept:
    Color nested rectangles with the color of their containing rectangle.

    Steps:
    1. Identify all rectangles in the grid by their outlines.
    2. Create a copy of the grid and remove interior of all rectangles.
    3. Find the outermost rectangles that remain after this process.
    4. For each outermost rectangle, color all interior rectangles with its color.
    5. Return the modified grid with colored nested rectangles.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Create a working copy to identify outermost rectangles
    working_grid = input_grid.copy()

    # Find all unique non-zero values (rectangle colors)
    unique_values = np.unique(input_grid[input_grid != 0])

    # First pass: hollow out all rectangles to identify nested structures
    for value in unique_values:
        # Find positions of the current value
        value_positions = np.argwhere(input_grid == value)

        # Group connected positions into separate rectangles
        rectangle_groups = group_connected_positions(value_positions)

        # Process each rectangle
        for rectangle in rectangle_groups:
            rectangle = np.array(rectangle)

            # Find rectangle boundaries
            min_row, min_col = rectangle.min(axis=0)
            max_row, max_col = rectangle.max(axis=0)

            # Remove the interior (hollow out the rectangle)
            # This helps identify which rectangles are outermost
            working_grid[min_row + 1 : max_row, min_col + 1 : max_col] = 0

    # Find remaining values in the working grid (these are outermost rectangles)
    outermost_rectangle_values = np.unique(working_grid[working_grid != 0])

    # Second pass: color interior rectangles with the color of their container
    for value in outermost_rectangle_values:
        # Find positions of the current outermost rectangle
        value_positions = np.argwhere(working_grid == value)

        # Find outermost rectangle boundaries
        min_row, min_col = value_positions.min(axis=0)
        max_row, max_col = value_positions.max(axis=0)

        # Extract the interior region from the output grid
        interior_region = output_grid[min_row + 1 : max_row, min_col + 1 : max_col]

        # Find non-zero positions in the interior (these are nested rectangles)
        non_zero_interior = np.argwhere(interior_region != 0)

        # Color these positions with the value of the outermost rectangle
        if non_zero_interior.size > 0:
            interior_region[non_zero_interior[:, 0], non_zero_interior[:, 1]] = value

        # Update the output grid with the modified interior
        output_grid[min_row + 1 : max_row, min_col + 1 : max_col] = interior_region

    return output_grid


def solve_4a1cacc2(input_grid):
    """
    Concept:
    Identify the non-8  (non-background) value in the grid and extend it from its position to the closest corner,
    filling a rectangular region.

    Steps:
    1. Find the unique non-8 (non-background) value in the grid.
    2. Locate the position of this value.
    3. Determine which corner is closest to this position.
    4. Fill a rectangular region from the value's position to the closest corner with this value.
    5. Return the modified grid.
    """

    # Convert input to numpy array
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find the unique non-8 value (assumes there's only one such value)
    non_8_value = np.unique(input_grid[input_grid != 8])[0]

    # Find the position of the non-8 value (assumes it appears at only one position)
    non_8_position = np.argwhere(input_grid == non_8_value)[0]
    row, col = tuple(non_8_position)

    # Define the four corners of the grid
    corners = [
        (0, 0),  # Top-left
        (0, ncols - 1),  # Top-right
        (nrows - 1, 0),  # Bottom-left
        (nrows - 1, ncols - 1),  # Bottom-right
    ]

    # Calculate Euclidean distances from the non-8 value to each corner
    distances_to_corners = [np.linalg.norm(np.array(corner) - non_8_position) for corner in corners]

    # Find the closest corner
    closest_corner_index = np.argmin(distances_to_corners)

    # Fill the rectangular region from the non-8 value position to the closest corner
    if closest_corner_index == 0:  # Top-left corner
        output_grid[: row + 1, : col + 1] = non_8_value
    elif closest_corner_index == 1:  # Top-right corner
        output_grid[: row + 1, col:] = non_8_value
    elif closest_corner_index == 2:  # Bottom-left corner
        output_grid[row:, : col + 1] = non_8_value
    elif closest_corner_index == 3:  # Bottom-right corner
        output_grid[row:, col:] = non_8_value

    return output_grid


def solve_b60334d2(input_grid):
    """
    Concepts: Drawing a flower-like pattern at marked positions

    Transformation steps:
    1. Find all positions with value 5 in the input grid
    2. For each position with value 5:
       - Place 1s in the four adjacent positions (up, down, left, right)
       - Place 5s in the four diagonal positions (corners)
       - Replace the center position with 0
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find all positions containing value 5 (marker)
    pos_with_5 = np.argwhere(input_grid == 5)

    # Define relative positions for adjacent (cross) and diagonal (corner) cells
    cross_pos = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # down, right, up, left
    corner_pos = [[1, 1], [1, -1], [-1, 1], [-1, -1]]  # diagonals

    # Apply the transformation pattern for each position with value 5
    for pos in pos_with_5:
        r, c = tuple(pos)

        # Place 1s in the four adjacent positions (cross pattern)
        for dr, dc in cross_pos:
            nr, nc = r + dr, c + dc
            # Check if position is within grid boundaries
            if 0 <= nr < nrows and 0 <= nc < ncols:
                output_grid[nr, nc] = 1

        # Place 5s in the four diagonal positions (corner pattern)
        for dr, dc in corner_pos:
            nr, nc = r + dr, c + dc
            # Check if position is within grid boundaries
            if 0 <= nr < nrows and 0 <= nc < ncols:
                output_grid[nr, nc] = 5

        # delete center position to 0
        output_grid[r, c] = 0

    return output_grid


def solve_6c434453(input_grid):
    """
    Concepts: Pattern detection and transformation
    - Identifies 3x3 square ring patterns in the input grid
    - Replaces each square ring with a plus (+) pattern of value of different colors (value 2)

    Transformation steps:
    1. Find all connected components of non-zero values in the input grid
    2. For each component, check if it forms a 3x3 square ring pattern
    3. If a square ring is found:
       - Clear the 3x3 region containing the ring
       - Insert a plus (+) pattern with value of different colors (value 2) centered at the same location
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Convert input to numpy array and initialize output
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find connected components of non-zero values
    non_zero_positions = np.argwhere(input_grid != 0)
    connected_components = group_connected_positions(non_zero_positions, connectivity=4)

    # Define the target patterns
    square_ring_pattern = [
        [0, 0],
        [0, 1],
        [0, 2],  # Top edge
        [1, 0],
        [1, 2],  # Middle row (sides only)
        [2, 0],
        [2, 1],
        [2, 2],
    ]  # Bottom edge
    square_ring_set = set(map(tuple, square_ring_pattern))

    # Define the plus pattern to insert
    plus_pattern = [
        [0, 0],  # Center
        [1, 0],  # Down
        [0, 1],  # Right
        [-1, 0],  # Up
        [0, -1],
    ]  # Left

    # Process each connected component
    for component in connected_components:
        component = np.array(component)

        # Get bounding box of the component
        min_row, min_col = component.min(axis=0)
        max_row, max_col = component.max(axis=0)

        # Normalize component coordinates to origin (0,0)
        normalized_component = component - np.array([min_row, min_col])
        component_set = set(map(tuple, normalized_component))

        # Check if component matches square ring pattern
        if component_set == square_ring_set:
            # Clear the region containing the square ring
            output_grid[min_row : max_row + 1, min_col : max_col + 1] = 0

            # Calculate center position
            center_row = (min_row + max_row) // 2
            center_col = (min_col + max_col) // 2

            # Insert plus pattern
            for dr, dc in plus_pattern:
                new_row, new_col = center_row + dr, center_col + dc
                if 0 <= new_row < nrows and 0 <= new_col < ncols:
                    output_grid[new_row, new_col] = 2

    return output_grid


def solve_810b9b61(input_grid):
    """
    Detect rectangular rings in the input grid and transform their color.

    Concepts:
    - Pattern detection: Find hollow rectangular shapes (rings)
    - Shape analysis: Verify ring properties (border=1, interior=0)
    - Color transformation: Change ring color from 1 to 3

    Transformation steps:
    1. Find connected components of non-zero values
    2. For each component:
       - Extract the bounding box
       - Check if it forms a valid rectangular ring
       - If valid, change ring color from 1 to 3

    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Convert input to numpy array and initialize output
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find the non-zero value (assuming single value)
    non_zero_values = np.unique(input_grid[input_grid != 0])
    if len(non_zero_values) == 0:
        return output_grid
    non_zero_val = non_zero_values[0]

    # Find connected components
    ring_positions = np.argwhere(input_grid == non_zero_val)
    connected_components = group_connected_positions(ring_positions, connectivity=4)

    # Process each potential rectangular ring
    for component in connected_components:
        # Convert to numpy array for easier manipulation
        component = np.array(component)

        # Get bounding box coordinates
        min_row, min_col = component.min(axis=0)
        max_row, max_col = component.max(axis=0)

        # Extract the block and its interior
        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]
        interior = block[1:-1, 1:-1]

        # Create mask for ring detection (True for border, False for interior)
        ring_mask = np.ones_like(block, dtype=bool)
        ring_mask[1:-1, 1:-1] = False

        # Check if block forms a valid rectangular ring:
        # - Must have an interior (not a solid block)
        # - Border must be all 1s
        # - Interior must be all 0s
        is_valid_ring = (
            len(interior) > 0
            and np.all(block[ring_mask] == non_zero_val)
            and np.all(block[~ring_mask] == 0)
        )

        if is_valid_ring:
            # Transform ring color from 1 to 3
            block[ring_mask] = 3
            output_grid[min_row : max_row + 1, min_col : max_col + 1] = block

    return output_grid


def solve_95a58926(input_grid):
    """
    Transform a grid by removing noise and creating a regular partitioning pattern.

    Concepts:
    - Pattern cleaning: Remove noise cells while preserving structural elements
    - Grid partitioning: Create regular grid divisions with horizontal and vertical lines
    - Intersection marking: Place special markers at line intersections

    Transformation steps:
    1. Remove noise cells (non 0 and non 5) from the grid
    2. Determine the size of partitioning blocks by finding first line marker
    3. Create regular horizontal and vertical partition lines
    4. Place noise value markers at line intersections

    """

    # Convert input to numpy array and create working copy
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    nrows, ncols = input_grid.shape

    # Constants for grid values (colors)
    BACKGROUND = 0
    PARTITION_LINE = 5

    # Find the noise value (any value that's not background or partition line)
    noise_mask = (input_grid != BACKGROUND) & (input_grid != PARTITION_LINE)
    noise_val = np.unique(input_grid[noise_mask])[0]  # Assume single noise value

    # Clean grid by removing noise
    output_grid[output_grid == noise_val] = BACKGROUND

    # Find partition block size by locating first partition line
    block_size = 0
    for size in range(max(nrows, ncols)):
        if np.any(output_grid[:size, :size] == PARTITION_LINE):
            block_size = size
            break

    # Calculate partition line positions
    # Subtract 1 to convert from size to index
    partition_rows = (
        np.array([i * block_size for i in range(1, nrows) if i * block_size <= nrows]) - 1
    )
    partition_cols = (
        np.array([i * block_size for i in range(1, ncols) if i * block_size <= ncols]) - 1
    )

    # complete partition grid pattern
    output_grid[partition_rows, :] = PARTITION_LINE  # Horizontal lines
    output_grid[:, partition_cols] = PARTITION_LINE  # Vertical lines

    # Mark intersections with noise value
    for row in partition_rows:
        for col in partition_cols:
            output_grid[row, col] = noise_val

    return output_grid


def solve_1c786137(input_grid):
    """
    Detects a rectangular frame in a grid and returns its interior region.

    Concepts:
    - Connected component analysis
    - Frame detection via boundary validation

    Transformation steps:
    1. Identify connected components for each non-background value.
    2. For each component, check if it forms a valid rectangular frame:
       - Top/bottom rows and left/right columns are filled with the same value
       - Interior is not filled.
    3. Return the interior of the first detected frame.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    def is_frame(component):
        """Check if a component forms a valid rectangular frame."""
        if len(component) < 8:  # Minimum size for a frame
            return False

        positions = np.array(component)
        min_row, min_col = positions.min(axis=0)
        max_row, max_col = positions.max(axis=0)
        height = max_row - min_row + 1
        width = max_col - min_col + 1

        if height < 3 or width < 3:  # Minimum dimensions
            return False

        mask = np.zeros((height, width), dtype=bool)
        for r, c in component:
            mask[r - min_row, c - min_col] = True

        return (
            np.all(mask[0, :])  # Top row should be filled
            and np.all(mask[-1, :])  # Bottom row should be filled
            and np.all(mask[:, 0])  # Left column should be filled
            and np.all(mask[:, -1])  # Right column should be filled
            and not np.all(mask[1:-1, 1:-1])  # Interior should be empty
        )

    input_grid = np.array(input_grid)
    frames = []
    values = np.unique(input_grid[input_grid != 0])
    for val in values:
        positions = np.argwhere(input_grid == val)
        components = group_connected_positions(positions, connectivity=4)
        for component in components:
            if is_frame(component):
                positions = np.array(component)
                min_row, min_col = positions.min(axis=0)
                max_row, max_col = positions.max(axis=0)
                frames.append((min_row, min_col, max_row, max_col, val))

    # Return the interior of the first detected frame (assuming only one frame exist)
    if frames:
        min_row, min_col, max_row, max_col, _ = frames[0]
        output_grid = input_grid[min_row + 1 : max_row, min_col + 1 : max_col]
        return output_grid

    # If no frame found, return an empty array
    return np.array([])


def solve_8dae5dfc(input_grid):
    """
    Transform nested rectangular frames by reversing their color values.

    Concepts:
    - Connected component analysis: Group adjacent non-zero cells, each group is made of nested rectangular frames
    - Pattern recognition: Identify nested rectangular frames colors (values)
    - Color transformation: Reverse the order of colors from outer to inner frame

    Transformation steps:
    1. Find connected components of non-zero values
    2. For each component:
        a. Extract the rectangular block containing the component
        b. Identify unique colors from outer to inner frame
        c. Reverse the color ordering and apply to frames

    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find connected components of non-zero values
    non_zero_positions = np.argwhere(input_grid != 0)
    connected_components = group_connected_positions(non_zero_positions)

    # Process each connected component
    for component in connected_components:
        # Get bounding box of component
        component = np.array(component)
        min_row, min_col = component.min(axis=0)
        max_row, max_col = component.max(axis=0)
        height = max_row - min_row + 1
        width = max_col - min_col + 1

        # Extract block containing the component
        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

        # Identify unique colors from outer to inner frames
        # Sample middle column from top to center to get frame colors
        frame_colors = []
        for row in range(height // 2 + 1):
            color = block[row, width // 2]
            if color not in frame_colors:
                frame_colors.append(color)

        # Reverse color ordering for transformation
        reversed_colors = frame_colors[::-1]

        # Apply reversed colors to each frame
        output_block = block.copy()
        for old_color, new_color in zip(frame_colors, reversed_colors):
            color_positions = np.argwhere(block == old_color)
            output_block[color_positions[:, 0], color_positions[:, 1]] = new_color

        # Update output grid with transformed block
        output_grid[min_row : max_row + 1, min_col : max_col + 1] = output_block

    return output_grid


def solve_2753e76c(input_grid):
    """
    Create a summary grid showing the number of connected components for each value (color).

    Concepts:
    - Connected component analysis: Group adjacent cells with same value
    - Component counting: Track number of distinct connected regions per value
    - Create a summary grid showing the number of connected components for each value (color).

    Transformation steps:
    1. Find all non-zero values in the input grid
    2. For each value, count its connected components
    3. Sort values by number of components (descending)
    4. Create output grid where:
       - Each row represents a unique value as per the sorted list
       - Row length equals max number of components for that value
       - Values are right-aligned based on component count

    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)

    # Find all non-zero values
    non_zero_vals = np.unique(input_grid[input_grid != 0])

    # Count connected components for each value
    component_counts = []
    for val in non_zero_vals:
        # Find all positions of current value
        value_positions = np.argwhere(input_grid == val)
        # Group into connected components
        connected_regions = group_connected_positions(value_positions)
        # Store number of components
        component_counts.append(len(connected_regions))

    # Sort values by number of components (descending)
    sort_order = np.argsort(component_counts)[::-1]
    max_components = component_counts[sort_order[0]]

    # Create output grid
    num_values = len(non_zero_vals)
    output_grid = np.zeros((num_values, max_components), dtype=int)

    # Fill output grid with values as per the sorted order, right-aligned by component count
    for row, original_idx in enumerate(sort_order):
        value = non_zero_vals[original_idx]
        count = component_counts[original_idx]
        # Place value in rightmost positions based on component count
        output_grid[row, -count:] = value

    return output_grid


def solve_c6e1b8da(input_grid):
    """
    Transform shapes by moving rectangles to stick ends and filling gaps.

    Concepts:
    - Connected component analysis
    - Rectangle detection and extraction
    - Directional movement based on stick position
    - Gap filling in transformed shapes

    Transformation steps:
    1. Find all non-zero connected components (they will be overlapping rectangles with and without sticks)
    2. For each component:
        a. Extract bounding box
        b. If contains gaps (stick), identify stick direction
        c. Move rectangle part to stick end
    3. Fill any occurred gaps in the rectangles in output

    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    def move_rectangle(block, direction, dimensions):
        """Helper to extract and position rectangle based on stick direction."""
        H, W = dimensions
        if direction == "bottom":
            return block[0:min_r, :], H - min_r
        elif direction == "right":
            return block[:, 0:min_c], W - min_c
        elif direction == "top":
            return block[max_r + 1 :, :], 0
        else:  # left
            return block[:, max_c + 1 :], 0

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Process each non-zero value
    for val in np.unique(input_grid[input_grid != 0]):
        positions = np.argwhere(input_grid == val)
        components = group_connected_positions(positions)

        # Handle each connected component
        for component in components:
            component = np.array(component)
            min_row, min_col = component.min(axis=0)
            max_row, max_col = component.max(axis=0)
            height, width = max_row - min_row + 1, max_col - min_col + 1

            block = input_grid[min_row : max_row + 1, min_col : max_col + 1]
            if not np.any(block == 0):
                continue

            # Clear original component
            output_grid[component[:, 0], component[:, 1]] = 0

            # Find stick position
            non_val_pos = np.argwhere(block != val)
            min_r, min_c = non_val_pos.min(axis=0)
            max_r, max_c = non_val_pos.max(axis=0)

            # Determine stick direction and move rectangle
            if min_r != 0:  # stick is along a row till the bottom of the block
                direction = "bottom"
            elif min_c != 0:  # stick is along a column till the right boundary of the block
                direction = "right"
            elif max_r != height - 1:  # stick is along a row till the top of the block
                direction = "top"
            else:  # stick is along a column till the left boundary of the block
                direction = "left"

            rectangle, shift = move_rectangle(block, direction, (height, width))

            # Place rectangle in new position
            if direction in ["bottom", "top"]:
                output_grid[
                    min_row + shift : min_row + shift + rectangle.shape[0],
                    min_col : min_col + rectangle.shape[1],
                ] = rectangle
            else:
                output_grid[
                    min_row : min_row + rectangle.shape[0],
                    min_col + shift : min_col + shift + rectangle.shape[1],
                ] = rectangle

    # if any gap occures in the rectangles in output, fill them
    for val in np.unique(output_grid[output_grid != 0]):
        positions = np.argwhere(output_grid == val)
        components = group_connected_positions(positions)
        for component in components:
            component = np.array(component)
            min_row, min_col = component.min(axis=0)
            max_row, max_col = component.max(axis=0)
            block = output_grid[min_row : max_row + 1, min_col : max_col + 1]
            block[block == 0] = val
            output_grid[min_row : max_row + 1, min_col : max_col + 1] = block

    return output_grid


def solve_74dd1130(input_grid):
    """
    Transpose the input grid by swapping rows and columns.

    Concepts:
    - Matrix transposition: Convert rows to columns and columns to rows

    Transformation steps:
    1. Transpose the input grid using numpy's .T property.

    """

    # Convert input to numpy array and transpose
    input_grid = np.array(input_grid)
    output_grid = input_grid.T

    return output_grid


def solve_ded97339(input_grid):
    """
    Connect aligned non-zero values by horizontal or vertical lines in the grid.

    Concepts:
    - Pattern detection: Find aligned non-zero values
    - Line drawing: Connect values along rows and columns
    - Value preservation: Maintain original values while filling connections

    Transformation steps:
    1. Find positions of non-zero values
    2. For each position:
        a. Check same row for other non-zero values
        b. Check same column for other non-zero values
        c. Fill the gaps between aligned values
    3. Return modified grid with connections

    """
    # Convert to numpy array
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    nrows, ncols = input_grid.shape

    # Find all non-zero positions
    positions = list(zip(*np.where(input_grid != 0)))

    # Process each non-zero position
    for r1, c1 in positions:
        val = input_grid[r1, c1]

        # Check same row for other values
        for c2 in range(ncols):
            if c2 != c1 and input_grid[r1, c2] == val:
                # Fill between aligned horizontal values
                start, end = min(c1, c2), max(c1, c2)
                output_grid[r1, start : end + 1] = val

        # Check same column for other values
        for r2 in range(nrows):
            if r2 != r1 and input_grid[r2, c1] == val:
                # Fill between aligned vertical values
                start, end = min(r1, r2), max(r1, r2)
                output_grid[start : end + 1, c1] = val

    return output_grid


def solve_a1aa0c1e(input_grid):
    """
    Summarize heights of non-zero values (excluding 0, 5, 9) in the grid.

    Concepts:
    - Pattern detection: Identify specific values and their locations
    - Bounding box calculation: Find boundaries of value regions
    - Value filtering: Exclude specific numbers from analysis
    - Position tracking: Record minimum row positions for ordering

    Transformation steps:
    1. Extract unique values (excluding 0, 5, 9)
    2. Create output grid based on unique value count
    3. For each value:
        a. Find positions and bounding box
        b. Calculate minimum row position
        c. Order values by minimum row position
    4. Fill output grid based on ordered values
    5. Add special handling for value 5
    """

    input_grid = np.array(input_grid)

    # Find unique values excluding 0, 5, 9
    excluded = {0, 5, 9}
    unique_vals = [val for val in np.unique(input_grid) if val not in excluded]

    # Initialize output grid
    output_grid = np.zeros((len(unique_vals), len(unique_vals) + 2), dtype=int)
    output_grid[:, -2] = 9  # Set second-to-last column to 9

    # Track minimum row positions for ordering
    min_rows = []
    for val in unique_vals:
        positions = np.argwhere(input_grid == val)
        min_rows.append(positions[:, 0].min())

    # Process values in order of minimum row position
    order = np.argsort(min_rows)
    for i, o in enumerate(order):
        val = unique_vals[o]
        positions = np.argwhere(input_grid == val)

        if len(positions) > 0:
            # Calculate bounding box
            min_row = positions[:, 0].min()
            max_row = positions[:, 0].max()
            height = max_row - min_row + 1

            # Fill output grid based on height
            output_grid[i, : max(0, height // 2 - 1)] = val

    # Special handling for value 5
    row_with_4 = np.where(output_grid == 4)[0]
    if row_with_4.size == 0:
        row_with_8 = np.where(output_grid == 8)[0]
        if row_with_8.size > 0:
            output_grid[row_with_8, -1] = 5
    else:
        output_grid[row_with_4, -1] = 5

    return output_grid


def solve_516b51b7(input_grid):
    """
    Find rectangles of connected 1s and convert them into nested frames with alternating values.

    Concepts:
    - Rectangle detection: Identify boundaries of connected 1s in input grid
    - Frame generation: Create concentric frames with alternating value pattern
    - Pattern application: Apply values 1->2->3->2 from outside to inside

    Transformation steps:
    1. Convert input to numpy array
    2. Find positions of all 1s in the grid
    3. Group connected 1s into rectangles
    4. For each rectangle:
       a. Determine boundaries (min/max row/column)
       b. Calculate how many nested frames fit inside
       c. Fill frames from outside to inside with pattern [1,2,3,2]
    5. Return the transformed grid
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Convert input to numpy array and initalize empty ouput grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Find positions of 1s
    one_positions = np.argwhere(input_grid == 1)
    if len(one_positions) == 0:
        return output_grid

    # Group connected 1s into rectangles
    groups = group_connected_positions(one_positions)

    # Process each rectangle
    for group in groups:
        group = np.array(group)

        # Find rectangle boundaries
        min_row, min_col = group.min(axis=0)
        max_row, max_col = group.max(axis=0)

        # Calculate dimensions
        height = max_row - min_row + 1
        width = max_col - min_col + 1

        # Create nested frames
        num_layers = (min(height, width) + 1) // 2
        frame_values = [1, 2, 3, 2]  # Pattern to repeat

        # Fill frames from outside to inside
        for layer in range(num_layers):
            value = frame_values[layer % len(frame_values)]

            # Top and bottom edges
            output_grid[min_row + layer, min_col + layer : max_col - layer + 1] = value
            output_grid[max_row - layer, min_col + layer : max_col - layer + 1] = value

            # Left and right edges
            output_grid[min_row + layer : max_row - layer + 1, min_col + layer] = value
            output_grid[min_row + layer : max_row - layer + 1, max_col - layer] = value

    return output_grid


def solve_6350f1f4(input_grid):
    """
    Removes noise (replacing 5's with 0's), detects square patterns in a grid separated by rows/columns of zeros,
    and transforms these squares by either filling them with the most common value or replacing them with a reference pattern.

    Concepts:
    - Noise removal: Remove noise values (5's) from the grid
    - Pattern detection: Find complete patterns in grid subsections (squares)
    - Pattern transformation: Apply transformation rules to grid subsections (squares)

    Transformation steps:
    1. Remove noise by replacing 5's with 0's. grid is partitioned into squares by rows and columns of 0s
    2. Identify square size using first all-zero row
    3. Find a reference pattern from the square with non-zero values
    4. Apply pattern transformation rules to each square (subsection):
       - If square contains the most frequent value from pattern, fill with that value
       - If square has no values matching the most frequent value, replace with pattern
    """

    # Convert input to numpy array and create output grid
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Remove noise (replace 5's with 0's)
    output_grid = np.where(input_grid == 5, 0, output_grid)

    # Find first row of all 0s to determine subsection size
    size = 0
    for r in range(nrows):
        if np.all(output_grid[r] == 0):
            size = r
            break

    # If no all-zero row found, return the cleaned grid
    if size == 0:
        return output_grid

    # Find a reference pattern from non-zero subsections
    pattern = None
    for r in range(0, nrows, size + 1):
        for c in range(0, ncols, size + 1):
            block = output_grid[r : r + size, c : c + size]
            if np.all(block != 0):
                pattern = block.copy()
                break

    # If no pattern found, return the cleaned grid
    if pattern is None:
        return output_grid

    # Find most frequent value in the pattern
    unique, count = np.unique(pattern, return_counts=True)
    most_frequent = unique[np.argmax(count)]

    # Apply transformation to each subsection
    for r in range(0, nrows, size + 1):
        for c in range(0, ncols, size + 1):
            block = output_grid[r : r + size, c : c + size]

            # Apply transformation rules
            if np.any(block == most_frequent):
                output_grid[r : r + size, c : c + size] = most_frequent
            elif np.all(block != most_frequent):
                output_grid[r : r + size, c : c + size] = pattern

    return output_grid


def solve_5614dbcf(input_grid):
    """
    Downsamples a larger grid to a 3x3 grid by taking the most frequent value (majority vote) from each block.

    Concepts:
    - Grid downsampling: Reduces a large grid into a smaller 3x3 representation by majority vote
    - Statistical sampling: Uses the most frequent value in each block as representative
    - Block processing: Divides the input grid into equal-sized blocks for analysis

    Steps:
    1. Divide the input grid into 3x3 blocks (or as many as fit)
    2. For each block, find the most frequently occurring value
    3. Place this value in the corresponding position of a new 3x3 output grid
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros((3, 3), dtype=int)

    size = 3

    for i in range(0, nrows, size):
        for j in range(0, ncols, size):
            if i + size <= nrows and j + size <= ncols:
                block = input_grid[i : i + size, j : j + size]
                unique, count = np.unique(block, return_counts=True)
                most_frequent = unique[np.argmax(count)]
                out_row, out_col = i // size, j // size
                if out_row < 3 and out_col < 3:
                    output_grid[out_row, out_col] = most_frequent

    return output_grid


def solve_7d7772cc(input_grid):
    """
    Detects a bracket-shaped frame (any 90° rotation) extending fully along the grid boundary
    moving special values toward the frame or opposite edge if match is found or not.

    Concepts:
    - Frame detection: Identifies bracket-like frames using grid boundaries
    - Value classification: Distinguishes between background, frame, and special values
    - Spatial transformation: move toward the frame or opposite edge if match is found or not.

    Transformation steps:
    1. Identify the frame value, its inner and outer background values
    2. Find the boundary coordinates of the frame
    3. For each direction (top, bottom, left, right):
       - If a special value appears once in a row/column, move it to the frame edge
       - If multiple special values appear, move them to the grid edge
    """

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    nrows, ncols = input_grid.shape

    # Detect background and frame values using grid boundaries
    boundaries = [input_grid[0, :], input_grid[-1, :], input_grid[:, 0], input_grid[:, -1]]
    outer_background_val = None
    frame_val = None
    inner_background_val = None

    for b in boundaries:
        unique_vals = np.unique(b)
        if len(unique_vals) == 1:
            outer_background_val = unique_vals[0]
        if len(unique_vals) == 2:
            if b[0] == b[-1]:
                frame_val = b[0]
                inner_background_val = [v for v in unique_vals if v != frame_val][0]

    # Find frame boundaries
    frame_pos = np.argwhere(input_grid == frame_val)
    min_row, min_col = np.min(frame_pos, axis=0)
    max_row, max_col = np.max(frame_pos, axis=0)

    # Process bottom frame (when frame doesn't touch top)
    if min_row != 0:  # frame is touching bottom, we go column wise
        for c in range(ncols):
            col = input_grid[:, c]
            special_vals = set(col) - {inner_background_val, outer_background_val, frame_val}
            # if there is only one special value (matching case)
            if len(special_vals) == 1:
                special_val = list(special_vals)[0]
                pos = np.where(col == special_val)[0]

                min_r = np.min(pos)
                # move it along the column to just outside edge of the frame
                output_grid[min_r, c] = outer_background_val
                output_grid[min_row - 1, c] = special_val
            else:  # if there are more than one special value (non matching case)
                for special_val in special_vals:
                    pos = np.where(col == special_val)[0]
                    min_r = np.min(pos)
                    if min_r < min_row:  # this value is outside the frame, move it to the top
                        output_grid[min_r, c] = outer_background_val
                        output_grid[0, c] = special_val

    # Process right frame (when frame doesn't touch left)
    if min_col != 0:  # frame is touching right, we go row wise
        for r in range(nrows):
            row = input_grid[r, :]
            special_vals = set(row) - {inner_background_val, outer_background_val, frame_val}
            # if there is only one special value (matching case)
            if len(special_vals) == 1:
                special_val = list(special_vals)[0]
                pos = np.where(row == special_val)[0]
                min_c = np.min(pos)
                # move it along the row to just outside edge of the frame
                output_grid[r, min_c] = outer_background_val
                output_grid[r, min_col - 1] = special_val
            else:  # if there are more than one special value (non matching case)
                for special_val in special_vals:
                    pos = np.where(row == special_val)[0]
                    min_c = np.min(pos)
                    if min_c < min_col:  # this value is outside the frame, move it to the left
                        output_grid[r, min_c] = outer_background_val
                        output_grid[r, 0] = special_val

    # Process left frame (when frame doesn't touch right)
    if max_col != ncols - 1:  # frame is touching left, we go row wise
        for r in range(nrows):
            row = input_grid[r, :]
            special_vals = set(row) - {inner_background_val, outer_background_val, frame_val}
            # if there is only one special value (matching case)
            if len(special_vals) == 1:
                special_val = list(special_vals)[0]
                pos = np.where(row == special_val)[0]
                max_c = np.max(pos)
                # move it along the row to just outside edge of the frame
                output_grid[r, max_c] = outer_background_val
                output_grid[r, max_col + 1] = special_val
            else:  # if there are more than one special value (non matching case)
                for special_val in special_vals:
                    pos = np.where(row == special_val)[0]
                    max_c = np.max(pos)
                    if max_c > max_col:  # this value is outside the frame, move it to the right
                        output_grid[r, max_c] = outer_background_val
                        output_grid[r, ncols - 1] = special_val

    # Process top frame (when frame doesn't touch bottom)
    if max_row != nrows - 1:  # frame is touching top, we go column wise
        for c in range(ncols):
            col = input_grid[:, c]
            special_vals = set(col) - {inner_background_val, outer_background_val, frame_val}
            # if there is only one special value (matching case)
            if len(special_vals) == 1:
                special_val = list(special_vals)[0]
                pos = np.where(col == special_val)[0]
                max_r = np.max(pos)
                # move it along the column to just outside edge of the frame
                output_grid[max_r, c] = outer_background_val
                output_grid[max_row + 1, c] = special_val
            else:  # if there are more than one special value (non matching case)
                for special_val in special_vals:
                    pos = np.where(col == special_val)[0]
                    max_r = np.max(pos)
                    if max_r > max_row:  # this value is outside the frame, move it to the bottom
                        output_grid[max_r, c] = outer_background_val
                        output_grid[nrows - 1, c] = special_val

    return output_grid


def solve_c48954c1(input_grid):
    """
    Unfolding Symmetric Pattern
    Creates a symmetric pattern by mirroring the input grid in multiple directions.

    Concepts:
    - Reflective symmetry: Creates horizontal and vertical reflections of the input grid
    - Tiling: Combines the original grid with its reflections to create a larger pattern
    - Self-similarity: Generates a fractal-like structure with the input repeated in a pattern

    Transformation steps:
    1. Create a horizontal reflection of the input grid (left-right flip)
    2. Construct a middle row by placing the original grid between two of its horizontal reflections
    3. Create vertical reflections (top-bottom flips) of this middle row
    4. Stack these three rows (reflection, original middle row, reflection) to create a 3x3 tile pattern
    """

    input_grid = np.array(input_grid)

    # Step 1: Create horizontal reflection of the grid
    flipped_lr = np.fliplr(input_grid)

    # Step 2: Build the middle row by placing the original between two reflections
    middle_stack = np.hstack((flipped_lr, input_grid, flipped_lr))

    # Step 3: Create vertical reflections of the middle row
    top_stack = np.flipud(middle_stack)
    bottom_stack = np.flipud(middle_stack)  # Same as top_stack

    # Step 4: Stack the three rows vertically to create the final pattern
    output_grid = np.vstack((top_stack, middle_stack, bottom_stack))

    return output_grid


def solve_dc2aa30b(input_grid):
    """
    Rearranges grid blocks based on their content of value 2 from right to left, top to bottom row-wise.

    Concepts:
    - Block detection: Identifies grid partitions separated by rows of zeros
    - Content analysis: Counts occurrences of value 2 in each block
    - Spatial reorganization: Rearranges blocks by descending count in right-to-left order

    Transformation steps:
    1. Identify grid partitioning by detecting rows of zeros
    2. Extract individual blocks from the partitioned grid
    3. Count occurrences of value 2 in each block
    4. In the output grid, rearrange blocks in descending order of value 2 count from right to left, top to bottom row-wise
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros_like(input_grid)  # Start with empty grid of same size

    # Identify rows that consist entirely of zeros
    rows_with_0s = []
    for r in range(nrows):
        if np.all(input_grid[r] == 0):
            rows_with_0s.append(r)
    rows_with_0s = np.sort(rows_with_0s)

    # Calculate block size from the spacing between zero rows
    size = rows_with_0s[1] - rows_with_0s[0] - 1 if len(rows_with_0s) > 1 else nrows

    # Extract blocks and count value 2s in each
    blocks = []
    num_2s = []
    for r in range(0, nrows, size + 1):
        for c in range(0, ncols, size + 1):
            block = input_grid[r : r + size, c : c + size]
            count_2 = np.sum(block == 2)
            num_2s.append(count_2)
            blocks.append(block)

    # Get sort order for blocks by count of 2s
    order = np.argsort(num_2s)
    num_blocks = len(blocks)

    # Reshape order array and flip left-right for right-to-left ordering
    sqrt = int(np.sqrt(num_blocks))
    order = np.fliplr(order.reshape(sqrt, sqrt))

    # Place blocks in output grid according to new arrangement
    for i in range(sqrt):
        for j in range(sqrt):
            o = order[i, j]
            start_row = i * (size + 1)
            start_col = j * (size + 1)
            output_grid[start_row : start_row + size, start_col : start_col + size] = blocks[o]

    return output_grid


def solve_95755ff2(input_grid):
    """
    Diamond-fill: take non-zero border values (except 2) and propagate them
    inward along diamond-shaped columns/rows until they hit another value
    or the diamond boundary.

    Concept
    - Diamond frame recognition: Detect the diamond-shaped frame of 2s in the grid. (optional)
    - Border seeding: Take border values (non-zero, not 2) from the outermost rows/columns.
    - Value propagation: Spread these border values inward along rows/columns, constrained by the diamond boundary.
    - Selective filling: Only fill empty (0) cells inside the diamond, preserving existing values (including the 2 frame).

    Transformation Steps

    1. Identify the diamond-shaped frame made of 2s. (optional)
    2. Collect non-zero, non-2 values from the grid’s top, bottom, left, and right borders.
    3. For each collected border value:
        - If from top/bottom → propagate vertically inside the diamond.
        - If from left/right → propagate horizontally inside the diamond.
    4.Stop propagation when hitting another non-zero cell or the diamond’s edge.
    5. Return the updated grid with filled values inside the diamond.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    mid_row, mid_col = nrows // 2, ncols // 2

    # Fill columns (vertical patterns from top and bottom borders)
    for c in range(1, ncols - 1):
        # Process top border value
        value = input_grid[0, c]
        if value not in [0, 2]:
            if c < mid_col:  # Left side
                for r in range(mid_row - c + 1, mid_row + c):
                    if 0 <= r < nrows and output_grid[r, c] == 0:
                        output_grid[r, c] = value
                    else:
                        break
            elif c > mid_col:  # Right side
                for r in range(c - mid_col + 1, ncols - (c - mid_col + 1)):
                    if 0 <= r < nrows and output_grid[r, c] == 0:
                        output_grid[r, c] = value
                    else:
                        break

        # Process bottom border value
        value = input_grid[nrows - 1, c]
        if value not in [0, 2]:
            if c < mid_col:  # Left side
                for r in range(mid_row + c - 1, mid_row - c, -1):
                    if 0 <= r < nrows and output_grid[r, c] == 0:
                        output_grid[r, c] = value
                    else:
                        break
            elif c > mid_col:  # Right side
                for r in range(ncols - (c - mid_col) - 2, c - mid_col - 1, -1):
                    if 0 <= r < nrows and output_grid[r, c] == 0:
                        output_grid[r, c] = value
                    else:
                        break

    # Fill rows (horizontal patterns from left and right borders)
    for r in range(1, nrows - 1):
        # Process left border value
        value = input_grid[r, 0]
        if value not in [0, 2]:
            if r < mid_row:  # Top half
                for c in range(mid_col - r + 1, mid_col + r):
                    if 0 <= c < ncols and output_grid[r, c] == 0:
                        output_grid[r, c] = value
                    else:
                        break
            elif r > mid_row:  # Bottom half
                for c in range(r - mid_row + 1, ncols - (r - mid_row + 1)):
                    if 0 <= c < ncols and output_grid[r, c] == 0:
                        output_grid[r, c] = value
                    else:
                        break

        # Process right border value
        value = input_grid[r, ncols - 1]
        if value not in [0, 2]:
            if r < mid_row:  # Top half
                for c in range(ncols - (mid_row - r) - 1, mid_col, -1):
                    if 0 <= c < ncols and output_grid[r, c] == 0:
                        output_grid[r, c] = value
                    else:
                        break
            elif r > mid_row:  # Bottom half
                for c in range(ncols - (r - mid_row) - 2, r - mid_row - 1, -1):
                    if 0 <= c < ncols and output_grid[r, c] == 0:
                        output_grid[r, c] = value
                    else:
                        break

    return output_grid


def solve_c6141b15(input_grid):
    """
    Concept:
    Transform an input grid by identifying straight lines and non-line objects, then:
    - Create an output grid with background color 7
    - Place non-line objects at the line endpoints
    - Connect all centers of non-line objects with lines

    Transformation Steps:
    1. Identify background color (hard coded here as 7) and initialize empty output grid
    2. Classify objects in the input grid as either lines or non-line objects
    3. Extract line endpoints and non-line object patterns
    4. Place non-line objects at the line endpoints in the output grid
    5. Draw lines connecting all non-line object centers
    6. Return the transformed output grid
    """
    from arc_agi_2_atlas.providers.grid_utils import (
        group_connected_positions,
        is_straight_line,
        connect_points_with_lines,
    )

    # Convert input to numpy array
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Identify background color (assumed to be 7)
    background_color = 7

    # Create an output grid initialized with the background color
    output_grid = np.full_like(input_grid, background_color)

    def place_object(grid, center, object_pattern, background):
        """
        Place an object centered at the specified position.

        Args:
            grid: 2D numpy array representing the grid
            center: Tuple (row, col) for the center position
            object_pattern: 2D numpy array of the object pattern to place
            background: Background value to ignore when placing the pattern

        Returns:
            2D numpy array with the object placed
        """
        result = grid.copy()
        obj_height, obj_width = object_pattern.shape
        half_h, half_w = obj_height // 2, obj_width // 2

        # Calculate placement boundaries
        start_row = center[0] - half_h
        start_col = center[1] - half_w

        # Ensure the object fits within the grid
        if (
            start_row < 0
            or start_row + obj_height > grid.shape[0]
            or start_col < 0
            or start_col + obj_width > grid.shape[1]
        ):
            return result

        # Place the object, preserving background where the pattern has background value
        for r in range(obj_height):
            for c in range(obj_width):
                if object_pattern[r, c] != background:
                    result[start_row + r, start_col + c] = object_pattern[r, c]

        return result

    # Find all non-background values in the input grid
    non_background_values = np.unique(input_grid[input_grid != background_color])

    # Variables to store our findings
    non_line_pattern = None
    non_line_color = None
    non_line_centers = []
    line_endpoints = None
    line_color = None

    # Process each unique value in the grid
    for val in non_background_values:
        # Find all positions with this value
        positions = np.argwhere(input_grid == val)

        # Group connected positions
        connected_groups = group_connected_positions(positions, connectivity=8)

        for group in connected_groups:
            group_array = np.array(group)

            # Check if this group forms a straight line
            is_line, endpoints = is_straight_line(group_array)

            if is_line and endpoints is not None and len(endpoints) == 2:
                # This is a line - store its endpoints and color
                line_endpoints = [tuple(p) for p in endpoints]
                line_color = val
            else:
                # This is a non-line object - extract its pattern
                min_row, min_col = group_array.min(axis=0)
                max_row, max_col = group_array.max(axis=0)

                # Extract the object pattern (use the first non-line object found)
                if non_line_pattern is None:
                    non_line_pattern = input_grid[
                        min_row : max_row + 1, min_col : max_col + 1
                    ].copy()
                    non_line_color = val

                # Calculate center of the object
                center = (min_row + max_row) // 2, (min_col + max_col) // 2
                non_line_centers.append(center)

    # Make sure we found both a line and a non-line object
    if line_endpoints is None or non_line_pattern is None:
        return output_grid

    # Place non-line objects at both line endpoints
    for endpoint in line_endpoints:
        output_grid = place_object(output_grid, endpoint, non_line_pattern, background_color)

    # Draw lines connecting all non-line object centers
    output_grid = connect_points_with_lines(output_grid, non_line_centers, line_color)

    return output_grid


def solve_a5313dff(input_grid):
    """
    Fills isolated regions of 0s with 1s if they don't touch the grid border.

    Concept:
    Identify connected regions of 0s (empty spaces) and fill them with 1s
    if they are completely surrounded by other values 2s (i.e., don't touch the grid border).

    Transformation Steps:
    1. Find all positions with value 0 (empty spaces).
    2. Group these positions into connected components.
    3. For each connected component:
       a. Skip if any position touches the grid border.
       b. Fill the entire region with 1s if it's completely enclosed.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Convert input to numpy array if it's not already
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find all positions containing 0s
    empty_positions = np.argwhere(input_grid == 0)

    # If there are no empty positions, return the original grid
    if len(empty_positions) == 0:
        return output_grid

    # Group connected empty positions
    empty_regions = group_connected_positions(empty_positions, connectivity=4)

    # Process each connected region of empty positions
    for region in empty_regions:
        region = np.array(region)

        # Find the bounding box of the region
        min_row, min_col = region.min(axis=0)
        max_row, max_col = region.max(axis=0)

        # Skip regions that touch the grid border
        if min_row == 0 or min_col == 0 or max_row == nrows - 1 or max_col == ncols - 1:
            continue

        # Fill the enclosed empty region with 1s
        output_grid[region[:, 0], region[:, 1]] = 1

    return output_grid


def solve_b25e450b(input_grid):
    """
    Clears grass (color 5) in rows/columns based on grass cutters (color 0) at the edges,
    then repositions the grass cutters at the opposite edges.

    Concept:
    When a grass cutter (value 0) is placed at an edge of the grid, it clears all grass in
    the corresponding row or column and then moves to the opposite edge.

    Transformation Steps:
    1. Identify grass cutters (color 0) at the edges of the grid
    2. For each grass cutter:
       a. If at top/bottom edge, clear the entire column (replace with background color)
       b. If at left/right edge, clear the entire row (replace with background color)
    3. Reposition each grass cutter to the opposite edge:
       a. From top → bottom, bottom → top
       b. From left → right, right → left
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Convert input to numpy array if it's not already
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Define the background color (represents cleared grass)
    background_color = 7

    # Find all grass cutter positions (value 0)
    grass_cutter_positions = np.argwhere(input_grid == 0)

    # If there are no grass cutters, return the original grid
    if len(grass_cutter_positions) == 0:
        return output_grid

    # Group connected grass cutter positions
    grass_cutter_groups = group_connected_positions(grass_cutter_positions)

    # First pass: Clear grass in rows/columns based on grass cutter positions
    for cutter_group in grass_cutter_groups:
        cutter_group = np.array(cutter_group)
        min_row, min_col = cutter_group.min(axis=0)
        max_row, max_col = cutter_group.max(axis=0)
        height = max_row - min_row + 1
        width = max_col - min_col + 1

        # Check grass cutter position and clear corresponding row/column
        if min_row == 0:  # Grass cutter at the top edge
            output_grid[:, min_col : max_col + 1] = background_color  # Clear the entire column
        elif max_row == nrows - 1:  # Grass cutter at the bottom edge
            output_grid[:, min_col : max_col + 1] = background_color  # Clear the entire column
        elif min_col == 0:  # Grass cutter at the left edge
            output_grid[min_row : max_row + 1, :] = background_color  # Clear the entire row
        elif max_col == ncols - 1:  # Grass cutter at the right edge
            output_grid[min_row : max_row + 1, :] = background_color  # Clear the entire row

    # Second pass: Reposition grass cutters to opposite edges
    for cutter_group in grass_cutter_groups:
        cutter_group = np.array(cutter_group)
        min_row, min_col = cutter_group.min(axis=0)
        max_row, max_col = cutter_group.max(axis=0)
        height = max_row - min_row + 1
        width = max_col - min_col + 1

        # Reposition grass cutters based on their original position
        if min_row == 0:  # Grass cutter was at the top edge
            output_grid[-height:, min_col : max_col + 1] = 0  # Move to the bottom edge
        elif max_row == nrows - 1:  # Grass cutter was at the bottom edge
            output_grid[:height, min_col : max_col + 1] = 0  # Move to the top edge
        elif min_col == 0:  # Grass cutter was at the left edge
            output_grid[min_row : max_row + 1, -width:] = 0  # Move to the right edge
        elif max_col == ncols - 1:  # Grass cutter was at the right edge
            output_grid[min_row : max_row + 1, :width] = 0  # Move to the left edge

    return output_grid


def solve_af726779(input_grid):
    """
    Creating inverted triangles of alternating colors (7 and 6).

    Concept:
    For each row containing a specific value (top_value), identify pairs of adjacent occurrences
    and place another value (bottom_value) two rows below in the middle column between those pairs.
    This process is repeated alternating between two different values.

    Transformation Steps:
    1. Scan the grid from bottom to top to find rows containing the target value (top_value)
    2. Identify pairs of adjacent occurrences of this value in the row
    3. For each pair, place another value (bottom_value) two rows below in the middle column
    4. Alternate this process between two different values (7→6 and 6→7)
    """

    # Convert input to numpy array if it's not already
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    def place_row_below(grid, top_value, bottom_value):
        """
        Find pairs of top_value in a row that is closest to the grid-bottom and place bottom_value two rows below.

        Args:
            grid: The current grid state
            top_value: The value to look for in rows
            bottom_value: The value to place two rows below

        Returns:
            Updated grid with new values placed
        """
        # Find the last row from bottom containing the top_value
        row_with_top_value_id = None
        for r in range(nrows - 1, 0, -1):  # Scan from bottom to top
            if top_value in grid[r]:
                row_with_top_value_id = r
                break

        # If no row contains the top_value, return the grid unchanged
        if row_with_top_value_id is None:
            return grid

        # Get the row and positions of top_value in that row
        row_with_top_value = grid[row_with_top_value_id]
        positions = np.sort(np.where(row_with_top_value == top_value)[0])

        # Calculate target row for placement (two rows below)
        next_next_row_id = row_with_top_value_id + 2

        # Only proceed if the target row is within grid bounds
        if next_next_row_id < nrows:
            # For each pair of adjacent top_values, place bottom_value in between and two rows below
            for i in range(len(positions) - 1):
                middle_cols = list(range(positions[i] + 1, positions[i + 1]))
                # Only place if there's exactly one column between the pair
                if len(middle_cols) == 1:
                    grid[next_next_row_id, middle_cols[0]] = bottom_value

        return grid

    # Alternately apply the transformation for both value pairs 7->6 and 6->7 and so on
    for _ in range(nrows):
        output_grid = place_row_below(output_grid, top_value=7, bottom_value=6)
        output_grid = place_row_below(output_grid, top_value=6, bottom_value=7)

    return output_grid


def solve_712bf12e(input_grid):
    """
    Simulates the movement (towards top or right) of entities (value 2) through a grid with empty spaces (value 0)
    and blockers (value 5).

    Concept:
    Entities move according to specific rules: first try to move upward, and if blocked,
    try to move right. Continue movement until getting stuck or hitting the top edge of the grid.

    Transformation Steps:
    1. Identify all entities (value 2) in the grid
    2. For each entity, simulate movement according to the rules:
       a. First try to move up one cell if empty (value 0)
       b. If blocked above (value 5), try to move right if empty
       c. If blocked in both directions, entity stops moving
    3. Continue movement until entity reaches top boundary or gets stuck
    """

    # Convert input to numpy array if it's not already
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    def one_step_move(grid, start_pos):
        """
        Move an entity one step according to the movement rules.

        Args:
            grid: The current grid state
            start_pos: Current position of the entity (r, c)

        Returns:
            tuple: (updated_grid, new_position)
            - If the entity can move, updates the grid and returns new position
            - If the entity can't move, returns the original position
        """
        end_pos = None
        r, c = start_pos

        # First priority: Try to move up
        if r > 0 and grid[r - 1, c] == 0:  # Empty cell above
            grid[r - 1, c] = 2  # Move entity up
            end_pos = (r - 1, c)
        # Second priority: If blocked above, try to move right
        elif r > 0 and grid[r - 1, c] == 5:  # Blocker above
            # Try moving right if in bounds and empty
            if c + 1 < ncols and grid[r, c + 1] == 0:
                grid[r, c + 1] = 2  # Move entity right
                end_pos = (r, c + 1)
            else:  # Can't move - either out of bounds or blocked
                end_pos = (r, c)  # Stay in place
        else:  # Other scenarios (e.g., at top edge)
            end_pos = (r, c)  # Stay in place

        return grid, end_pos

    # Find all entities (value 2) in the grid
    entity_positions = np.argwhere(input_grid == 2)

    # Process each entity
    for pos in entity_positions:
        start_pos = tuple(pos)

        # Simulate movement (limit to maximum possible steps to avoid infinite loops)
        max_steps = nrows * ncols
        for _ in range(max_steps):
            # Remember original position to check if entity moved
            original_pos = start_pos

            # Move one step
            output_grid, end_pos = one_step_move(output_grid, start_pos)

            # Extract new position coordinates
            r_new, c_new = end_pos

            # Check termination conditions
            if end_pos == original_pos:  # No movement occurred
                break
            if r_new == 0:  # Reached the top edge
                break

            # Update starting position for next iteration
            start_pos = end_pos

    return output_grid


def solve_6150a2bd(input_grid):
    """
    Rotates the input grid 180 degrees (equivalent to flipping both horizontally and vertically).

    Concepts:
    - Matrix transformation: Applies a 180-degree rotation to the grid
    - Image processing: Similar to rotating an image upside down
    - Symmetry operations: Combines horizontal and vertical reflection

    Steps:
    1. Convert input to numpy array for matrix operations
    2. Flip the matrix left-right (horizontally) using np.fliplr()
    3. Flip the matrix up-down (vertically) using np.flipud()
    4. Return the transformed grid
    """
    input_grid = np.array(input_grid)

    # Apply 180-degree rotation by flipping both horizontally and vertically
    output_grid = np.fliplr(np.flipud(input_grid))

    # Alternatively, could use np.rot90 twice:
    # output_grid = np.rot90(input_grid, 2)  # Rotate 180 degrees

    return output_grid


def solve_97a05b5b(input_grid):
    """
    Patern matching and 3x3 block fitting.

    Concepts:
    - Component extraction: Identifies connected regions of non-zero values
    - Block prioritization: Uses the largest block as the base grid for output
    - Pattern fitting: Places smaller blocks in the output grid if patterns match (positions of 0s in the output grid match positions of 2s in the block)
    - Rotation matching: Rotates blocks to fit into available spaces

    Steps:
    1. Identify all connected non-zero components in the input grid
    2. Find the largest component to use as the base output grid
    3. Extract all other components as blocks to be placed
    4. Sort blocks by number of 2's they contain (descending)
    5. Place each block in available spaces where they fit/match (positions of 0s in output match positions of 2s in block)
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Convert input to numpy array and create initial output
    input_grid = np.array(input_grid)

    # Find all non-zero positions and group them into connected components
    pos_without_0 = np.argwhere(input_grid != 0)
    parts = group_connected_positions(pos_without_0)

    # Find the largest connected component
    biggest_block = None
    bigH, bigW = 0, 0
    other_blocks = []

    # Extract the largest block based on area
    for part in parts:
        part = np.array(part)
        min_row, min_col = np.min(part, axis=0)
        max_row, max_col = np.max(part, axis=0)
        H, W = max_row - min_row + 1, max_col - min_col + 1
        if H * W > bigH * bigW:
            bigH, bigW = H, W
            biggest_block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

    # Extract all other blocks with different dimensions
    for part in parts:
        part = np.array(part)
        min_row, min_col = np.min(part, axis=0)
        max_row, max_col = np.max(part, axis=0)
        H, W = max_row - min_row + 1, max_col - min_col + 1
        if H != bigH or W != bigW:
            other_blocks.append(input_grid[min_row : max_row + 1, min_col : max_col + 1])

    # Sort blocks by number of 2's they contain (descending)
    num_2s = [np.sum(blk == 2) for blk in other_blocks]
    order = np.argsort(num_2s)[::-1]
    other_blocks = [other_blocks[i] for i in order]

    def fill_output_grid(output_grid, blk):
        """
        Place a block in the output grid where it fits.
        Tries all four rotations and places at first valid position.
        """
        mask0 = output_grid == 0
        mask2 = blk == 2

        # Try each of the 4 possible rotations
        for k in range(4):
            mask2_rot = np.rot90(mask2, k=k)

            # Check all possible positions in the output grid
            for r in range(output_grid.shape[0] - mask2_rot.shape[0] + 1):
                for c in range(output_grid.shape[1] - mask2_rot.shape[1] + 1):
                    sub_mask0 = mask0[r : r + mask2_rot.shape[0], c : c + mask2_rot.shape[1]]

                    # If rotated block's pattern of 2's matches empty spaces of 0's
                    if np.array_equal(sub_mask0, mask2_rot):
                        blk_rot = np.rot90(blk, k=k)
                        output_grid[r : r + mask2_rot.shape[0], c : c + mask2_rot.shape[1]] = (
                            blk_rot
                        )
                        return output_grid

        return output_grid

    # Use the largest block as the base output grid
    output_grid = biggest_block.copy()

    # Fill in with remaining blocks
    for blk in other_blocks:
        output_grid = fill_output_grid(output_grid, blk)

    return output_grid


def solve_dbc1a6ce(input_grid):
    """
    Connects 1s in the grid with 8s along rows and columns.

    Concepts:
    - Draw straight lines (8s) between pairs of 1s in the same row or column

    Transformation Steps:
    1. Convert input to numpy array and create a copy for output
    2. Find all positions containing the value 1
    3. For each pair of 1s:
       a. If they share a row, fill all cells between them with 8s
       b. If they share a column, fill all cells between them with 8s
    4. Restore all original 1s that might have been overwritten
    """

    # Convert input to numpy array and create initial output
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find all positions of 1s
    pos_with_1 = np.argwhere(input_grid == 1)

    # Process each pair of 1s exactly once
    for i in range(len(pos_with_1)):
        for j in range(i + 1, len(pos_with_1)):
            r1, c1 = tuple(pos_with_1[i])
            r2, c2 = tuple(pos_with_1[j])

            # If 1s are in the same row, fill the path between them with 8s
            if r1 == r2:
                output_grid[r1, min(c1, c2) : max(c1, c2) + 1] = 8

            # If 1s are in the same column, fill the path between them with 8s
            elif c1 == c2:
                output_grid[min(r1, r2) : max(r1, r2) + 1, c1] = 8

    # Restore all original 1s that might have been overwritten with 8s
    output_grid[pos_with_1[:, 0], pos_with_1[:, 1]] = 1

    return output_grid


def solve_3bd67248(input_grid):
    """
    Draws colored lines on a grid: one along the anti-diagonal and one at the bottom.

    Concepts:
    - Line drawing on matrix (grid)

    Transformation Steps:
    1. Convert input to numpy array and create a copy for modification
    2. Draw a horizontal line of 4s across the bottom row (except first column)
    3. Draw an anti-diagonal line of 2s from top-right to bottom-left
    4. Return the modified grid
    """

    # Convert input to numpy array and create initial output
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Draw a horizontal line of 4s along the bottom row (starting from second column)
    output_grid[-1, 1:] = 4

    # Draw anti-diagonal line of 2s (from top-right to bottom-left), excluding  bottom left corner
    for i in range(nrows - 1):
        output_grid[i, ncols - 1 - i] = 2

    return output_grid


def solve_cb227835(input_grid):
    """
    Identifies two 8s in the input grid that are closest to opposite corners,
    then connects them with lines of 3s to form a boundary structure.

    Concepts:
    - Pattern recognition: Identifying 8s positioned near opposite corners
    - Boundary creation: Connecting corner elements with straight lines to form a boundary structure.
    - Grid transformation: Converting elements along line to value (color) 3

    Transformation Steps:
    1. Find all positions containing value 8 in the input grid
    2. Identify if 8s are positioned along main diagonal (top-left to bottom-right)
       or anti-diagonal (top-right to bottom-left)
    3. Draw lines of 3s connecting the 8s:
       a. Along diagonal paths between the 8s
       b. Vertically/ horizontally from 8s to form a boundary structure.
    """

    # Convert input to numpy array
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find all positions containing the value 8
    pos_with_8 = np.argwhere(input_grid == 8)

    # Get minimum and maximum row and column coordinates of 8s
    min_row, min_col = np.min(pos_with_8, axis=0)
    max_row, max_col = np.max(pos_with_8, axis=0)
    pos_with_8 = set(map(tuple, pos_with_8))

    if (min_row, min_col) in pos_with_8 and (max_row, max_col) in pos_with_8:
        # Case 1: 8s are positioned along main diagonal (top-left to bottom-right)

        # Draw diagonal line from top-left 8 downward and rightward
        for i in range(1, max(nrows, ncols)):
            r, c = min_row + i, min_col + i
            if 0 <= r < nrows and 0 <= c <= max_col:
                output_grid[r, c] = 3
            else:
                break

        # Draw diagonal line from bottom-right 8 upward and leftward
        for i in range(1, max(nrows, ncols)):
            r, c = max_row - i, max_col - i
            if 0 <= r < nrows and min_col <= c < ncols:
                output_grid[r, c] = 3
            else:
                break

        # Draw vertical line down from top-left 8
        for i in range(min_row + 1, nrows):
            if output_grid[i, min_col] == 0:
                output_grid[i, min_col] = 3
            else:
                break

        # Draw vertical line up from bottom-right 8
        for i in range(max_row - 1, -1, -1):
            if output_grid[i, max_col] == 0:
                output_grid[i, max_col] = 3
            else:
                break

    elif (min_row, max_col) in pos_with_8 and (max_row, min_col) in pos_with_8:
        # Case 2: 8s are positioned along anti-diagonal (top-right to bottom-left)

        # Draw diagonal line from top-right 8 downward and leftward
        for i in range(1, max(nrows, ncols)):
            r, c = min_row + i, max_col - i
            if 0 <= r <= max_row and 0 <= c < ncols:
                output_grid[r, c] = 3
            else:
                break

        # Draw diagonal line from bottom-left 8 upward and rightward
        for i in range(1, max(nrows, ncols)):
            r, c = max_row - i, min_col + i
            if min_row <= r < nrows and 0 <= c < ncols:
                output_grid[r, c] = 3
            else:
                break

        # Draw horizontal line right from bottom-left 8
        for i in range(min_col + 1, ncols):
            if output_grid[max_row, i] == 0:
                output_grid[max_row, i] = 3
            else:
                break

        # Draw horizontal line left from top-right 8
        for i in range(max_col - 1, -1, -1):
            if output_grid[min_row, i] == 0:
                output_grid[min_row, i] = 3
            else:
                break

    return output_grid


def solve_cd3c21df(input_grid):
    """
    Identifies and returns the unique connected component from the input grid.

    Concepts:
    - Connected component analysis
    - Pattern uniqueness detection
    - Shape extraction

    Transformation Steps:
    1. Find non-zero positions and group them into connected components
    2. Extract each component as a rectangular block
    3. Return the block with a unique pattern
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Convert to numpy array
    input_grid = np.array(input_grid)

    # Group non-zero positions into connected components
    groups = group_connected_positions(np.argwhere(input_grid != 0))

    # Extract blocks and their flattened representations
    blocks = []
    patterns = []

    for group in groups:
        # Get bounding box coordinates
        min_r, min_c = np.min(group, axis=0)
        max_r, max_c = np.max(group, axis=0)

        # Extract the block
        block = input_grid[min_r : max_r + 1, min_c : max_c + 1]
        blocks.append(block)
        patterns.append(tuple(block.flatten()))

    # Find the unique block
    output_grid = blocks[0]
    for i, pattern in enumerate(patterns):
        if pattern not in patterns[:i] + patterns[i + 1 :]:
            output_grid = blocks[i]

    return output_grid


def solve_20981f0e(input_grid):
    """
    Centers blocks of 1s within squares defined by corners marked with 2s.

    Concepts:
    - Grid pattern centering
    - Bounding box computation
    - Shape repositioning

    Transformation Steps:
    1. Identify squares defined by 2s at their corners
    2. Find a sub-block of 1s within each square
    3. Center these blocks within their respective squares
    """

    # Convert to numpy array
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find positions containing value 2 (corner markers)
    pos_with_2 = np.argwhere(input_grid == 2)
    rows_with_2 = np.sort(np.unique([r for r, c in pos_with_2]))
    cols_with_2 = np.sort(np.unique([c for r, c in pos_with_2]))
    size = rows_with_2[1] - rows_with_2[0] - 1

    # Process each square defined by corner markers
    for i in range(len(rows_with_2)):
        for j in range(len(cols_with_2)):
            # Define square boundaries
            row_start = rows_with_2[i] + 1
            row_end = rows_with_2[i] + 1 + size
            col_start = cols_with_2[j] + 1
            col_end = cols_with_2[j] + 1 + size

            # Extract the block within this square
            block = input_grid[row_start:row_end, col_start:col_end]
            H, W = block.shape

            # Find positions of 1s within the block
            pos_with_1 = np.argwhere(block == 1)

            if len(pos_with_1) > 0:
                # Get bounding box of the pattern of 1s
                min_r, min_c = pos_with_1.min(axis=0)
                max_r, max_c = pos_with_1.max(axis=0)

                # Extract the pattern of 1s
                sub_block = block[min_r : max_r + 1, min_c : max_c + 1]
                h, w = sub_block.shape

                # Calculate offsets for centering
                half_diff_h = (H - h) // 2
                half_diff_w = (W - w) // 2

                # Create new centered block
                new_block = np.zeros_like(block)
                new_block[half_diff_h : half_diff_h + h, half_diff_w : half_diff_w + w] = sub_block

                # Replace the block in the output grid with the centered block
                output_grid[row_start:row_end, col_start:col_end] = 0
                output_grid[row_start:row_end, col_start:col_end] = new_block

    return output_grid


def solve_d364b489(input_grid):
    """
    Completes colorful crosses/flowers (+) in the grid.

    Concepts:
    - Pattern recognition: Identifying centers of crosses
    - Pattern completion: Adding colored petals around centers
    - Spatial transformation: Creating a specific flower pattern

    Transformation Steps:
    1. Find all positions containing value 1 (centers of crosses)
    2. For each center position, create a flower pattern:
       - Keep center as 1
       - Set top petal to color 2
       - Set bottom petal to color 8
       - Set left petal to color 7
       - Set right petal to color 6
    """

    # Convert to numpy array
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find positions containing value 1 (center of cross)
    pos_with_1 = np.argwhere(input_grid == 1)

    # Complete colorful cross/flower of shape +
    for r, c in pos_with_1:
        # Keep center as it is 1
        output_grid[r, c] = 1

        # Add colored petals in four directions
        if r > 0:
            output_grid[r - 1, c] = 2  # Color 2 at top petal
        if r < nrows - 1:
            output_grid[r + 1, c] = 8  # Color 8 at bottom petal
        if c > 0:
            output_grid[r, c - 1] = 7  # Color 7 at left petal
        if c < ncols - 1:
            output_grid[r, c + 1] = 6  # Color 6 at right petal

    return output_grid


def solve_03560426(input_grid):
    """
    Stack colored blocks from bottom to the left edge, keeping the same order.

    Concepts:
    - Pattern extraction: Identifying connected regions (ractangular-blocks) of same color
    - Block arrangement: Stacking blocks with overlapping corners
    - Spatial reorganization: Placing blocks in a stair-like pattern

    Transformation Steps:
    1. Identify distinct colors from the bottom row of input grid
    2. For each color, extract its bounding box from the input grid
    3. Arrange these blocks starting from top-left, with each subsequent block
       overlapping at corners in a diagonal stair pattern
    """

    # Convert to numpy array
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Extract unique non-zero elements from bottom row (preserve order)
    non_zero_vals = []
    for c in range(ncols):
        val = input_grid[-1, c]
        if val != 0 and val not in non_zero_vals:
            non_zero_vals.append(val)

    # Starting position for the first block
    min_r, min_c = 0, 0

    # Place each block in sequence with overlapping corners
    for val in non_zero_vals:
        # Find all positions with the current value
        positions = np.argwhere(input_grid == val)

        # Determine bounding box
        min_row, min_col = positions.min(axis=0)
        max_row, max_col = positions.max(axis=0)

        # Extract the block
        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

        # Place block at current position
        height, width = block.shape
        output_grid[min_r : min_r + height, min_c : min_c + width] = block

        # Move to next position with overlapping corners
        # (bottom-right of current block connects to top-left of next block)
        min_r += height - 1
        min_c += width - 1

    return output_grid


def solve_ca8de6ea(input_grid):
    """
    Transform grid by extracting inner content and swapping corner and adjacent values.

    Concepts:
    - Grid transformation: Extracting inner region while preserving corners
    - Pattern manipulation: Moving values between specific positions
    - Corner preservation: Maintaining original corner values

    Transformation Steps:
    1. Extract the inner block of the grid (all but outer border)
    2. For each corner position, copy its value to the adjacent cross position
    3. Replace corner values with those from the original grid
    """

    # Convert to numpy array
    input_grid = np.array(input_grid)

    # Extract the center block (remove border)
    center_block = input_grid[1:-1, 1:-1]
    output_grid = center_block

    # Define relative positions of corners and adjacent cross positions
    corners = [(0, 0), (0, -1), (-1, 0), (-1, -1)]  # Top-left, top-right, bottom-left, bottom-right
    cross = [(0, 1), (1, 0), (1, -1), (-1, 1)]  # Right of TL, below TL, left of BR, above BR

    # For each pair of positions, copy corner values to cross positions
    # and restore original corner values
    for i in range(4):
        # Copy corner value to adjacent cross position
        output_grid[cross[i]] = output_grid[corners[i]]
        # Restore original corner value from input grid
        output_grid[corners[i]] = input_grid[corners[i]]

    return output_grid


def solve_e2092e0c(input_grid):
    """
    Finds pattern bounded by frame of 5s and/or grid boundaries
    draws a border of 5s around each matching pattern.

    Concepts:
    - Pattern detection: pattern bounded by frame of 5s and/or grid boundaries
    - Pattern matching: Finding occurrences of patterns within a grid
    - Border creation: Drawing borders around identified patterns

    Transformation Steps:
    1. Finds pattern bounded by frame of 5s and/or grid boundaries
        - Find all positions containing 5s
        - Group connected 5s together
        - Identify the largest group of connected 5s as the frame
        - Identify the pattern within this frame
    2. Search for all occurrences of this pattern in the grid
    3. Draw a border of 5s around each pattern occurrence
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    # Convert to numpy array
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find all positions with value 5
    pos_with_5 = np.argwhere(input_grid == 5)

    # Group connected positions with value 5
    groups = group_connected_positions(pos_with_5)

    # Find the largest connected group
    biggest_group = max(groups, key=len) if groups else []

    # Get the bounding box of the pattern
    min_row, max_row = min(p[0] for p in biggest_group), max(p[0] for p in biggest_group)
    min_col, max_col = min(p[1] for p in biggest_group), max(p[1] for p in biggest_group)

    # Extract the pattern
    pattern = input_grid[min_row:max_row, min_col:max_col]

    # Find all matching patterns in the grid
    height, width = pattern.shape
    for r in range(nrows - height + 1):
        for c in range(ncols - width + 1):
            subgrid = input_grid[r : r + height, c : c + width]

            # If pattern matches, draw a border of 5s around it
            if np.array_equal(subgrid, pattern):
                # Left and right borders
                output_grid[r - 1 : r + height + 1, c - 1] = 5
                output_grid[r - 1 : r + height + 1, c + width] = 5

                # Top and bottom borders
                output_grid[r - 1, c - 1 : c + width + 1] = 5
                output_grid[r + height, c - 1 : c + width + 1] = 5

    return output_grid


def solve_2013d3e2(input_grid):
    """
    Extract the top-left quadrant of the bounding box containing all non-zero values.

    Concepts:
    - Bounding box detection: Finding the minimal rectangle containing all non-zero elements
    - Region extraction: Retrieving specific portion (top-left quadrant) of identified region


    Transformation Steps:
    1. Find all non-zero positions in the input grid
    2. Determine the bounding box (min/max coordinates) of these positions
    3. Extract the full block defined by this bounding box
    4. Calculate half-dimensions of the extracted block
    5. Return only the top-left quadrant of the block
    """

    # Convert to numpy array
    input_grid = np.array(input_grid)

    # Find all positions with non-zero values
    pos_non_zero = np.argwhere(input_grid != 0)

    # Calculate bounding box coordinates
    min_row, min_col = pos_non_zero.min(axis=0)
    max_row, max_col = pos_non_zero.max(axis=0)

    # Extract the block containing all non-zero elements
    block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

    # Calculate half-dimensions for quadrant extraction
    half_h, half_w = block.shape[0] // 2, block.shape[1] // 2

    # Extract top-left quadrant
    output_grid = block[:half_h, :half_w]

    return output_grid


def solve_195ba7dc(input_grid):
    """
    Find a column containing all 2s and create a binary output grid based on merging
    the regions separated by this column.

    Concepts:
    - Column-based partitioning: Identifying a dividing column with value 2
    - Region merging: Combining data from separate regions of the grid
    - Binary transformation: Converting to 1s where either region had non-zero values

    Transformation Steps:
    1. Identify the column where all values equal 2 (partition column)
    2. Split the grid into left and right parts, excluding the partition column
    3. Add corresponding elements from both parts
    4. Create a binary output where any non-zero sum becomes 1
    """

    # Convert to numpy array
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Find partitioning column containing all 2s
    col_with_2 = None
    for c in range(ncols):
        if np.all(input_grid[:, c] == 2):
            col_with_2 = c
            break

    # Split grid into left and right parts around partition
    left_part = input_grid[:, :col_with_2]
    right_part = input_grid[:, col_with_2 + 1 :]

    # Combine regions and create binary output
    # (1 where either region had a value, 0 where both were 0)
    add = left_part + right_part
    output_grid = (add != 0).astype(int)

    return output_grid


def solve_fc754716(input_grid):
    """
    Find center color (value) in the input grid and create a frame around it of the same color.

    Concepts:
    - Center identification: Locating the center cell of a grid
    - Value extraction: Retrieving the color/value from the center position
    - Frame creation: Using the extracted value to create a border around the entire grid
    - Value replacement: Setting the center position to 0 (background)

    Transformation Steps:
    1. Extract the value from the center cell of the input grid
    2. Replace the center cell value with 0
    3. Create a frame/border around the entire grid using the center value
    """

    # Convert to numpy array
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Extract the center value
    central_val = input_grid[nrows // 2, ncols // 2]

    # Replace center value with 0
    output_grid[nrows // 2, ncols // 2] = 0

    # Create a frame around the grid using the central value
    output_grid[0, :] = central_val  # Top row
    output_grid[-1, :] = central_val  # Bottom row
    output_grid[:, 0] = central_val  # Left column
    output_grid[:, -1] = central_val  # Right column

    return output_grid


def solve_2dc579da(input_grid):
    """
    Extract the quadrant containing non-background colors from a grid divided into four blocks.

    Concepts:
    - Grid partitioning: Dividing the grid into four quadrants using (and excluding) central row and column
    - Mark detection: Identifying blocks that contain a non-background color
    - Extraction: Returning the first block that contains a non-background color

    Transformation Steps:
    1. Divide the input grid into four quadrants using the central row and column
    2. Analyze each quadrant to identify which contains multiple colors
    3. Return the first quadrant that contains more than one color value
    """

    # Convert to numpy array
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Extract the four quadrants separated by central row and central column
    top_left_block = input_grid[: nrows // 2, : ncols // 2]
    top_right_block = input_grid[: nrows // 2, ncols // 2 + 1 :]
    bottom_left_block = input_grid[nrows // 2 + 1 :, : ncols // 2]
    bottom_right_block = input_grid[nrows // 2 + 1 :, ncols // 2 + 1 :]

    # Collect all blocks for processing
    blocks = [top_left_block, top_right_block, bottom_left_block, bottom_right_block]

    # Find the first block that contains multiple (background and a non-background) colors
    for block in blocks:
        unique_values = np.unique(block)
        if len(unique_values) > 1:  # If block contains more than one color
            output_grid = block
            break

    return output_grid


def solve_ec883f72(input_grid):
    """
    Extend the interior color from the corners of the block of non-background values outward,
    along the diagonals, until reaching the grid boundary.

    Concepts:
    - Bounding box detection: Find the smallest rectangular block containing all non-background (nonzero) values (colors)
    - Corner identification: Locate corners of the bounding box that are not on the grid boundary.
    - Color extraction: Identify the frame and interior colors within the rectangular block.
    - Diagonal extension: Propagate the interior color outward from each non-boundary corner.

    Transformation Steps:
    1. Find the minimal bounding box of non-background (non-zero) cells.
    2. Identify corners of the bounding box that are not on the grid boundary.
    3. Determine the frame color and the unique interior color.
    4. For each non-boundary corner, extend the interior color outward along its diagonal until the grid boundary.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find bounding box of non-background (non-zero) colors
    pos_non_zeros = np.argwhere(input_grid != 0)
    min_row, min_col = pos_non_zeros.min(axis=0)
    max_row, max_col = pos_non_zeros.max(axis=0)
    block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

    # Identify corners of the bounding box
    box_corners = [(min_row, min_col), (min_row, max_col), (max_row, min_col), (max_row, max_col)]
    # Filter corners that are not on the grid boundary
    non_boundary_corners = [
        corner for corner in box_corners if 0 < corner[0] < nrows - 1 and 0 < corner[1] < ncols - 1
    ]

    # Extract frame and interior colors
    frame_value = input_grid[non_boundary_corners[0][0], non_boundary_corners[0][1]]
    unique_vals = set(np.unique(block))
    interior_val = (unique_vals - {0, frame_value}).pop()  # Expecting only one interior color

    # Extend interior color outward from each non-boundary corner
    for corner in non_boundary_corners:
        r, c = corner
        if corner == (min_row, min_col):
            direction = (-1, -1)
        elif corner == (min_row, max_col):
            direction = (-1, 1)
        elif corner == (max_row, min_col):
            direction = (1, -1)
        elif corner == (max_row, max_col):
            direction = (1, 1)
        for step in range(1, max(nrows, ncols)):
            rr, cc = r + direction[0] * step, c + direction[1] * step
            if rr < 0 or rr >= nrows or cc < 0 or cc >= ncols:
                break
            output_grid[rr, cc] = interior_val

    return output_grid


def solve_2281f1f4(input_grid):
    """
    Paint intersections of columns (in the first row) and rows (in the last column) containing color 5 with color 2.

    Concepts:
    - Value detection: Identify columns in the first row and rows in the last column containing a specific color (5).
    - Intersection marking: Paint the intersection cells of these columns and rows with a new color (2).

    Transformation Steps:
    1. Find all columns in the first row where the value is 5.
    2. Find all rows in the last column where the value is 5.
    3. For each intersection of these rows and columns, set the cell value to 2.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find columns in the first row with value 5
    cols_with_5 = np.where(input_grid[0] == 5)[0]
    # Find rows in the last column with value 5
    rows_with_5 = np.where(input_grid[:, -1] == 5)[0]

    # Paint intersections with color 2
    for r in rows_with_5:
        for c in cols_with_5:
            output_grid[r, c] = 2

    return output_grid


def solve_5587a8d0(input_grid):
    """
    Create concentric square frames of non-background colors from outer to inner,
    in the order of frequency of color in the input grid.

    Concepts:
    - Frequency analysis: Identify the most frequent color (background) and order other colors by frequency.
    - Frame drawing: Draw square frames for each non-background color, from outermost to innermost.
    - Grid resizing: Output grid size depends on the number of unique non-background colors.

    Transformation Steps:
    1. Identify the most frequent color in the input grid (background color).
    2. Determine the unique non-background colors and their frequencies.
    3. Create an output grid sized to fit all frames (size = 2 * num_non_background_colors - 1).
    4. Draw concentric square frames for each non-background color in descending order of frequency.
    """
    input_grid = np.array(input_grid)
    unique, count = np.unique(input_grid, return_counts=True)
    order = np.argsort(-count)  # indices that would sort counts descending
    background_val = unique[order[0]]  # most frequent value (background)

    num_non_back_vals = len(unique) - 1  # excluding background
    size = 2 * num_non_back_vals - 1
    output_grid = np.full((size, size), background_val)

    min_row, min_col = 0, 0
    max_row, max_col = size, size
    for o in order[1:]:
        val = unique[o]
        # Draw frame of color 'val'
        output_grid[min_row, min_col:max_col] = val
        output_grid[max_row - 1, min_col:max_col] = val
        output_grid[min_row:max_row, min_col] = val
        output_grid[min_row:max_row, max_col - 1] = val

        # Move one layer inward
        min_row += 1
        min_col += 1
        max_row -= 1
        max_col -= 1

    return output_grid


def solve_68b16354(input_grid):
    """
    Input output mirror vertically.

    Concepts: Flip the input grid vertically (upside down).


    Transformation Steps:
    1. Flip the input grid vertically using numpy's flipud function.
    """
    input_grid = np.array(input_grid)
    output_grid = np.flipud(input_grid)

    return output_grid


def solve_a78176bb(input_grid):
    """
    Draw lines parallel to a slanting (diagonal) line of non-background, non-5 values,
    extending in directions indicated by triangular clusters of 5s attached to the line.

    Concepts:
    - Connected component analysis: Group clusters of 5s.
    - Diagonal line extension: Draw lines parallel to the main diagonal based on cluster position.
    - Grid manipulation: Remove 5s and extend the main color.

    Transformation Steps:
    1. Identify the unique non-background, non-5 value (main line color).
    2. Find all positions of 5s and group them into connected components.
    3. Remove all 5s from the grid.
    4. For each cluster, determine its orientation and extend the main line color diagonally outward and
    downward until the grid boundary is reached.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find the unique non-0, non-5 value (main line color)
    non_0_5_val = np.unique(input_grid[(input_grid != 0) & (input_grid != 5)])[0]

    # Find all positions of 5s
    pos_with_5 = np.argwhere(input_grid == 5)
    output_grid[pos_with_5[:, 0], pos_with_5[:, 1]] = 0  # Remove 5s

    # Group connected positions of 5s
    parts = group_connected_positions(pos_with_5, connectivity=4)
    for part in parts:
        part = np.array(part)
        min_row, min_col = part.min(axis=0)
        max_row, max_col = part.max(axis=0)
        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

        # Bottom-left triangle: extend diagonals from just outside the block
        if np.all(block[:, 0] == 5) and np.all(block[-1] == 5):
            r, c = max_row + 1, min_col - 1
            for step in range(nrows * ncols):
                rr, cc = r - step, c - step
                if 0 <= rr < nrows and 0 <= cc < ncols:
                    output_grid[rr, cc] = non_0_5_val
                else:
                    break
            for step in range(nrows * ncols):
                rr, cc = r + step, c + step
                if 0 <= rr < nrows and 0 <= cc < ncols:
                    output_grid[rr, cc] = non_0_5_val
                else:
                    break

        # Top-right triangle: extend diagonals from just outside the block
        elif np.all(block[0] == 5) and np.all(block[:, -1] == 5):
            r, c = min_row - 1, max_col + 1
            for step in range(nrows * ncols):
                rr, cc = r - step, c - step
                if 0 <= rr < nrows and 0 <= cc < ncols:
                    output_grid[rr, cc] = non_0_5_val
                else:
                    break
            for step in range(nrows * ncols):
                rr, cc = r + step, c + step
                if 0 <= rr < nrows and 0 <= cc < ncols:
                    output_grid[rr, cc] = non_0_5_val
                else:
                    break

    return output_grid


def solve_ff2825db(input_grid):
    """
    Draws two frames using the most frequent nonzero value in the interior of the grid:
    - An inner frame around the bounding box of the most frequent value in the interior.
    - An outer frame (excluding the first row) using the same value.

    Concepts:
    - Frequency analysis in a subgrid
    - Bounding box detection
    - Frame drawing

    Transformation Steps:
    1. Extract the interior (excluding first two rows and first/last columns).
    2. Find the most frequent nonzero value in the interior.
    3. Find the bounding box of this value in the interior.
    4. Clear the interior region totally.
    5. Draw an inner frame around the bounding box using the detected value.
    6. Draw an outer frame (excluding the first row) using the same value.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Extract interior (excluding first two rows and first/last columns)
    interior = input_grid[2:-1, 1:-1]

    # Find most frequent nonzero value in the interior
    unique, count = np.unique(interior[interior != 0], return_counts=True)
    if len(unique) == 0:
        return output_grid  # No nonzero values to frame

    most_freq_val = unique[np.argmax(count)]

    # Find bounding box of the most frequent value
    pos_with_most_freq = np.argwhere(interior == most_freq_val)
    min_row, min_col = pos_with_most_freq.min(axis=0)
    max_row, max_col = pos_with_most_freq.max(axis=0)

    # Clear interior
    output_grid[2:-1, 1:-1] = 0

    # Draw inner frame
    row_offset, col_offset = 2, 1
    output_grid[min_row + row_offset, min_col + col_offset : max_col + col_offset + 1] = (
        most_freq_val
    )
    output_grid[max_row + row_offset, min_col + col_offset : max_col + col_offset + 1] = (
        most_freq_val
    )
    output_grid[min_row + row_offset : max_row + row_offset + 1, min_col + col_offset] = (
        most_freq_val
    )
    output_grid[min_row + row_offset : max_row + row_offset + 1, max_col + col_offset] = (
        most_freq_val
    )

    # Draw outer frame (excluding first row)
    output_grid[1] = most_freq_val
    output_grid[-1] = most_freq_val
    output_grid[1:-1, 0] = most_freq_val
    output_grid[1:-1, -1] = most_freq_val

    return output_grid


def solve_09c534e7(input_grid):
    """
    For each connected nonzero region, fill its interior (cells fully surrounded by nonzero values)
    with the least frequent nonzero color in that region.

    Concepts:
    - Connected component analysis
    - Interior detection via 8-neighborhood
    - Frequency analysis within a region

    Transformation Steps:
    1. Find all connected groups of nonzero cells.
    2. For each group, determine the least frequent nonzero color.
    3. Identify interior positions (not on border, all 8 neighbors nonzero).
    4. Fill interior positions with the chosen color.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find all connected groups of nonzero cells
    pos_non_zero = np.argwhere(input_grid != 0)
    groups = group_connected_positions(pos_non_zero)

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for group in groups:
        group = np.array(group)
        vals = input_grid[tuple(group.T)]
        non_zero_vals, counts = np.unique(vals[vals != 0], return_counts=True)
        if len(non_zero_vals) == 0:
            continue

        # Select the least frequent nonzero color as the interior color
        interior_color = non_zero_vals[np.argmin(counts)]

        # Identify interior positions
        interior_pos = []
        for r, c in group:
            # Skip border cells
            if r == 0 or r == nrows - 1 or c == 0 or c == ncols - 1:
                continue
            ngb = [
                input_grid[r + dr, c + dc]
                for dr, dc in neighbors
                if 0 <= r + dr < nrows and 0 <= c + dc < ncols
            ]
            # Check if all neighbors are nonzero, consider (r, c) as interior position
            if ngb and np.all(np.array(ngb) != 0):
                interior_pos.append((r, c))

        # Fill interior positions with the interior color
        for r, c in interior_pos:
            output_grid[r, c] = interior_color

    return output_grid


def solve_1a07d186(input_grid):
    """
    Concepts:
    - Pattern Detection: Identify rows or columns filled with a single nonzero value.
    - Neighborhood Analysis: Locate adjacent blocks with the same value.
    - Value Propagation: Extend the identified value to adjacent cells in the specified direction.

    Transformation Steps:
    1. Detect rows or columns filled with a single nonzero value in the input grid.
    2. Identify the specific rows or columns with their values that meet this criterion.
    3. Start with a blank output grid, place the identified rows/columns back.
    4. for each identified row/column:
    - find the same value in the blocks above/below (for rows) or left/right (for columns).
    - move that value to the adjacent cells in the direction of the filled row/column.
    5. Return the reconstructed and extended output grid.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros_like(input_grid)  # Start with a blank grid

    direction = None
    unique_vals = []
    positions = []

    # Check for rows with a single nonzero value
    for r in range(nrows):
        row = input_grid[r]
        unique = np.unique(row)  # Ignore background (0)
        if len(unique) == 1 and unique[0] != 0:
            direction = "along rows"
            unique_vals.append(unique[0])
            positions.append(r)

    # Check for columns with a single nonzero value
    for c in range(ncols):
        unique = np.unique(input_grid[:, c])
        if len(unique) == 1 and unique[0] != 0:
            direction = "along columns"
            unique_vals.append(unique[0])
            positions.append(c)

    # Reconstruct and extend rows or columns
    for val, pos in zip(unique_vals, positions):
        if direction == "along rows":
            output_grid[pos, :] = val  # Place the row with the value back

            # Extend above the row
            top_block = input_grid[:pos]
            place = np.argwhere(top_block == val)
            for p in place:
                output_grid[pos - 1, p[1]] = val

            # Extend below the row
            bottom_block = input_grid[pos + 1 :]
            place = np.argwhere(bottom_block == val)
            for p in place:
                output_grid[pos + 1, p[1]] = val

        elif direction == "along columns":
            output_grid[:, pos] = val  # Place the column with the value back

            # Extend to the left of the column
            left_block = input_grid[:, :pos]
            place = np.argwhere(left_block == val)
            for p in place:
                output_grid[p[0], pos - 1] = val

            # Extend to the right of the column
            right_block = input_grid[:, pos + 1 :]
            place = np.argwhere(right_block == val)
            for p in place:
                output_grid[p[0], pos + 1] = val

    return output_grid


def solve_32597951(input_grid):
    """
    Concepts:
    - Region extraction
    - Value replacement within a block

    Transformation Steps:
    1. Find all positions in the input grid with value 8.
    2. Extract the minimal bounding rectangle containing all 8s.
    3. Within this block, locate all positions with value 1.
    4. Replace each such position with value 3 in the output grid.
    5. Return the modified output grid.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    positions_with_8 = np.argwhere(input_grid == 8)
    if positions_with_8.size == 0:
        return output_grid

    # Get bounding box of all 8s
    min_row, min_col = positions_with_8.min(axis=0)
    max_row, max_col = positions_with_8.max(axis=0)
    block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

    # Replace 1s with 3s in the in the block of the output grid
    positions_with_1 = np.argwhere(block == 1)
    for r, c in positions_with_1:
        output_grid[min_row + r, min_col + c] = 3

    return output_grid


def solve_be94b721(input_grid):
    """
    Concepts:
    - Frequency analysis
    - Block extraction

    Transformation Steps:
    1. Identify the most frequent nonzero value in the input grid.
    2. Find all positions containing this value.
    3. Extract the minimal bounding block that contains all these positions.
    4. Return the extracted block as the output grid.
    """
    from arc_agi_2_atlas.providers.grid_utils import extract_min_bound_block

    input_grid = np.array(input_grid)

    # Find the most frequent nonzero value
    unique, counts = np.unique(input_grid[input_grid != 0], return_counts=True)
    most_frequent_value = unique[np.argmax(counts)]

    # Get positions of the most frequent value
    pos_most_frequent = np.argwhere(input_grid == most_frequent_value)

    # Extract minimal bounding block containing all positions
    output_grid = extract_min_bound_block(input_grid, pos_most_frequent)

    return output_grid


def solve_cf98881b(input_grid):
    """
    Concepts:
    - Grid partitioning
    - Block-wise merging

    Transformation Steps:
    1. Identify columns in the input grid that are entirely filled with the value 2
    2. Partition the grid into blocks using these columns as separators.
    3. Merge the blocks from left to right, preserving nonzero values from earlier blocks.
    4. Return the merged output grid.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Identify partitioning columns filled with 2s
    col_with_2s = [-1]
    blocks = []
    for c in range(ncols):
        if np.all(input_grid[:, c] == 2):
            blocks.append(input_grid[:, col_with_2s[-1] + 1 : c])
            col_with_2s.append(c)
    blocks.append(input_grid[:, col_with_2s[-1] + 1 :])

    # Merge blocks left to right only filling in empty (0) cells
    output_grid = blocks[0]
    for block in blocks[1:]:
        mask = output_grid != 0
        output_grid = output_grid * mask + block * (~mask)
    return output_grid


def solve_27a77e38(input_grid):
    """
    Place the most frequent value from the top block and put it in the center of the last row.

    Concepts:
    - Grid partitioning
    - Frequency analysis
    - Value placement

    Transformation Steps:
    1. Partition the input grid into top and bottom blocks using the middle row of 5s as a separator.
    2. Find the most frequent value in the top block.
    3. Place this value in the center cell of the last row of the output grid.
    4. Return the modified output grid.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Partition grid into top and bottom blocks using the middle row
    top_block = input_grid[: nrows // 2]
    bottom_block = input_grid[(nrows // 2) + 1 :]

    # Find the most frequent value in the top block
    unique, counts = np.unique(top_block, return_counts=True)
    most_frequent_value = unique[np.argmax(counts)]

    # Place the most frequent value in the center of the last row
    output_grid[-1, ncols // 2] = most_frequent_value

    return output_grid


def solve_6455b5f5(input_grid):
    """
    find the smallest empty compartments and fill them with 8s
    find the biggest empty compartments and fill them with 1s

    Concepts:
    - Connected component analysis
    - Region filling

    Transformation Steps:
    1. Find all empty compartments (regions of 0s) in the input grid.
    2. Identify the smallest and largest such compartments by size.
    3. Fill all cells in the smallest compartment(s) with 8.
    4. Fill all cells in the largest compartment(s) with 1.
    5. Return the modified grid.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find all positions with value 0
    pos_with_0 = np.argwhere(input_grid == 0)
    if len(pos_with_0) == 0:
        return output_grid

    # Group connected positions (empty compartments)
    groups = group_connected_positions(pos_with_0)
    sizes = np.array([len(g) for g in groups])
    smallest, biggest = sizes.min(), sizes.max()

    # Fill smallest compartments with 8
    for idx in np.where(sizes == smallest)[0]:
        group_smallest = np.array(groups[idx])
        output_grid[group_smallest[:, 0], group_smallest[:, 1]] = 8

    # Fill biggest compartments with 1
    for idx in np.where(sizes == biggest)[0]:
        group_biggest = np.array(groups[idx])
        output_grid[group_biggest[:, 0], group_biggest[:, 1]] = 1

    return output_grid


def solve_54d9e175(input_grid):
    """
    Transform the grid by filling framed 3x3 blocks:

    - Each block has 0s as the frame and a single nonzero value at its center.
    - Add 5 to the nonzero center value.
    - Fill the entire 3x3 block with this updated value.

    Concepts:
    - Block detection
    - Region filling

    Transformation Steps:
    1. Locate groups of connected 0s (frames).
    2. Extract the bounding box for each group (candidate 3x3 block).
    3. Identify the unique nonzero value inside the block.
    4. Add 5 to it and fill the entire block.
    5. Return the modified grid.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find connected groups of 0-valued positions (frames)
    zero_positions = np.argwhere(input_grid == 0)
    groups = group_connected_positions(zero_positions)

    for group in groups:
        group = np.array(group)
        min_row, min_col = np.min(group, axis=0)
        max_row, max_col = np.max(group, axis=0)

        # Extract candidate 3x3 block
        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]

        # Check for a single nonzero center value and fill the entire block with updated value
        non_zero_vals = np.unique(block[block != 0])
        if len(non_zero_vals) == 1:
            updated_val = non_zero_vals[0] + 5
            output_grid[min_row : max_row + 1, min_col : max_col + 1] = updated_val

    return output_grid


def solve_f28a3cbb(input_grid):
    """
    Gather identical values (color) to the top-left and bottom-right corners from adjacent quadrants.

    Concepts:
    - Grid partitioning
    - value gathering

    Transformation Steps:
    1. Identify the unique non-background value in the top-left and bottom-right 3x3 blocks.
    2. For the top-left 3x3 block:
       - Move any matching value from the adjacent top-right, bottom-left, and bottom-right quadrants to the border of the top-left block,
       replacing its original position with the background color.
    3. For the bottom-right 3x3 block:
       - Move any matching value from the adjacent top-right, bottom-left, and top-left quadrants to the border of the bottom-right block,
       replacing its original position with the background color.
    4. Return the transformed grid.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    unique, counts = np.unique(input_grid, return_counts=True)
    background_color = unique[np.argmax(counts)]

    # ====== process the top-left 3x3 block ======
    top_left_block = input_grid[:3, :3]
    val = np.unique(top_left_block)[0]  # expecting only one non-background value

    # find and move the value from its top-right adjacent quadrant to the border of the top-left block
    its_top_right_block = input_grid[:3, 3:]
    pos = np.argwhere(its_top_right_block == val)
    for p in pos:
        r, c = tuple(p)
        c += 3
        output_grid[r, c] = background_color
        output_grid[r, 3] = val
    # find and move the value from its bottom-left adjacent quadrant to the border of the top-left block
    its_bottom_left_block = input_grid[3:, :3]
    pos = np.argwhere(its_bottom_left_block == val)
    for p in pos:
        r, c = tuple(p)
        r += 3
        output_grid[r, c] = background_color
        output_grid[3, c] = val
    # find and move the value from its bottom-right adjacent quadrant to the border of the top-left block
    its_bottom_right_block = input_grid[3:, 3:]
    pos = np.argwhere(its_bottom_right_block == val)
    for p in pos:
        r, c = tuple(p)
        r += 3
        c += 3
        output_grid[r, c] = background_color
        output_grid[2, 3] = val

    # ======= process the bottom-right 3x3 block ======
    bottom_right_block = input_grid[-3:, -3:]
    val = np.unique(bottom_right_block)[0]  # expecting only one non-background value

    # find and move the value from its top-right adjacent quadrant to the border of the bottom-right block
    its_top_right_block = input_grid[:-3, -3:]
    pos = np.argwhere(its_top_right_block == val)
    for p in pos:
        r, c = tuple(p)
        c += ncols - 3
        output_grid[r, c] = background_color
        output_grid[-4, c] = val
    # find and move the value from its bottom-left adjacent quadrant to the border of the bottom-right block
    its_bottom_left_block = input_grid[-3:, :-3]
    pos = np.argwhere(its_bottom_left_block == val)
    for p in pos:
        r, c = tuple(p)
        r += nrows - 3
        output_grid[r, c] = background_color
        output_grid[r, -4] = val
    # find and move the value from its top-left adjacent quadrant to the border of the bottom-right block
    its_top_left_block = input_grid[:-3, :-3]
    pos = np.argwhere(its_top_left_block == val)
    for p in pos:
        r, c = tuple(p)
        output_grid[r, c] = background_color
        output_grid[-3, -4] = val

    return output_grid


def solve_7e02026e(input_grid):
    """
    Find and fill '+' shaped free spaces (all 0s) with 3s

    Concepts:
    - Pattern detection
    - Region filling

    Transformation Steps:
    1. Scan the grid for '+' shaped regions where all five cells are free (with 0s).
       The '+' shape consists of:
       - Center: (r+1, c+1)
       - Top: (r, c+1)
       - Bottom: (r+2, c+1)
       - Left: (r+1, c)
       - Right: (r+1, c+2)
    2. For each such region, fill the entire '+' shape with 3s.
    3. Return the modified grid.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find and fill '+' shaped free spaces (all 0s) with 3s
    for r in range(nrows - 2):
        for c in range(ncols - 2):
            if (
                input_grid[r, c + 1] == 0
                and input_grid[r + 1, c] == 0
                and input_grid[r + 1, c + 1] == 0
                and input_grid[r + 1, c + 2] == 0
                and input_grid[r + 2, c + 1] == 0
            ):
                output_grid[r, c + 1] = 3
                output_grid[r + 1, c] = 3
                output_grid[r + 1, c + 1] = 3
                output_grid[r + 1, c + 2] = 3
                output_grid[r + 2, c + 1] = 3

    return output_grid


def solve_363442ee(input_grid):
    """
    Extract a pattern from the left block (partitioned by a column of 5s) and place it in the right block at non-zero (1s) marked positions.

    Concepts:
    - Pattern extraction
    - Block partitioning
    - Pattern placement

    Transformation Steps:
    1. Identify the partitioning column where all values are 5.
    2. Extract the top-left block (size x size) as the pattern.
    3. Find non-zero positions (with value 1) in the right block.
    4. Place the pattern at each marked position in the right block, centered around the marker.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find the partitioning column (all 5s)
    size = None
    for c in range(ncols):
        if np.all(input_grid[:, c] == 5):
            size = c  # Expected to be 3
            break

    if size is None:
        raise ValueError("No partitioning column found.")

    # Extract pattern: top-left block
    pattern = input_grid[:size, :size]

    # Get right block
    right_block = input_grid[:, size + 1 :]
    marker_pos = np.argwhere(right_block != 0)

    for pos in marker_pos:
        r, c = tuple(pos)
        # Place pattern centered at (r, c) in the right block
        min_r = r - 1
        min_c = (
            c + size
        )  # Since right_block starts at column size+1, global min_c = c + (size + 1) - 1 = c + size
        output_grid[min_r : min_r + size, min_c : min_c + size] = pattern

    return output_grid


def solve_a680ac02(input_grid):
    """
    Identify connected groups of non-zero values, remove solid blocks,
    preserve hollow blocks, trim empty rows/columns, and stack the remaining blocks.

    Concept:
    - Connected non-zero regions are either solid (fully filled) or hollow (partially filled).
    - Solid blocks are removed; hollow blocks are extracted and stacked vertically or horizontally
      based on the grid's aspect ratio.

    Transformation Steps:
    1. Identify all connected groups of non-zero positions in the input grid.
    2. For each group, remove it if it forms a solid block (all cells non-zero).
    3. Trim the output grid by removing rows and columns that are entirely zero.
    4. Divide the trimmed grid into sections (assuming 4x4 blocks) and extract the bounding box of non-zero positions in each section.
    5. Stack the extracted blocks vertically if the grid is taller than wide, or horizontally otherwise.
    """

    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()

    # Find all non-zero positions and group them into connected components
    non_zero_positions = np.argwhere(input_grid != 0)
    connected_groups = group_connected_positions(non_zero_positions)

    # Remove solid blocks from output
    for group in connected_groups:
        group = np.array(group)
        min_row, min_col = group.min(axis=0)
        max_row, max_col = group.max(axis=0)
        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]
        if np.all(block != 0):
            output_grid[min_row : max_row + 1, min_col : max_col + 1] = 0

    # Trim rows and columns that are entirely zero
    non_zero_rows = np.any(output_grid != 0, axis=1)
    non_zero_cols = np.any(output_grid != 0, axis=0)
    output_grid = output_grid[non_zero_rows][:, non_zero_cols]

    # Stack hollow blocks
    H, W = output_grid.shape
    block_size = 4
    extracted_blocks = []

    if H >= W:
        # Vertical stacking
        for r in range(0, H, block_size):
            section = output_grid[r : r + block_size, :]
            section_positions = np.argwhere(section != 0)
            if len(section_positions) > 0:
                min_r, min_c = section_positions.min(axis=0)
                max_r, max_c = section_positions.max(axis=0)
                block = section[min_r : max_r + 1, min_c : max_c + 1]
                extracted_blocks.append(block)
        if extracted_blocks:
            output_grid = np.vstack(extracted_blocks)
    else:
        # Horizontal stacking
        for c in range(0, W, block_size):
            section = output_grid[:, c : c + block_size]
            section_positions = np.argwhere(section != 0)
            if len(section_positions) > 0:
                min_r, min_c = section_positions.min(axis=0)
                max_r, max_c = section_positions.max(axis=0)
                block = section[min_r : max_r + 1, min_c : max_c + 1]
                extracted_blocks.append(block)
        if extracted_blocks:
            output_grid = np.hstack(extracted_blocks)

    return output_grid


def solve_91714a58(input_grid):
    """
    Identifies the largest connected component of non-zero cells across all values,
    and returns only the largest solid rectangle (no zeros) within that component.

    Concept:
    - Connected components are groups of adjacent non-zero cells (4-connectivity).
    - The largest component (by size) is selected, preserving its original values.
    - Within the bounding box of this component, "make rows and columns that carry extra non-zero cells zeros" to isolate the largest solid rectangle.

    Transformation Steps:
    1. Find all unique non-zero values in the input grid.
    2. For each value, identify connected components and track the largest one overall.
    3. Copy the largest connected component to the output grid with its original values.
    4. Compute the bounding box of the component.
    5. Within the bounding box, trim it to the largest solid rectangle by removing non-zero cells
    6. Return the modified output grid.
    """

    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Get unique non-zero values
    unique_values = np.unique(input_grid[input_grid != 0])

    # Find the largest connected component across all values
    max_size = 0
    largest_group = None
    component_value = None
    for val in unique_values:
        mask = input_grid == val
        positions = np.argwhere(mask)
        connected_groups = group_connected_positions(positions, connectivity=4)
        for group in connected_groups:
            if len(group) > max_size:
                max_size = len(group)
                largest_group = group
                component_value = val

    # If a largest group exists, process it
    if largest_group is not None:
        largest_group = np.array(largest_group)
        # Copy the component to output with original values
        output_grid[largest_group[:, 0], largest_group[:, 1]] = input_grid[
            largest_group[:, 0], largest_group[:, 1]
        ]

        # Compute bounding box
        min_row, min_col = np.min(largest_group, axis=0)
        max_row, max_col = np.max(largest_group, axis=0)

        # Extract the block within the bounding box
        block = output_grid[min_row : max_row + 1, min_col : max_col + 1]

        # Find positions with zeros in the block
        zero_positions = np.argwhere(block == 0)

        # Trim the block to make it the largest solid rectangle
        if len(zero_positions) > 0:
            unique_rows = np.unique(zero_positions[:, 0])
            unique_cols = np.unique(zero_positions[:, 1])

            # If only one row has zeros, make it all 0s in that row
            if len(unique_rows) == 1:
                block[unique_rows[0], :] = 0

            # If only one column has zeros, make it all 0s that column
            if len(unique_cols) == 1:
                block[:, unique_cols[0]] = 0

        # Update the output grid with the trimmed block
        output_grid[min_row : max_row + 1, min_col : max_col + 1] = block

    return output_grid


def solve_a1570a43(input_grid):
    """
    Detects a frame marked with value 3 at four corners and an object marked with value 2,
    then moves the object to the center of the frame while preserving the frame.

    Concept:
    - The frame is a rectangular marked with 3s at its four corners.
    - The object is a set of color 2s that need to be centered within the frame.
    - Centering is achieved by calculating the center of the frame and the object,
      then shifting the object accordingly.

    Transformation Steps:
    1. Identify positions of the frame (value 3) and compute its bounding box and center.
    2. Identify positions of the object (value 2) and compute its center.
    3. Calculate the shift needed to move the object's center to the frame's center.
    4. Place the frame in the output grid.
    5. Shift and place the object in the output grid, ensuring positions stay within bounds.
    """

    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Find positions of the frame (color 3)
    pos_with_3 = np.argwhere(input_grid == 3)
    if len(pos_with_3) == 0:
        return output_grid  # No frame, return empty grid

    min_row3, min_col3 = pos_with_3.min(axis=0)
    max_row3, max_col3 = pos_with_3.max(axis=0)
    cen_row3, cen_col3 = (min_row3 + max_row3) // 2, (min_col3 + max_col3) // 2

    # Place the frame in the output grid
    output_grid[pos_with_3[:, 0], pos_with_3[:, 1]] = 3

    # Find positions of the object (color 2)
    pos_with_2 = np.argwhere(input_grid == 2)
    if len(pos_with_2) == 0:
        return output_grid  # No object, return frame only

    min_row2, min_col2 = pos_with_2.min(axis=0)
    max_row2, max_col2 = pos_with_2.max(axis=0)
    cen_row2, cen_col2 = (min_row2 + max_row2) // 2, (min_col2 + max_col2) // 2

    # Calculate shift to center the object within the frame
    shift_row = cen_row3 - cen_row2
    shift_col = cen_col3 - cen_col2

    # Place the shifted object in the output grid, with bounds checking
    for r, c in pos_with_2:
        new_r = r + shift_row
        new_c = c + shift_col
        if 0 <= new_r < input_grid.shape[0] and 0 <= new_c < input_grid.shape[1]:
            output_grid[new_r, new_c] = 2

    return output_grid


def solve_db615bd4(input_grid):
    """
    Identifies a frame in the grid, extracts colored blocks outside the frame,
    solidifies them (makes all cells the same color), and arranges them inside
    the frame in the order they appear, either vertically or horizontally based
    on the frame's aspect ratio.

    Concept:
    - The grid contains a frame (most frequent color after backgrounds), blocks
      of other colors outside the frame, and backgrounds.
    - Blocks are solidified to their dominant color and placed inside the frame
      in a stacked arrangement, preserving their order of appearance.

    Transformation Steps:
    1. Identify background colors (most and second most frequent) and frame color (third most frequent).
    2. Locate the frame's bounding box and complete it in the output grid.
    3. Clear the inside of the frame.
    4. Collect blocks outside the frame, solidify them, and remove them from the input.
    5. Stack the blocks vertically or horizontally (based on frame height > width) with separators.
    6. Center the stacked arrangement inside the frame.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Identify colors by frequency
    unique, counts = np.unique(input_grid, return_counts=True)
    count_sort = np.argsort(-counts)
    background_color1 = unique[count_sort[0]]
    background_color2 = unique[count_sort[1]]
    frame_color = unique[count_sort[2]]  # Frame color

    # Find frame positions and bounding box
    pos_frame = np.argwhere(input_grid == frame_color)
    if len(pos_frame) == 0:
        return output_grid  # No frame, return copy
    min_row, min_col = pos_frame.min(axis=0)
    max_row, max_col = pos_frame.max(axis=0)
    H, W = max_row - min_row + 1, max_col - min_col + 1

    # Complete (Solidify) the frame in the output grid
    output_grid[min_row : max_row + 1, min_col] = frame_color
    output_grid[min_row : max_row + 1, max_col] = frame_color
    output_grid[min_row, min_col : max_col + 1] = frame_color
    output_grid[max_row, min_col : max_col + 1] = frame_color

    # Clear the inside of the frame
    output_grid[min_row + 1 : max_row, min_col + 1 : max_col] = background_color1

    # Collect blocks outside the frame
    val_in_order = []
    if H > W:
        # Vertical stacking: scan rows
        for r in range(nrows):
            row_unique = np.unique(input_grid[r])
            for v in row_unique:
                if (
                    v not in (background_color1, background_color2, frame_color)
                    and v not in val_in_order
                ):
                    val_in_order.append(v)
    else:
        # Horizontal stacking: scan columns
        for c in range(ncols):
            col_unique = np.unique(input_grid[:, c])
            for v in col_unique:
                if (
                    v not in (background_color1, background_color2, frame_color)
                    and v not in val_in_order
                ):
                    val_in_order.append(v)

    blocks = []
    for v in val_in_order:
        pos_v = np.argwhere(input_grid == v)
        if len(pos_v) == 0:
            continue
        min_r, min_c = pos_v.min(axis=0)
        max_r, max_c = pos_v.max(axis=0)
        block = np.full((max_r - min_r + 1, max_c - min_c + 1), v)  # Solidify block
        blocks.append(block)
        # Remove block from output_grid (set to background)
        output_grid[pos_v[:, 0], pos_v[:, 1]] = background_color1

    if not blocks:
        return output_grid  # No blocks to place

    # Stack the blocks
    if H > W:
        # Vertically stack with separators
        separator = np.full((1, blocks[0].shape[1]), background_color1)
        stack = separator.copy()
        for block in blocks:
            stack = np.vstack([stack, block, separator])
    else:
        # Horizontally stack with separators
        separator = np.full((blocks[0].shape[0], 1), background_color1)
        stack = separator.copy()
        for block in blocks:
            stack = np.hstack([stack, block, separator])

    # Center the stack in the frame
    stack_height, stack_width = stack.shape
    frame_center_row = min_row + H // 2
    frame_center_col = min_col + W // 2
    stack_center_row = stack_height // 2
    stack_center_col = stack_width // 2
    y_offset = frame_center_row - stack_center_row
    x_offset = frame_center_col - stack_center_col

    # Ensure offsets keep stack within frame bounds
    y_offset = max(min_row + 1, min(y_offset, max_row - stack_height))
    x_offset = max(min_col + 1, min(x_offset, max_col - stack_width))

    # Place the stack
    output_grid[y_offset : y_offset + stack_height, x_offset : x_offset + stack_width] = stack

    return output_grid


def solve_8abad3cf(input_grid):
    """
    Arranges non-background colors as squares in a horizontal row, sized by the square root of their frequency,
    with background separators, and flips the result vertically to match the expected orientation (so that they touch the bottom).

    Concept:
    - The grid contains a background color (most frequent) and other colors representing elements.
    - Each non-background color is represented as a square block, where the side length is the integer square root of its count.
    - Blocks are placed side by side with background separators, and the entire arrangement is flipped upside down.

    Transformation Steps:
    1. Identify unique colors and their frequencies in the input grid.
    2. Sort colors by frequency in ascending order.
    3. Determine the background color as the most frequent.
    4. For each non-background color, compute its block size as the integer square root of its count.
    5. Create a new grid with height equal to the largest block size and width as the sum of block sizes plus separators.
    6. Place each block in the grid with background spacing between them.
    7. Flip the grid vertically to achieve the final orientation (so that they touch the bottom).
    """

    input_grid = np.array(input_grid)

    # Get unique colors and their counts
    unique, counts = np.unique(input_grid, return_counts=True)
    order = np.argsort(counts)  # Sort by frequency ascending

    # Background is the most frequent color
    background_color = unique[order[-1]]

    # Non-background colors and their sizes
    colors = unique[order[:-1]]
    sizes = np.sqrt(counts[order[:-1]]).astype(int)

    if len(colors) == 0:
        return input_grid  # No non-background colors, return input

    # Compute output grid dimensions
    H = sizes[-1]  # Height is the largest size
    W = np.sum(sizes) + len(sizes) - 1  # Width includes spacing
    output_grid = np.full((H, W), background_color, dtype=int)

    # Place each color's block
    start_col = 0
    for i, (color, size) in enumerate(zip(colors, sizes)):
        if size > 0:
            output_grid[:size, start_col : start_col + size] = color
        start_col += size + 1  # Move to next position with spacing

    # Flip vertically to match expected output
    output_grid = np.flipud(output_grid)

    return output_grid


def solve_337b420f(input_grid):
    """
    Concept:
        The function extracts the largest connected group of non-background cells from each block of the input grid,
        where blocks are separated by columns of all zeros.
        It then places these groups into a compact output grid, shifting left if needed to avoid overlap.

    Transformation Steps:
        1. Identify columns in the input grid that are entirely zeros to use as block separators.
        2. Set the output grid size based on the first partitioning column.
        3. For each block between partitioning columns:
            a. Find all non-background cell positions.
            b. Group these positions by 4-connectivity.
            c. Select the largest group.
            d. Place the group in the output grid at its original positions if free space (with background color 8) is available;
            otherwise, shift left by one column and place.
        4. Return the resulting compact output grid.
    """

    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Get unique colors and their counts
    unique, counts = np.unique(input_grid, return_counts=True)
    background_color = unique[np.argmax(counts)]

    # Find columns that are all zeros (partitioning columns)
    partitioning_cols = []
    for c in range(ncols):
        if np.all(input_grid[:, c] == 0):
            partitioning_cols.append(c)

    # Set output grid size based on first partitioning column
    H = W = partitioning_cols[0]
    output_grid = np.full((H, W), background_color, dtype=int)

    # Add boundaries for block extraction
    partitioning_cols = [-1] + partitioning_cols + [ncols]

    # Process each block
    for i in range(len(partitioning_cols) - 1):
        block = input_grid[:, partitioning_cols[i] + 1 : partitioning_cols[i + 1]]
        pos = np.argwhere(block != background_color)
        if len(pos) == 0:
            continue
        groups = group_connected_positions(pos, connectivity=4)
        val = block[tuple(pos[0])]

        # Find the largest group
        marked_group = None
        size = 0
        for group in groups:
            if len(group) > size:
                size = len(group)
                marked_group = group
        marked_group = np.array(marked_group)

        # Place the group in the output grid, shift left if needed
        if np.all(output_grid[marked_group[:, 0], marked_group[:, 1]] == background_color):
            output_grid[marked_group[:, 0], marked_group[:, 1]] = val
        else:
            output_grid[marked_group[:, 0], marked_group[:, 1] - 1] = val

    return output_grid


def solve_dce56571(input_grid):
    """
    Count non-background cells in the input grid and draw a centered horizontal line of that color and size in the middle row of the output grid
    initialized with the background color.

    Concept:
    - frequency (number of occurrences) analysis
    - count non-background cells
    - draw centered horizontal line of that color and size in middle row

    Transformation Steps:
        1. Identify the background color and the non-background color.
        2. Count the number of non-background colored cells.
        3. Create the output grid with the background color.
        4. Create a horizontal line of the non-background color in the middle row.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Find unique colors and their counts
    unique, counts = np.unique(input_grid, return_counts=True)
    order = np.argsort(-counts)
    background = unique[order[0]]

    # Initialize output grid with background color
    output_grid = np.full((nrows, ncols), background)

    # Assuming only one non-background color (most frequent after background)
    num_non_bg = counts[order[1]]
    non_bg_val = unique[order[1]]

    # Calculate starting column for centering the line
    start = (ncols - num_non_bg) // 2

    # Place the horizontal line in the middle row
    output_grid[nrows // 2, start : start + num_non_bg] = non_bg_val

    return output_grid


def solve_ac605cbb(input_grid):
    """
    Concept:
    - color (value) based grid transformation (drawing lines)
    - analysing intersections of newly drawn lines and drawing diagonals from there

    Transformation Steps:
        1. Identify non-background colors (assuming background is 0).
        2. For each non-background color, locate its position and draw line patterns with color 5 according to the color value.
        3. If the two 5 line intesect, means: For each cell with color 5 that has non-zero neighbors in all four directions (up, down, left, right),
        then draw a diagonal line of color 4 extending to the grid edge.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Find non-background colors (assuming background is 0)
    non_zero_vals = np.unique(input_grid[input_grid != 0])

    # For each non-background value, draw lines in specific directions using color 5
    for val in non_zero_vals:
        r, c = tuple(np.argwhere(input_grid == val)[0])  # Expectation: only one occurrence
        if val == 1:
            output_grid[r, c + 1 : c + 3] = 5
            output_grid[r - 1, c + 2] = val
        elif val == 2:
            output_grid[r, c - 3 : c] = 5
            output_grid[r, c - 4] = val
        elif val == 3:
            output_grid[r + 1 : r + 3, c] = 5
            output_grid[r + 3, c] = val
        elif val == 6:
            output_grid[r - 5 : r, c] = 5
            output_grid[r - 6, c] = val

    # Find positions with color 5 to deal with the case of intersections
    pos_with_5 = np.argwhere(output_grid == 5)
    for p in pos_with_5:
        r, c = tuple(p)
        # If the two newly drawn 5 line intersect, means: If 5 surrounded by non-zero values in all four directions, draw diagonal line of color 4
        if (
            output_grid[r, c - 1] != 0
            and output_grid[r, c + 1] != 0
            and output_grid[r - 1, c] != 0
            and output_grid[r + 1, c] != 0
        ):
            for s in range(max(nrows, ncols)):
                rr, cc = r + s, c - s
                if 0 <= rr < nrows and 0 <= cc < ncols:
                    output_grid[rr, cc] = 4
                else:
                    break

    return output_grid


def solve_a87f7484(input_grid):
    """
    Block with unique black and white pattern out.

    Concept:
    - Dividing the grid into blocks and
    - Identifying unique black and white pattern
    - odd one out

    Transformation Steps:
        1. Determine grid orientation and divide into 3x3 blocks.
        2. Create binary masks (black and white pattern) for non-zero elements in each block.
        3. Count occurrences of each mask across blocks.
        4. Select the block with the mask that appears exactly once, indicating a unique pattern.
        5. Return the corresponding block as the output grid.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    blocks = []
    masks = []
    if nrows > ncols:  # Divide input grid into 3x3 vertical blocks
        for r in range(0, nrows, 3):
            block = input_grid[r : r + 3, :]
            mask = block != 0
            masks.append(mask)
            blocks.append(block)
    else:  # Divide input grid into 3x3 horizontal blocks
        for c in range(0, ncols, 3):
            block = input_grid[:, c : c + 3]
            mask = block != 0
            masks.append(mask)
            blocks.append(block)

    # Count occurrences of each mask
    from collections import defaultdict

    mask_counts = defaultdict(int)
    for mask in masks:
        mask_tuple = tuple(map(tuple, mask))  # Convert to hashable tuple
        mask_counts[mask_tuple] += 1

    # Find the mask that appears exactly once: unique pattern
    unique_mask = None
    for mask_tuple, count in mask_counts.items():
        if count == 1:
            unique_mask = mask_tuple
            break

    # Get the corresponding block
    if unique_mask is not None:
        for i, mask in enumerate(masks):
            if tuple(map(tuple, mask)) == unique_mask:
                output_grid = blocks[i]
                break

    return output_grid


def solve_5b6cbef5(input_grid):
    """
    Create a larger grid by tiling the input grid based on non-zero cells. (similar to Koch curve)

    Concept:
    - non-zero cell analysis
    - tiling with input grid

    Transformation Steps:
        1. Initialize a large output grid of size (nrows**2, ncols**2).
        2. For each non-zero cell in the input grid, copy the entire input grid into the corresponding tile in the output grid.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros((nrows**2, ncols**2), dtype=int)

    for r in range(nrows):
        for c in range(ncols):
            if input_grid[r, c] != 0:
                output_grid[r * nrows : (r + 1) * nrows, c * ncols : (c + 1) * ncols] = input_grid

    return output_grid


def solve_c4d1a9ae(input_grid):
    """
    Identify vertical blocks separated by background columns.
    For each block, fill its background cells with the unique color from the next block (cyclically).

    Concept:
    - block partitioning
    - changing background color in each block to the non-background color of the next block (establishing a cyclic relationship between blocks).

    Transformation Steps:
        1. Detect background color (most frequent value).
        2. Find columns that are entirely background (partition columns).
        3. Split the grid into blocks between partition columns.
        4. For each block, fill its background cells with the unique color from the next block.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Step 1: Find background color
    unique, counts = np.unique(input_grid, return_counts=True)
    background_color = unique[np.argmax(counts)]

    # Step 2: Find partition columns (columns with background color only)
    partitioning_cols = (
        [-1] + [c for c in range(ncols) if np.all(input_grid[:, c] == background_color)] + [ncols]
    )

    # Step 3: Find unique non-background value for each block
    non_bg_vals = []
    for i in range(len(partitioning_cols) - 1):
        c_start = partitioning_cols[i] + 1
        c_end = partitioning_cols[i + 1]
        block = input_grid[:, c_start:c_end]
        vals = np.unique(block[block != background_color])
        # Defensive: If block is empty, skip (should not happen in valid ARC tasks)
        non_bg_vals.append(vals[0] if len(vals) > 0 else background_color)

    # Step 4: Fill background cells in each block with next block's unique color
    for i in range(len(partitioning_cols) - 1):
        c_start = partitioning_cols[i] + 1
        c_end = partitioning_cols[i + 1]
        block = input_grid[:, c_start:c_end]
        v = non_bg_vals[(i + 1) % len(non_bg_vals)]
        new_block = block.copy()
        new_block[block == background_color] = v
        output_grid[:, c_start:c_end] = new_block

    return output_grid


def solve_470c91de(input_grid):
    """
    Move colored blocks diagonally based on the position of the marker (color 8).

    Concept:
        - Extract colored blocks from the input grid.
        - Detect marker positions (color 8) at a block's corner.
        - Move the entire block one step diagonally in the direction of the marker.

    Transformation Steps:
        1. Identify the background value (most frequent in the grid).
        2. For each unique value (excluding background and marker 8):
            a. Find the minimal bounding block carrying the value (color).
            b. In the block, find the marker (color 8) position.
            c. Move the block one step diagonally based on the marker's position and remove the marker.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    # Step 1: Find background value
    unique, counts = np.unique(input_grid, return_counts=True)
    background_value = unique[np.argmax(counts)]
    output_grid = np.full((nrows, ncols), background_value, dtype=input_grid.dtype)

    marker_color = 8

    # Step 2: Select values to process (exclude background and marker)
    selected_vals = unique[(unique != background_value) & (unique != marker_color)]

    for val in selected_vals:
        pos_value = np.argwhere(input_grid == val)
        min_row, min_col = pos_value.min(axis=0)
        max_row, max_col = pos_value.max(axis=0)

        block = input_grid[min_row : max_row + 1, min_col : max_col + 1]
        H, W = block.shape
        block_unique, block_counts = np.unique(block, return_counts=True)
        most_frequent_value = block_unique[np.argmax(block_counts)]

        # Find marker position (expects only one marker per block)
        marker_positions = np.argwhere(block == marker_color)
        if marker_positions.size == 0:
            continue  # No marker found, skip
        pos_marker = tuple(marker_positions[0])

        # Move block diagonally in the direction of the marker and remove the marker
        if pos_marker == (0, 0):  # top-left
            r0, r1 = max(min_row - 1, 0), max_row
            c0, c1 = max(min_col - 1, 0), max_col
            output_grid[r0:r1, c0:c1] = most_frequent_value
        elif pos_marker == (0, W - 1):  # top-right
            r0, r1 = max(min_row - 1, 0), max_row
            c0, c1 = min_col + 1, min(max_col + 2, ncols)
            output_grid[r0:r1, c0:c1] = most_frequent_value
        elif pos_marker == (H - 1, 0):  # bottom-left
            r0, r1 = min_row + 1, min(max_row + 2, nrows)
            c0, c1 = max(min_col - 1, 0), max_col
            output_grid[r0:r1, c0:c1] = most_frequent_value
        elif pos_marker == (H - 1, W - 1):  # bottom-right
            r0, r1 = min_row + 1, min(max_row + 2, nrows)
            c0, c1 = min_col + 1, min(max_col + 2, ncols)
            output_grid[r0:r1, c0:c1] = most_frequent_value

    return output_grid


def solve_a5f85a15(input_grid):
    """
    For each non-background diagonal line, set every second cell (odd index) to color 4.

    Concept:
        - Identify all non-background connected groups (expected to be diagonal lines).
        - For each group, set every second cell (odd index) to color 4.

    Transformation Steps:
        1. Identify the background color (most frequent value).
        2. Find all non-background connected groups.
        3. For each group, sort by row and column, then set every odd-indexed cell to color 4.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    unique, counts = np.unique(input_grid, return_counts=True)
    background_color = unique[np.argmax(counts)]  # usually 0

    pos_non_bg = np.argwhere(input_grid != background_color)
    groups = group_connected_positions(pos_non_bg)

    for group in groups:
        group = np.array(group)
        # Sort by row, then by column for consistent diagonal order
        order = np.lexsort((group[:, 1], group[:, 0]))
        group = group[order]
        for i, (r, c) in enumerate(group):
            if i % 2 == 1:
                output_grid[r, c] = 4  # set to color 4

    # ============== Alternative implementation ==============
    # min_r, min_c = group.min(axis=0)
    # start from the top-left position, change the color to 4 at alternative diagonal positions until reach a grid boundary
    # for step in range(1, max(nrows, ncols), 2):
    #     r, c = min_r + step, min_c + step
    #     if 0 <= r < nrows and 0 <= c < ncols:
    #         output_grid[r, c] = 4 # change the color to 4
    #     else:
    #         break

    return output_grid


def solve_17b80ad2(input_grid):
    """
    Fills columns upward from bottom markers (color 5), changing color when a non-zero cell is encountered.

    Concept:
        - Markers are given in the bottom row with color 5.
        - For each marker column, fill upwards with the current color.
        - When a non-zero color is encountered, update the fill color to that value.

    Transformation Steps:
        1. For each column, if the bottom cell is a marker (5), fill upwards.
        2. At each step, if the input cell is zero, fill with the current color.
        3. If a non-zero cell is encountered, update the current color to that value and continue.
    """
    import numpy as np

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    # Set the marker color 5
    marker_color = 5

    for c in range(ncols):
        if output_grid[nrows - 1, c] == marker_color:
            # initialize color to marker color
            color = marker_color
            for r in range(nrows - 1, -1, -1):
                if (
                    input_grid[r, c] == 0
                ):  # if cell is empty (with background color 0), fill with current color
                    output_grid[r, c] = color
                else:  # update color to the encountered non-zero color
                    color = input_grid[r, c]

    return output_grid


def solve_95990924(input_grid):
    """
    Detects 2x2 squares of color 5 and paints their corners:
    - 1: top-left
    - 2: top-right
    - 3: bottom-left
    - 4: bottom-right

    Concept:
        - For each connected 2x2 (or larger) block of color 5, color the four corners if they are background.

    Transformation Steps:
        1. Identify background and square color.
        2. Find all connected groups of the square color.
        3. For each group, determine its bounding box and paint corners if background.
    """
    import numpy as np
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    unique_colors, counts = np.unique(input_grid, return_counts=True)
    background_color = unique_colors[np.argmax(counts)]
    # Assume the next most frequent color is the square color
    square_color = unique_colors[counts.argsort()[-2]]

    square_positions = np.argwhere(input_grid == square_color)
    if len(square_positions) == 0:
        return output_grid

    groups = group_connected_positions(square_positions)

    for group in groups:
        group = np.array(group)
        min_row, min_col = group.min(axis=0)
        max_row, max_col = group.max(axis=0)

        corners = [
            (min_row - 1, min_col - 1),  # top-left
            (min_row - 1, max_col + 1),  # top-right
            (max_row + 1, min_col - 1),  # bottom-left
            (max_row + 1, max_col + 1),  # bottom-right
        ]
        for idx, (r, c) in enumerate(corners, start=1):
            if 0 <= r < nrows and 0 <= c < ncols and input_grid[r, c] == background_color:
                output_grid[r, c] = idx

    return output_grid


def solve_c909285e(input_grid):
    """
    Detects the frame (least frequent color) in the grid and returns the frame with its interior.

    Concept:
        - Identify the color that appears least frequently (assumed to be the frame).
        - Extract the minimal bounding rectangle containing all frame pixels.
        - Return the subgrid defined by this rectangle.

    Transformation Steps:
        1. Find the least frequent (frame) color in the grid.
        2. Locate all positions of this color.
        3. Compute the bounding box (min/max row and column).
        4. Return the subgrid within this bounding box.
    """

    input_grid = np.array(input_grid)
    unique_colors, counts = np.unique(input_grid, return_counts=True)

    # Find the least frequent color (frame color) and then frame itself
    frame_color = unique_colors[np.argmin(counts)]
    frame_positions = np.argwhere(input_grid == frame_color)

    min_row, min_col = frame_positions.min(axis=0)
    max_row, max_col = frame_positions.max(axis=0)

    # Return the picture with the frame
    output_grid = input_grid[min_row : max_row + 1, min_col : max_col + 1]

    return output_grid


def solve_342ae2ed(input_grid):
    """
    Connects two same-color blocks by drawing a diagonal line between their nearest corners.

    Concept:
        - For each non-background color, find all connected groups (expecting exactly two).
        - If there are exactly two groups, connect their bounding box corners with a diagonal line.

    Transformation Steps:
        1. Identify background and non-background colors.
        2. For each non-background color, find connected groups (blocks)
        3. If there are exactly two blocks, compute their bounding box corners.
        4. Draw a diagonal line between the appropriate corners.

    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = input_grid.copy()

    unique_colors, counts = np.unique(input_grid, return_counts=True)
    background_color = unique_colors[np.argmax(counts)]
    non_bg_colors = unique_colors[unique_colors != background_color]

    for color in non_bg_colors:
        positions = np.argwhere(input_grid == color)
        if len(positions) == 0:
            continue
        groups = group_connected_positions(positions)
        if len(groups) != 2:  # expect exactly two block per color to connect
            continue

        # Get bounding box corners for both groups
        corners = []
        for group in groups:
            group = np.array(group)
            min_row, min_col = group.min(axis=0)
            max_row, max_col = group.max(axis=0)
            corners.append((min_row, min_col, max_row, max_col))

        (r1_min, c1_min, r1_max, c1_max), (r2_min, c2_min, r2_max, c2_max) = corners

        # Determine which diagonal to draw
        if r1_min < r2_min and c1_min < c2_min:
            # Top-left to bottom-right
            for step in range(1, min(r2_min - r1_max, c2_min - c1_max) + 1):
                r, c = r1_max + step, c1_max + step
                if r > r2_min or c > c2_min:
                    break
                output_grid[r, c] = color
        elif r1_min > r2_min and c1_min > c2_min:
            # Bottom-right to top-left
            for step in range(1, min(r1_min - r2_max, c1_min - c2_max) + 1):
                r, c = r1_min - step, c1_min - step
                if r < r2_max or c < c2_max:
                    break
                output_grid[r, c] = color
        elif r1_min > r2_min and c1_min < c2_min:
            # Bottom-left to top-right
            for step in range(1, min(r1_min - r2_max, c2_min - c1_max) + 1):
                r, c = r1_min - step, c1_max + step
                if r < r2_max or c > c2_min:
                    break
                output_grid[r, c] = color
        elif r1_min < r2_min and c1_min > c2_min:
            # Top-right to bottom-left
            for step in range(1, min(r2_min - r1_max, c1_min - c2_max) + 1):
                r, c = r1_max + step, c1_min - step
                if r > r2_min or c < c2_max:
                    break
                output_grid[r, c] = color

    return output_grid


def solve_a3325580(input_grid):
    """
    Find the non-background color(s) that appear most frequently in the input grid.
    Return a new grid with those colors forming a vertical bar of length equal to their count, ordered by their first appearance from left to right.

    Concept:
    - frequency count of colors
    - ordering by first appearance

    Steps:
        1. Identify the background color (most frequent).
        2. Find the second most frequent color(s).
        3. Order these colors by their leftmost column of appearance.
        4. Build a vertical bar with these colors, each as a column, height = their count.
    """
    import numpy as np

    input_grid = np.array(input_grid)
    unique_colors, counts = np.unique(input_grid, return_counts=True)
    order = np.argsort(-counts)  # descending order

    background_color = unique_colors[order[0]]
    # Find the count of the second most frequent color(s)
    second_count = counts[order[1]]
    # Get all colors with this count (could be ties)
    second_colors = unique_colors[counts == second_count]

    # Order by first (leftmost) column of appearance
    min_cols = [np.argwhere(input_grid == color)[:, 1].min() for color in second_colors]
    ordered_colors = second_colors[np.argsort(min_cols)]

    # Build the output: each color forms a column of height = second_count
    output_grid = np.stack([np.full(second_count, color) for color in ordered_colors], axis=1)

    return output_grid


def solve_4acc7107(input_grid):
    """
    Arrange same-color objects by their position in the input grid.
    Each connected group of a color is stacked from bottom to top, left to right, in order of their first column appearance.

    Concept:
    - arranging same color objects
    - sorting by spatial properties: first column appearance from left to right


    Steps:
        1. Identify background color (most frequent).
        2. For each non-background color, sort by first column of appearance.
        3. For each color, find connected groups and sort them by their leftmost column.
        4. Place each group as a block in the output grid, stacking vertically and shifting right for each color.
    """

    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    unique_colors, counts = np.unique(input_grid, return_counts=True)
    order = np.argsort(-counts)  # descending order

    background_color = unique_colors[order[0]]
    output_grid = np.full((nrows, ncols), background_color)

    non_bg_colors = unique_colors[order[1:]]
    # Sort colors by their first (leftmost) column appearance
    min_cols = [np.min(np.argwhere(input_grid == color)[:, 1]) for color in non_bg_colors]
    sorted_colors = non_bg_colors[np.argsort(min_cols)]

    col_marker = 0
    for color in sorted_colors:
        positions = np.argwhere(input_grid == color)
        if len(positions) == 0:
            continue
        groups = group_connected_positions(positions)
        # Sort groups by their leftmost column
        min_cs = [np.min(np.array(group)[:, 1]) for group in groups]
        arranged_groups = [groups[i] for i in np.argsort(min_cs)]

        max_w = 0
        r, c = nrows - 1, col_marker
        for group in arranged_groups:
            group = np.array(group)
            min_row, min_col = np.min(group, axis=0)
            max_row, max_col = np.max(group, axis=0)
            block = input_grid[min_row : max_row + 1, min_col : max_col + 1].copy()
            block[block != color] = (
                background_color  # clean block if there is any other color inside
            )

            h, w = block.shape
            output_grid[r - h + 1 : r + 1, c : c + w] = block
            r -= h + 1
            max_w = max(max_w, w)

        col_marker += max_w + 1

    return output_grid


def solve_b94a9452(input_grid):
    """
    Find the colored block (expecting two colors in it), interchange the colors, and return the block.

    Concept:
        - Extacting colored block (non-background).
        - Swaping colors

    Steps:
        1. Identify the background color (most frequent).
        2. Find all positions that are not background.
        3. Extract the minimal bounding rectangle containing all non-background cells.
        4. Swap the two non-background colors in this block.
        5. Return the transformed block.
    """

    input_grid = np.array(input_grid)
    unique_colors, counts = np.unique(input_grid, return_counts=True)
    order = np.argsort(-counts)  # descending order
    background_color = unique_colors[order[0]]
    non_bg_colors = unique_colors[order[1:]]

    # Find bounding box of non-background region
    pos = np.argwhere(input_grid != background_color)
    min_row, min_col = pos.min(axis=0)
    max_row, max_col = pos.max(axis=0)
    block = input_grid[min_row : max_row + 1, min_col : max_col + 1].copy()

    # Swap the two non-background colors
    if len(non_bg_colors) == 2:
        c1, c2 = non_bg_colors
        block_swapped = block.copy()
        block_swapped[block == c1] = -1  # Temporary marker
        block_swapped[block == c2] = c1
        block_swapped[block_swapped == -1] = c2
        return block_swapped
    else:
        # If not exactly two colors, just return the block unchanged
        return block


def solve_67c52801(input_grid):
    """
    Rearranges colored blocks from the top part to the bottom part by matching their widths to available (background) spaces.

    Concept:
        - Identify colored blocks in the upper part of the grid.
        - Identify contiguous background spaces in the bottom two rows.
        - Place each colored block into a matching-width background space, rotating if necessary.

    Steps:
        1. Identify the background color (most frequent).
        2. Find contiguous background spaces in the bottom two rows.
        3. Extract colored blocks from the top rows.
        4. Sort background spaces and blocks by width (descending).
        5. Place each block into a matching-width space, rotating if needed.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.copy(input_grid)

    # Identify background color (most frequent)
    unique_colors, counts = np.unique(input_grid, return_counts=True)
    background_color = unique_colors[np.argmax(counts)]

    # Find contiguous background spaces in the bottom two rows
    bottom_rows = input_grid[-2:, :]
    pos = np.argwhere(bottom_rows == background_color)
    groups = group_connected_positions(pos)

    # Sort background groups by width (descending)
    group_widths = [len(group) for group in groups]
    sorted_indices = np.argsort(-np.array(group_widths))
    groups = [groups[i] for i in sorted_indices]

    # Extract colored blocks from the top rows
    top_rows = input_grid[:-2, :]
    colors = np.unique(top_rows[top_rows != background_color])
    output_grid[:-2, :] = background_color  # Clear top rows

    colored_blocks = []
    for color in colors:
        pos = np.argwhere(top_rows == color)
        min_row, min_col = pos.min(axis=0)
        max_row, max_col = pos.max(axis=0)
        block = top_rows[min_row : max_row + 1, min_col : max_col + 1]
        colored_blocks.append(block)

    # Sort blocks by area (descending)
    block_areas = [block.shape[0] * block.shape[1] for block in colored_blocks]
    sorted_block_indices = np.argsort(-np.array(block_areas))
    colored_blocks = [colored_blocks[i] for i in sorted_block_indices]

    # Place each block into a matching-width background space
    used_blocks = set()
    for group in groups:
        group = np.array(group) + np.array([nrows - 2, 0])  # Adjust to grid coordinates
        min_col, max_col = group[:, 1].min(), group[:, 1].max()
        group_width = max_col - min_col + 1

        for idx, block in enumerate(colored_blocks):
            if idx in used_blocks:
                continue
            for candidate in [block, np.rot90(block)]:
                bh, bw = candidate.shape
                # Only place if block fits exactly in width and fits in the second last row
                if bw == group_width and bh <= 2:
                    row_end = nrows - 1
                    row_start = row_end - bh
                    output_grid[row_start:row_end, min_col : min_col + bw] = candidate
                    used_blocks.add(idx)
                    break
            if idx in used_blocks:
                break

    return output_grid


def solve_22208ba4(input_grid):
    """
    From the corners, select the blocks of the same color that occurs the most.
    Moves the colored blocks from their corner positions toward opposite corners.

    Concept:
        - Identify the background color as the most frequent color.
        - Among non-background colors, select the one with the highest number of connected groups.
        - For each connected group of that color, erase it from its original position and move the block toward the opposite corner.

    Steps:
        1. Determine background color and non-background colors.
        2. Find the non-background color with the most connected groups.
        3. For each group of that color, erase the block and place it in the opposite corner if it fits.
    """
    import numpy as np
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.copy(input_grid)

    # Identify background color (most frequent)
    unique_colors, counts = np.unique(input_grid, return_counts=True)
    order = np.argsort(-counts)  # descending order
    background_color = unique_colors[order[0]]
    non_bg_colors = unique_colors[order[1:]]

    # Select the blocks of the same color that occurs the most.
    selected_groups = None
    max_num_groups = 0
    for color in non_bg_colors:
        positions = np.argwhere(input_grid == color)
        groups = group_connected_positions(positions)
        num_groups = len(groups)
        if num_groups > max_num_groups:
            max_num_groups = num_groups
            selected_color = color
            selected_groups = groups

    if selected_groups is not None:
        for group in selected_groups:
            group = np.array(group)
            min_row, min_col = group.min(axis=0)
            max_row, max_col = group.max(axis=0)
            output_grid[min_row : max_row + 1, min_col : max_col + 1] = background_color
            block = input_grid[min_row : max_row + 1, min_col : max_col + 1]
            H, W = block.shape

            # Move the selected block to the appropriate corner
            if min_row == 0 and min_col == 0:  # move block toward bottom-right
                new_min_row = min_row + H
                new_min_col = min_col + W
                output_grid[new_min_row : new_min_row + H, new_min_col : new_min_col + W] = block
            elif min_row == 0 and max_col == ncols - 1:  # move block toward bottom-left
                new_min_row = min_row + H
                new_max_col = max_col - W
                output_grid[
                    new_min_row : new_min_row + H, new_max_col - W + 1 : new_max_col + 1
                ] = block
            elif max_row == nrows - 1 and min_col == 0:  # move block toward top-right
                new_max_row = max_row - H
                new_min_col = min_col + W
                output_grid[
                    new_max_row - H + 1 : new_max_row + 1, new_min_col : new_min_col + W
                ] = block
            elif max_row == nrows - 1 and max_col == ncols - 1:  # move block toward top-left
                new_max_row = max_row - H
                new_max_col = max_col - W
                output_grid[
                    new_max_row - H + 1 : new_max_row + 1, new_max_col - W + 1 : new_max_col + 1
                ] = block

    return output_grid


def solve_ce039d91(input_grid):
    """
    Paint the left-right symmetric non-background part in color 1.

    Concept:
        - Identify the background color (most frequent).
        - For each non-background cell, if its horizontal mirror is also non-background, paint both positions with color 1.

    Steps:
        1. Find the background and non-background colors.
        2. For each non-background cell, check its horizontal symmetric cell.
        3. If both are non-background, set both to color 1.
    """
    import numpy as np

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.copy(input_grid)

    # Identify background color (most frequent)
    unique_colors, counts = np.unique(input_grid, return_counts=True)
    order = np.argsort(-counts)  # descending order
    background_color = unique_colors[order[0]]
    non_bg_color = unique_colors[order[1]]

    # Paint symmetric non-background pairs in color 1
    non_bg_pos = np.argwhere(input_grid != background_color)
    for r, c in non_bg_pos:
        sym_c = ncols - 1 - c
        if input_grid[r, sym_c] == non_bg_color:
            output_grid[r, c] = 1
            output_grid[r, sym_c] = 1

    return output_grid


def solve_539a4f51(input_grid):
    """
    Expands the input grid to double its size in both dimensions and fills it with a diagonal pattern
    using the non-background colors from the first row of the input.

    Concept:
        - The output grid is 2x the input size in both rows and columns.
        - Colors from the first row (excluding background/zero) are repeated in order.
        - Each row i is filled with its color up to column i (inclusive), and each column i is filled up to row i.

    Steps:
        1. Convert input to numpy array and determine its shape.
        2. Create an output grid of zeros with doubled dimensions.
        3. Extract non-background colors from the first row, preserving order.
        4. For each row and column in the output, fill diagonals with the repeating color pattern.
    """

    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    Nrows, Ncols = 2 * nrows, 2 * ncols
    output_grid = np.zeros((Nrows, Ncols), dtype=int)

    # Extract non-background colors from the first row, preserving order
    colors = input_grid[0]
    colors = colors[colors != 0]
    num_colors = len(colors)

    # Fill the output grid with the diagonal pattern
    for i in range(Nrows):
        color = colors[i % num_colors]
        output_grid[i, : i + 1] = color
        output_grid[:i, i] = color

    return output_grid
