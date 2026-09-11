def _expand_panel_palette_by_mask(array):
    h, w = len(array), len(array[0])
    for axis in (0, 1):
        if (h, w)[axis] % 2:
            continue
        split = (h, w)[axis] // 2
        if axis == 0:
            panels = (array[:split], array[split:])
        else:
            panels = ([row[:split] for row in array], [row[split:] for row in array])
        monochrome = [
            index
            for index, panel in enumerate(panels)
            if len({value for row in panel for value in row if value != 0}) == 1
        ]
        if len(monochrome) != 1:
            continue
        mask_panel = panels[monochrome[0]]
        palette_panel = panels[1 - monochrome[0]]
        mh, mw = len(mask_panel), len(mask_panel[0])
        return [
            [
                palette_panel[br][bc] if mask_panel[r][c] else 0
                for bc in range(mw)
                for c in range(mw)
            ]
            for br in range(mh)
            for r in range(mh)
        ]
    return [row[:] for row in array]


def solve(grid):
    return _expand_panel_palette_by_mask(grid)
