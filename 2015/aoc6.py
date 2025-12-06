from utils import input_file, print_results
import re
from typing import Callable, TypeVar

with input_file(6) as f:
    lines = [line.strip() for line in f.readlines()]

pat = re.compile(r"([\w ]+) (\d+),(\d+) through (\d+),(\d+)")

actions = {
    "turn on": lambda i: True,
    "turn off": lambda i: False,
    "toggle": lambda i: not i,
}

actions2 = {
    "turn on": lambda i: i + 1,
    "turn off": lambda i: max(0, i - 1),
    "toggle": lambda i: i + 2,
}

GridType = TypeVar("GridType")


def run_commands(
    actions: dict[str, Callable[[GridType], GridType]], grid_value: GridType
) -> list[list[GridType]]:
    grid = [[grid_value for _ in range(1000)] for _ in range(1000)]

    for line in lines:
        search = pat.search(line)
        if not search:
            print(line)
            break
        a, *nums = search.groups()
        x1, y1, x2, y2 = map(int, nums)

        for r in range(y1, y2 + 1):
            for c in range(x1, x2 + 1):
                grid[r][c] = actions[a](grid[r][c])
    return grid


p1_grid = run_commands(actions, False)
p2_grid = run_commands(actions2, 0)

p1 = 0
for row in p1_grid:
    for val in row:
        if val:
            p1 += 1

p2 = sum(sum(row) for row in p2_grid)


print_results(p1, p2)
