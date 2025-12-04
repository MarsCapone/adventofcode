from utils import input_file
from itertools import product
from typing import Iterable
from collections import Counter

with input_file(4) as f:
    inp = [list(line.strip()) for line in f.readlines()]

Grid = list[list[str]]

POSITIONS = tuple(p for p in product([0, 1, -1], repeat=2) if p != (0, 0))

def neighbours_of_cell(grid: Grid, cell: tuple[int, int]) -> Iterable[str]:
    neighbour_coords = [tuple(map(sum, zip(cell, pos))) for pos in POSITIONS]
    return filter(None, (safe_coord(grid, *coord) for coord in neighbour_coords))


def safe_coord(grid: Grid, ri: int, ci: int) -> str | None:
    if 0 <= ri < len(grid) and 0 <= ci < len(grid[ri]):
        return grid[ri][ci]
    return None

rows = len(inp)
cols = len(inp[0])

def remove_rolls(grid: list[list[str]]) -> tuple[int, list[list[str]]]:
    # return the number removed and the new grid
    total = 0
    xs = []

    # copy the grid so we can modify
    grid = [[l for l in line] for line in grid]

    for ri in range(len(grid)):
        for ci, val in enumerate(grid[ri]):
            if val != "@":
                # not a roll, so we don't care
                continue

            neighbours = Counter(neighbours_of_cell(grid, (ri, ci)))
            neighboring_rolls = neighbours["@"]
        
            if neighboring_rolls < 4:
                total += 1
                xs.append((ri, ci))

    for r, c in xs:
        grid[r][c] = "x"
    
    return total, grid

total = 0
removed, grid = remove_rolls(inp)

print("Part 1:", removed)

while removed > 0:
    total += removed
    removed, grid = remove_rolls(grid)    

print("Part 2:", total)




