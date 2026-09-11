"""Synthetic contrast tests for structural rules not proved by corpus replay."""

import importlib.util
from pathlib import Path
from typing import Any, cast


def _load_solution(task_id: str) -> Any:
    spec = importlib.util.spec_from_file_location(
        f"synthetic_{task_id}", Path("solutions") / f"{task_id}.py"
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return cast("Any", module)


def test_rotate_rule_generalizes_to_non_square_grid() -> None:
    assert _load_solution("ed36ccf7").solve([[1, 2, 3], [4, 5, 6]]) == [
        [3, 6],
        [2, 5],
        [1, 4],
    ]


def test_flip_rule_preserves_shape_and_background() -> None:
    assert _load_solution("67a3c6ac").solve([[0, 1, 2], [3, 4, 5]]) == [
        [2, 1, 0],
        [5, 4, 3],
    ]


def test_square_spiral_generalizes_beyond_observed_multiple_of_four() -> None:
    output = _load_solution("28e73c20").solve([[0] * 12 for _ in range(12)])

    assert output[6][5] == 3
    assert sum(value == 3 for row in output for value in row) == 84


def test_tile_sort_discovers_grid_and_tile_sizes() -> None:
    solver = _load_solution("dc2aa30b").solve
    grid = [
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
    ]
    assert solver(grid) == [
        [1, 1, 0, 1, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]


def test_marker_panels_derive_lines_from_marker_rows_and_canvas() -> None:
    solver = _load_solution("1bfc4729").solve
    grid = [[0] * 8 for _ in range(12)]
    grid[3][5] = 4
    grid[9][2] = 6

    output = solver(grid)
    assert output[0] == [4] * 8
    assert output[3] == [4] * 8
    assert output[9] == [6] * 8
    assert output[11] == [6] * 8
    assert output[5] == [4, 0, 0, 0, 0, 0, 0, 4]
    assert output[6] == [6, 0, 0, 0, 0, 0, 0, 6]


def test_marker_alignment_rule_uses_border_anchor() -> None:
    solver = _load_solution("581f7754").solve
    grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    assert solver(grid) == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [2, 0, 1, 2, 1, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
    ]


def test_ray_rule_extends_through_a_single_outline_gap() -> None:
    solver = _load_solution("e12f9a14").solve
    grid = [[8] * 8 for _ in range(6)]
    for row in range(1, 5):
        for col in range(1, 5):
            if row in (1, 4) or col in (1, 4):
                grid[row][col] = 3
    for row in (2, 3):
        for col in (2, 3):
            grid[row][col] = 2
    grid[2][4] = 8

    expected = [row[:] for row in grid]
    for col in range(4, 8):
        expected[2][col] = 2
    assert solver(grid) == expected


def test_ray_rule_merges_converging_diagonals() -> None:
    solver = _load_solution("e12f9a14").solve
    grid = [[8] * 12 for _ in range(10)]
    for top, left, color, gap in ((5, 2, 2, (4, 4)), (5, 8, 4, (4, 7))):
        for row in range(top - 1, top + 3):
            for col in range(left - 1, left + 3):
                if row in (top - 1, top + 2) or col in (left - 1, left + 2):
                    grid[row][col] = 3
        for row in (top, top + 1):
            for col in (left, left + 1):
                grid[row][col] = color
        grid[gap[0]][gap[1]] = 8

    expected = [row[:] for row in grid]
    expected[4][4] = 2
    expected[4][7] = 4
    for row in range(4):
        expected[row][5] = 2
        expected[row][6] = 4
    assert solver(grid) == expected
