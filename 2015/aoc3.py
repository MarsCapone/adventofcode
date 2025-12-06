from utils import input_file, print_results

with input_file(3) as f:
    directions = f.read().strip()

current = 0 + 0j
seen = {current}

DIR = {"^": 1, "v": -1, ">": 1j, "<": -1j}

for direction in directions:
    current += DIR[direction]
    seen.add(current)

p1 = len(seen)

print_results(p1, None)