import pytest

from arc_agi_2_atlas.types import normalize_grid


@pytest.mark.parametrize(
    "value",
    [[], [[0], []], [[0], [0, 1]], [[-1]], [[10]], [[True]], "not a grid"],
)
def test_normalize_grid_rejects_invalid_grids(value: object) -> None:
    with pytest.raises(ValueError):
        normalize_grid(value)


def test_normalize_grid_copies_valid_grid() -> None:
    source = [[0, 1], [2, 3]]
    result = normalize_grid(source)
    assert result == source
    assert result is not source
