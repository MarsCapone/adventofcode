from utils import input_file, print_results
import re
from itertools import chain, permutations
from collections import defaultdict
from typing import Iterable

P = re.compile(
    r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)."
)

test = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

with input_file(13) as f:
    ts = [tuple(P.search(line.strip()).groups()) for line in f.readlines()]
    # ts = [tuple(P.search(line.strip()).groups()) for line in test.splitlines()]
    people = set(chain.from_iterable((a, b) for a, *_, b in ts))
    pairs = defaultdict(int)
    pairs.update({(a, b): int(q) * (1 if m == "gain" else -1) for a, m, q, b in ts})


p1 = 0


def get_best(people: Iterable[str]) -> int:
    best = 0
    for perm in permutations(people):
        neighbours = set(zip(perm, perm[1:] + (perm[0],)))
        neighbours |= {tuple(reversed(z)) for z in neighbours}
        score = sum(pairs[n] for n in neighbours)
        best = max(best, score)
    return best


p1 = get_best(people)
p2 = get_best(people | {"Samson"})

print_results(p1, p2)
