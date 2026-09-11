def solve(grid):
    h, w = len(grid), len(grid[0])
    remaining = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2}
    blocks = []
    while remaining:
        seed = min(remaining)
        remaining.remove(seed)
        stack = [seed]
        component = [seed]
        while stack:
            r, c = stack.pop()
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (nr, nc) in remaining:
                    remaining.remove((nr, nc))
                    stack.append((nr, nc))
                    component.append((nr, nc))
        blocks.append(set(component))
    if len(blocks) != 2 or any(
        len(block) != 4 or len({r for r, _ in block}) != 2 or len({c for _, c in block}) != 2
        for block in blocks
    ):
        return [[0]]
    if any(
        block != {(r, c) for r in {r for r, _ in block} for c in {c for _, c in block}}
        for block in blocks
    ):
        return [[0]]
    traversable = {(r, c) for r in range(h) for c in range(w) if grid[r][c] in (2, 8)}
    stack = list(blocks[0])
    seen = set(blocks[0])
    while stack:
        r, c = stack.pop()
        if (r, c) in blocks[1]:
            return [[8]]
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if (nr, nc) in traversable and (nr, nc) not in seen:
                seen.add((nr, nc))
                stack.append((nr, nc))
    return [[0]]
