from utils import input_file, print_results

with input_file(3) as f:
    directions = f.read().strip()

current = 0 + 0j
seen = {current}
santa = 0 + 0j
robot = 0 + 0j
seen2 = {robot, santa}
is_santa = True

DIR = {"^": 1, "v": -1, ">": 1j, "<": -1j}


for direction in directions:
    current += DIR[direction]
    seen.add(current)

    if is_santa:
        santa += DIR[direction]
    else:
        robot += DIR[direction]
    is_santa = not is_santa
    seen2.add(robot)
    seen2.add(santa)


p1 = len(seen)
p2 = len(seen2)

print_results(p1, p2)
