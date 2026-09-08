"""LLM-assisted solvers for remaining ARC-AGI-2 training tasks.

Each `solve_<task_id>` was inferred from the official training pairs and kept
only if it matches every official train and test pair exactly.
"""

import numpy as np


def solve_00576224(input_grid):
    """
    Concepts: tiling, horizontal flip, alternating rows of tiles

    Transformation steps:
    1. Repeat the input three times horizontally.
    2. Stack that strip three times, flipping the middle strip left-right.
    """
    input_grid = np.array(input_grid)
    rows = []
    for i in range(3):
        block = input_grid if i % 2 == 0 else np.fliplr(input_grid)  # Step 2: flip odd strips
        rows.append(np.tile(block, (1, 3)))  # Step 1: tile horizontally
    output_grid = np.vstack(rows)
    return output_grid


def solve_0692e18c(input_grid):
    """
    Concepts: fractal copy, color inversion, indicator cells

    Transformation steps:
    1. Build a color-inverted copy of the input (nonzero becomes 0, 0 becomes the sprite color).
    2. Scale the canvas by the input size.
    3. Where the input cell is nonzero, paste the inverted sprite into that block.
    """
    input_grid = np.array(input_grid)
    h, w = input_grid.shape
    color = int(next(c for c in np.unique(input_grid) if c != 0))
    inverted = np.where(input_grid == 0, color, 0)  # Step 1: invert colors
    output_grid = np.zeros((h * h, w * w), dtype=int)  # Step 2: scaled canvas
    for i in range(h):
        for j in range(w):
            if input_grid[i, j] != 0:  # Step 3: paste on nonzero cells
                output_grid[i * h : (i + 1) * h, j * w : (j + 1) * w] = inverted
    return output_grid


def solve_0c786b71(input_grid):
    """
    Concepts: dihedral kaleidoscope, rotation, reflection

    Transformation steps:
    1. Place rot180(input) in the top-left quadrant.
    2. Place flipud(input) top-right, fliplr(input) bottom-left, and the original bottom-right.
    """
    input_grid = np.array(input_grid)
    top_half = np.hstack(
        [np.rot90(input_grid, 2), np.flipud(input_grid)]
    )  # Step 1–2: top quadrants
    bottom_half = np.hstack([np.fliplr(input_grid), input_grid])  # Step 2: bottom quadrants
    output_grid = np.vstack([top_half, bottom_half])
    return output_grid


def solve_15696249(input_grid):
    """
    Concepts: constant row/column, tiling, alignment

    Transformation steps:
    1. Find the fully constant row or column in the input.
    2. Tile the input three times along the perpendicular axis.
    3. Place that strip in the block whose index matches the constant line.
    """
    input_grid = np.array(input_grid)
    h, w = input_grid.shape
    output_grid = np.zeros((h * 3, w * 3), dtype=int)
    for i in range(h):
        if np.all(input_grid[i] == input_grid[i, 0]):
            output_grid[i * h : (i + 1) * h, :] = np.tile(
                input_grid, (1, 3)
            )  # Steps 2–3: constant row
            return output_grid
    for j in range(w):
        if np.all(input_grid[:, j] == input_grid[0, j]):
            output_grid[:, j * w : (j + 1) * w] = np.tile(
                input_grid, (3, 1)
            )  # Steps 2–3: constant column
            return output_grid
    return output_grid


def solve_1a2e2828(input_grid):
    """
    Concepts: full row/column, unique divider color

    Transformation steps:
    1. Find a row that is a single nonzero color across its full width, or a column that is a single nonzero color across its full height.
    2. Return that color as a 1x1 grid.
    """
    input_grid = np.array(input_grid)
    for row in input_grid:
        if row[0] != 0 and np.all(row == row[0]):
            output_grid = np.array([[int(row[0])]])
            return output_grid
    for col in input_grid.T:
        if col[0] != 0 and np.all(col == col[0]):
            output_grid = np.array([[int(col[0])]])
            return output_grid
    output_grid = np.array([[0]])
    return output_grid


def solve_1e0a9b12(input_grid):
    """
    Concepts: gravity, per-column packing

    Transformation steps:
    1. In each column, keep nonzero cells in order.
    2. Drop them to the bottom of the column.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape
    output_grid = np.zeros_like(input_grid)
    for c in range(ncols):
        nz = input_grid[:, c]
        nz = nz[nz != 0]  # Step 1: keep nonzero cells
        output_grid[nrows - len(nz) :, c] = nz  # Step 2: pack to the bottom
    return output_grid


def solve_1f85a75f(input_grid):
    """
    Concepts: connected components, largest object, crop

    Transformation steps:
    1. Find 4-connected same-color objects.
    2. Crop the bounding box of the largest object, keeping only that object.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    parts = []
    for color in np.unique(input_grid):
        if color == 0:
            continue
        parts.extend(group_connected_positions(np.argwhere(input_grid == color), connectivity=4))

    part = np.array(max(parts, key=len))
    min_row, min_col = part.min(axis=0)
    max_row, max_col = part.max(axis=0)
    output_grid = np.zeros((max_row - min_row + 1, max_col - min_col + 1), dtype=int)
    for r, c in part:
        output_grid[r - min_row, c - min_col] = input_grid[r, c]
    return output_grid


def solve_22168020(input_grid):
    """
    Concepts: connected objects, horizontal fill

    Transformation steps:
    1. Group 8-connected cells of the same color.
    2. In each row of an object, fill from its leftmost to rightmost cell with that color.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    for color in np.unique(input_grid):
        if color == 0:
            continue
        for part in group_connected_positions(np.argwhere(input_grid == color), connectivity=8):
            part = np.array(part)
            for r in np.unique(part[:, 0]):
                cols = part[part[:, 0] == r, 1]
                output_grid[r, cols.min() : cols.max() + 1] = color
    return output_grid


def solve_23b5c85d(input_grid):
    """
    Concepts: connected components, smallest object, crop

    Transformation steps:
    1. Find 4-connected same-color objects.
    2. Return the bounding box of the smallest object.
    """
    from arc_agi_2_atlas.providers.grid_utils import (
        group_connected_positions,
        extract_min_bound_block,
    )

    input_grid = np.array(input_grid)
    parts = []
    for color in np.unique(input_grid):
        if color == 0:
            continue
        parts.extend(group_connected_positions(np.argwhere(input_grid == color), connectivity=4))

    smallest = min(parts, key=len)
    output_grid = extract_min_bound_block(input_grid, smallest)
    return output_grid


def solve_27a28665(input_grid):
    """
    Concepts: binary pattern classification, shape lookup

    Transformation steps:
    1. Ignore the actual color; treat nonzero cells as a 3x3 mask.
    2. Map each distinct mask to a fixed output color.
    """
    input_grid = np.array(input_grid)
    mask = tuple((input_grid != 0).astype(int).ravel())
    patterns = {
        (0, 1, 1, 0, 1, 1, 1, 0, 0): 3,
        (0, 1, 0, 1, 1, 1, 0, 1, 0): 6,
        (1, 0, 1, 0, 1, 0, 1, 0, 1): 2,
        (1, 1, 0, 1, 0, 1, 0, 1, 0): 1,
    }
    output_grid = np.array([[patterns[mask]]])
    return output_grid


def solve_34b99a2b(input_grid):
    """
    Concepts: symmetry, XOR gate, scalar multiplication

    Transformation steps:
    1. Identify the column of 4s that divides the grid into two equal-size parts.
    2. XOR the occupancy of the left and right parts.
    3. Multiply the result by 2.
    """
    input_grid = np.array(input_grid)
    nrows, ncols = input_grid.shape

    col_with_4 = None
    for i in range(ncols):
        if np.array_equal(input_grid[:, i], 4 * np.ones(nrows)):
            col_with_4 = i
            break

    left = input_grid[:, :col_with_4]
    right = input_grid[:, col_with_4 + 1 :]
    output_grid = ((left != 0) ^ (right != 0)).astype(int) * 2
    return output_grid


def solve_3906de3d(input_grid):
    """
    Concepts: gravity, per-column packing upward

    Transformation steps:
    1. In each column, keep nonzero cells in order.
    2. Pack them to the top of the column.
    """
    input_grid = np.array(input_grid)
    ncols = input_grid.shape[1]
    output_grid = np.zeros_like(input_grid)
    for c in range(ncols):
        nz = input_grid[:, c]
        nz = nz[nz != 0]
        output_grid[: len(nz), c] = nz
    return output_grid


def solve_3af2c5a8(input_grid):
    """
    Concepts: grid flipping and concatenation (stacking)

    Transformation steps:
    1. Create left-right, upside-down, and 180-degree variants of the input.
    2. Horizontally stack the original with its left-right flip (top half).
    3. Horizontally stack the upside-down flip with the 180-degree rotation (bottom half).
    4. Vertically stack the two halves.
    """
    input_grid = np.array(input_grid)
    flipped_lr = np.fliplr(input_grid)
    flipped_ud = np.flipud(input_grid)
    flipped_180 = np.rot90(input_grid, 2)
    top_half = np.hstack([input_grid, flipped_lr])
    bottom_half = np.hstack([flipped_ud, flipped_180])
    output_grid = np.vstack([top_half, bottom_half])
    return output_grid


def solve_3c9b0459(input_grid):
    """
    Concepts: rotation

    Transformation steps:
    1. Rotate the grid 180 degrees.
    """
    input_grid = np.array(input_grid)
    output_grid = np.rot90(input_grid, 2)
    return output_grid


def solve_496994bd(input_grid):
    """
    Concepts: vertical reflection, palindrome, copy to opposite edge

    Transformation steps:
    1. Take the contiguous nonempty rows at the top.
    2. Write their vertical flip onto the bottom of the grid.
    """
    input_grid = np.array(input_grid)
    rows = np.where(np.any(input_grid != 0, axis=1))[0]
    content = input_grid[rows.min() : rows.max() + 1]
    output_grid = input_grid.copy()
    output_grid[-content.shape[0] :] = np.flipud(content)
    return output_grid


def solve_5582e5ca(input_grid):
    """
    Concepts: most frequent color, fill

    Transformation steps:
    1. Find the most common color in the grid.
    2. Fill the whole grid with that color.
    """
    input_grid = np.array(input_grid)
    mode = int(np.bincount(input_grid.ravel()).argmax())
    output_grid = np.full_like(input_grid, mode)
    return output_grid


def solve_60c09cac(input_grid):
    """
    Concepts: integer scaling, pixel duplication

    Transformation steps:
    1. Replace each cell with a 2x2 block of the same color.
    """
    input_grid = np.array(input_grid)
    output_grid = np.kron(input_grid, np.ones((2, 2), dtype=int))
    return output_grid


def solve_662c240a(input_grid):
    """
    Concepts: stacked 3x3 blocks, diagonal symmetry, odd-one-out

    Transformation steps:
    1. Split the 9x3 grid into three 3x3 blocks.
    2. Return the block that is not equal to its transpose.
    """
    input_grid = np.array(input_grid)
    for i in range(3):
        block = input_grid[i * 3 : (i + 1) * 3]
        if not np.array_equal(block, block.T):
            output_grid = block
            return output_grid
    output_grid = input_grid[:3]
    return output_grid


def solve_67a3c6ac(input_grid):
    """
    Concepts: horizontal reflection

    Transformation steps:
    1. Flip the grid left-right.
    """
    input_grid = np.array(input_grid)
    output_grid = np.fliplr(input_grid)
    return output_grid


def solve_68b67ca3(input_grid):
    """
    Concepts: downsampling, even cells

    Transformation steps:
    1. Keep every other row and column, starting at (0, 0).
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid[::2, ::2]
    return output_grid


def solve_7468f01a(input_grid):
    """
    Concepts: crop to nonzero, horizontal flip

    Transformation steps:
    1. Crop to the bounding box of nonzero cells.
    2. Flip that crop left-right.
    """
    input_grid = np.array(input_grid)
    rows, cols = np.where(input_grid != 0)
    crop = input_grid[rows.min() : rows.max() + 1, cols.min() : cols.max() + 1]
    output_grid = np.fliplr(crop)
    return output_grid


def solve_7fe24cdd(input_grid):
    """
    Concepts: four rotations, 2x2 arrangement

    Transformation steps:
    1. Place the input top-left and a 90-degree clockwise rotation top-right.
    2. Place a 90-degree counterclockwise rotation bottom-left and a 180-degree rotation bottom-right.
    """
    input_grid = np.array(input_grid)
    top_half = np.hstack([input_grid, np.rot90(input_grid, 3)])
    bottom_half = np.hstack([np.rot90(input_grid, 1), np.rot90(input_grid, 2)])
    output_grid = np.vstack([top_half, bottom_half])
    return output_grid


def solve_833dafe3(input_grid):
    """
    Concepts: dihedral kaleidoscope, rotation, reflection

    Transformation steps:
    1. Place rot180(input) in the top-left quadrant.
    2. Place flipud(input) top-right, fliplr(input) bottom-left, and the original bottom-right.
    """
    input_grid = np.array(input_grid)
    top_half = np.hstack([np.rot90(input_grid, 2), np.flipud(input_grid)])
    bottom_half = np.hstack([np.fliplr(input_grid), input_grid])
    output_grid = np.vstack([top_half, bottom_half])
    return output_grid


def solve_9172f3a0(input_grid):
    """
    Concepts: integer scaling, pixel duplication

    Transformation steps:
    1. Replace each cell with a 3x3 block of the same color.
    """
    input_grid = np.array(input_grid)
    output_grid = np.kron(input_grid, np.ones((3, 3), dtype=int))
    return output_grid


def solve_9dfd6313(input_grid):
    """
    Concepts: transpose

    Transformation steps:
    1. Transpose the grid.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.T
    return output_grid


def solve_a416b8f3(input_grid):
    """
    Concepts: horizontal concatenation, copy

    Transformation steps:
    1. Concatenate the input with itself on the right.
    """
    input_grid = np.array(input_grid)
    output_grid = np.hstack([input_grid, input_grid])
    return output_grid


def solve_b6afb2da(input_grid):
    """
    Concepts: rectangles, corners, edges, interior recolor

    Transformation steps:
    1. Find each solid rectangle.
    2. Recolor corners to 1, remaining border to 4, and interior to 2.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    for color in np.unique(input_grid):
        if color == 0:
            continue
        for part in group_connected_positions(np.argwhere(input_grid == color), connectivity=4):
            part = np.array(part)
            r0, c0 = part.min(axis=0)
            r1, c1 = part.max(axis=0)
            for i in range(r0, r1 + 1):
                for j in range(c0, c1 + 1):
                    is_corner = i in (r0, r1) and j in (c0, c1)
                    is_edge = i in (r0, r1) or j in (c0, c1)
                    if is_corner:
                        output_grid[i, j] = 1
                    elif is_edge:
                        output_grid[i, j] = 4
                    else:
                        output_grid[i, j] = 2
    return output_grid


def solve_b9b7f026(input_grid):
    """
    Concepts: hollow object, bounding box

    Transformation steps:
    1. Find same-color 4-connected objects.
    2. Return the color of the object whose bounding box contains background cells (a hole).
    """
    from arc_agi_2_atlas.providers.grid_utils import (
        group_connected_positions,
        extract_min_bound_block,
    )

    input_grid = np.array(input_grid)
    for color in np.unique(input_grid):
        if color == 0:
            continue
        for part in group_connected_positions(np.argwhere(input_grid == color), connectivity=4):
            block = extract_min_bound_block(input_grid, part)
            if np.any(block == 0):
                output_grid = np.array([[int(color)]])
                return output_grid
    output_grid = np.array([[0]])
    return output_grid


def solve_c59eb873(input_grid):
    """
    Concepts: integer scaling, pixel duplication

    Transformation steps:
    1. Replace each cell with a 2x2 block of the same color.
    """
    input_grid = np.array(input_grid)
    output_grid = np.kron(input_grid, np.ones((2, 2), dtype=int))
    return output_grid


def solve_ce22a75a(input_grid):
    """
    Concepts: 3x3 tiling, marker cells, fill

    Transformation steps:
    1. Treat the grid as a 3x3 arrangement of 3x3 blocks.
    2. For each 5 (the center of a block), fill that whole 3x3 block with 1.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    for i, j in zip(*np.where(input_grid == 5)):
        r0, c0 = (i // 3) * 3, (j // 3) * 3
        output_grid[r0 : r0 + 3, c0 : c0 + 3] = 1
    return output_grid


def solve_d10ecb37(input_grid):
    """
    Concepts: crop, top-left 2x2

    Transformation steps:
    1. Return the top-left 2x2 block.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid[:2, :2]
    return output_grid


def solve_d13f3404(input_grid):
    """
    Concepts: diagonal rays, canvas doubling

    Transformation steps:
    1. Make a canvas twice as tall and wide.
    2. From each nonzero input cell, draw a down-right diagonal of that color.
    """
    input_grid = np.array(input_grid)
    n = input_grid.shape[0]
    output_grid = np.zeros((2 * n, 2 * n), dtype=int)
    h, w = input_grid.shape
    for i in range(h):
        for j in range(w):
            if input_grid[i, j] == 0:
                continue
            k = 0
            while i + k < 2 * n and j + k < 2 * n:
                output_grid[i + k, j + k] = input_grid[i, j]
                k += 1
    return output_grid


def solve_d9fac9be(input_grid):
    """
    Concepts: 3x3 square, center color

    Transformation steps:
    1. Find a 3x3 block whose border is a single nonzero color and whose center is a different nonzero color.
    2. Return the center color as a 1x1 grid.
    """
    input_grid = np.array(input_grid)
    h, w = input_grid.shape
    for i in range(h - 2):
        for j in range(w - 2):
            block = input_grid[i : i + 3, j : j + 3]
            border = np.concatenate([block[0], block[-1], block[1:-1, 0], block[1:-1, -1]])
            if border[0] != 0 and np.all(border == border[0]) and block[1, 1] not in (0, border[0]):
                output_grid = np.array([[int(block[1, 1])]])
                return output_grid
    output_grid = np.array([[0]])
    return output_grid


def solve_dc1df850(input_grid):
    """
    Concepts: neighborhood fill, marker color 2

    Transformation steps:
    1. For every cell of color 2, fill empty 8-neighbors with 1.
    """
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    h, w = input_grid.shape
    for i, j in zip(*np.where(input_grid == 2)):
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and output_grid[ni, nj] == 0:
                    output_grid[ni, nj] = 1
    return output_grid


def solve_e98196ab(input_grid):
    """
    Concepts: horizontal divider, overlay

    Transformation steps:
    1. Split the grid on the row of 5s.
    2. Overlay the bottom half onto the top half, keeping top nonzero cells.
    """
    input_grid = np.array(input_grid)
    nrows, _ = input_grid.shape
    row_with_5 = None
    for i in range(nrows):
        if np.array_equal(input_grid[i], 5 * np.ones(input_grid.shape[1])):
            row_with_5 = i
            break
    top = input_grid[:row_with_5]
    bottom = input_grid[row_with_5 + 1 :]
    output_grid = np.where(top != 0, top, bottom)
    return output_grid


def solve_f25ffba3(input_grid):
    """
    Concepts: vertical symmetry, mirror the lower half upward

    Transformation steps:
    1. Replace the upper half with the vertical flip of the lower half.
    """
    input_grid = np.array(input_grid)
    h = input_grid.shape[0]
    output_grid = input_grid.copy()
    output_grid[: h // 2] = np.flipud(input_grid[h // 2 :])
    return output_grid


def solve_f8ff0b80(input_grid):
    """
    Concepts: connected components, sort by size

    Transformation steps:
    1. Find 8-connected objects.
    2. Return their colors as a column, largest object first.
    """
    from arc_agi_2_atlas.providers.grid_utils import group_connected_positions

    input_grid = np.array(input_grid)
    comps = []
    for color in np.unique(input_grid):
        if color == 0:
            continue
        for part in group_connected_positions(np.argwhere(input_grid == color), connectivity=8):
            comps.append((int(color), part))
    comps = sorted(comps, key=lambda item: -len(item[1]))
    output_grid = np.array([[color] for color, _ in comps], dtype=int)
    return output_grid
