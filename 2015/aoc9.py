from utils import input_file, print_results
import re
from itertools import permutations

P = re.compile(r"^(.+) to (.+) = (\d+)$")

with input_file(9) as f:
    lines = [P.search(line.strip()).groups() for line in f.readlines()]

routes = {frozenset({a, b}): int(c) for a, b, c in lines}

all_places = frozenset.union(*routes.keys())

shortest = 99e99
longest = 0

for perm in permutations(all_places):
    perm = tuple(perm)
    dist = sum([routes[frozenset(edge)] for edge in zip(perm, perm[1:])])
    shortest = min(shortest, dist)
    longest = max(longest, dist)


print_results(shortest, longest)
