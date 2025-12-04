from utils import input_file
from itertools import product

with input_file(4) as f:
    inp = [list(line.strip()) for line in f.readlines()]

total = 0
xs = []

positions = tuple(p for p in product([0, 1, -1], repeat=2) if p != (0, 0))

def safe_coord(grid: list[tuple[str, ...]], ri: int, ci: int) -> str | None:
    if 0 <= ri < len(grid) and 0 <= ci < len(grid[ri]):
        return grid[ri][ci]
    return None

rows = len(inp)
cols = len(inp[0])

for ri, row in enumerate(inp):
    for ci, val in enumerate(inp[ri]):
        if val != "@":
            # not a roll, so we don't care
            continue

        neighboring_rolls = 0
        for pos in positions:
            neighbour_coord = tuple(map(sum, zip((ri, ci), pos)))
            neighbour = safe_coord(inp, *neighbour_coord)
            if neighbour and neighbour == "@":
                neighboring_rolls += 1
    
        if neighboring_rolls < 4:
            total += 1
            xs.append((ri, ci))

for r, c in xs:
    inp[r][c] = "x"


# print("\n".join("".join(line) for line in inp))

print(total)





