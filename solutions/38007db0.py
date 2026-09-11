def _select_unique_repeated_panel_by_rows(array):
    if len(array[0]) < 3:
        return [r[:] for r in array]
    period = None
    for candidate in range(1, len(array[0]) // 2 + 1):
        total = len(array) * (len(array[0]) - candidate)
        same = sum(
            array[r][c] == array[r][c + candidate]
            for r in range(len(array))
            for c in range(len(array[0]) - candidate)
        )
        if same / total > 0.9:
            period = candidate
            break
    if period is None:
        return [r[:] for r in array]
    starts = list(range(0, len(array[0]) - period, period))
    if len(starts) < 2:
        return [r[:] for r in array]
    output = []
    for row in range(len(array)):
        windows = [
            tuple(int(value) for value in array[row][start : start + period + 1])
            for start in starts
        ]
        counts: dict[tuple[int, ...], int] = {}
        for window in windows:
            counts[window] = counts.get(window, 0) + 1
        unique = [window for window in windows if counts[window] == 1]
        selected = unique[0] if len(unique) == 1 else max(counts, key=lambda window: counts[window])
        output.append(list(selected))
    return output


def solve(grid):
    return _select_unique_repeated_panel_by_rows(grid)
