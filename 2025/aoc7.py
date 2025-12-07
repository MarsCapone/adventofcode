from utils import input_file, print_results
from functools import reduce, lru_cache

with input_file(7) as f:
    lines = [line.strip() for line in f.readlines()]

Coord = tuple[int, int]


def parse(lines: list[str]) -> tuple[Coord, set[Coord]]:
    start = None
    splitters = set()
    for r, line in enumerate(lines):
        for c, val in enumerate(line):
            coord = (r, c)
            if val == "S":
                start = coord
            elif val == "^":
                if c == 0 or c == len(line) - 1:
                    raise Warning("need to handle splitters on the edge")
                splitters |= {coord}
    return start, splitters


def addc(*a: Coord) -> Coord:
    return reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), a)


start, splitters = parse(lines)

DOWN, LEFT, RIGHT = (1, 0), (0, -1), (0, 1)


def find_seen_splitters(start: Coord) -> set[Coord]:
    latest_tachyons = {addc(start, DOWN)}
    seen_splitters = set()

    while any(tr < len(lines) for tr, _ in latest_tachyons):
        next_tachyons = {addc(t, DOWN) for t in latest_tachyons}
        overlapping_splitters = next_tachyons & splitters

        # remove the ones that are in the positions of splitters
        next_tachyons -= overlapping_splitters
        # add the new ones left and right of any found splitters
        next_tachyons |= {addc(os, LEFT) for os in overlapping_splitters} | {
            addc(os, RIGHT) for os in overlapping_splitters
        }

        seen_splitters |= overlapping_splitters
        latest_tachyons = next_tachyons

    return seen_splitters


@lru_cache(None)
def find_splitter_timelines(max_depth: int, start: Coord) -> int:
    if max_depth < 0:
        return 0

    if start in splitters:
        return (
            1
            + find_splitter_timelines(max_depth - 1, addc(start, LEFT, DOWN))
            + find_splitter_timelines(max_depth - 1, addc(start, RIGHT, DOWN))
        )
    else:
        return find_splitter_timelines(max_depth - 1, addc(start, DOWN))


p1 = len(find_seen_splitters(start))
p2 = 1 + find_splitter_timelines(len(lines), start)


print_results(p1, p2)
