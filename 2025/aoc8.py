from utils import input_file, print_results
from itertools import combinations
from math import pow, sqrt

Coord = tuple[int, int, int]


def dist(c1: Coord, c2: Coord) -> int:
    return sqrt(sum(pow(a - b, 2) for a, b in zip(c1, c2)))


with input_file(8) as f:
    junction_boxes = [
        tuple(map(int, line.strip().split(","))) for line in f.readlines()
    ]


shortest_pairs = sorted(
    (tuple(comb) for comb in combinations(junction_boxes, 2)), key=lambda p: dist(*p)
)

# each index contains a circuit of junction boxes near each other
circuits: list[set[Coord]] = []

# given a junction box, which index of circuits is it in?
circuit_map: dict[Coord, int] = {}

last_connected = None

for i in range(len(shortest_pairs)):
    if i == 1000:
        sorted_lens = sorted([len(c) for c in circuits if c], reverse=True)
        a, b, c = sorted_lens[:3]
        p1 = a * b * c

    a, b = shortest_pairs[i]
    # print()
    # print("> ", a, b)
    # for circ in circuits:
    # print(circ)

    # a and b in the same circuit, no-op
    if a in circuit_map and b in circuit_map and circuit_map[a] == circuit_map[b]:
        # print("same circuit")
        continue

    # a and b seen before, but not in the same circuit. we need to join those circuits
    # but if we just remove at the index, we affect all other indexes
    # so instead, edit in place
    if a in circuit_map and b in circuit_map:
        # print("merging circuits", circuit_map[a], circuit_map[b])
        ca, cb = circuit_map[a], circuit_map[b]

        circuits[ca] = {
            *circuits[ca],
            *circuits[cb],
        }
        # print(">>>", circuits[ca])

        # update the map for b
        for coord in circuits[ca]:
            circuit_map[coord] = ca

        # set b to empty
        circuits[cb] = None
        continue

    last_connected = (a, b)

    # neither a nor b is in circuit_map, then it's a new circuit with just them
    if a not in circuit_map and b not in circuit_map:
        # print("new circuit")
        circuits.append({a, b})
        circuit_map[a] = len(circuits) - 1
        circuit_map[b] = len(circuits) - 1
        continue

    # only a is seen before
    if a in circuit_map and b not in circuit_map:
        # print("add b to a")
        circuits[circuit_map[a]].add(b)
        circuit_map[b] = circuit_map[a]
        continue

    # only b is seen before
    if b in circuit_map and a not in circuit_map:
        # print("add a to b")
        circuits[circuit_map[b]].add(a)
        circuit_map[a] = circuit_map[b]
        continue

    # else - idk what case is this
    raise Warning("what case is this?!")


p2 = last_connected[0][0] * last_connected[1][0]

print_results(p1, p2)
