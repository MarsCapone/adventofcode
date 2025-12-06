from functools import reduce
from io import FileIO
import sys
from pathlib import Path
from contextlib import contextmanager
from typing import Generator

def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


@contextmanager
def input_file(n: int) -> Generator[FileIO]:
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        filename = f"{n}.test.txt"
    else:
        filename = f"{n}.txt"
    
    p = Path(filename)
    with p.open() as f:
        yield f


def print_results(part1: any, part2: any) -> None:
    print("Part 1:", part1)
    print("Part 2:", part2)