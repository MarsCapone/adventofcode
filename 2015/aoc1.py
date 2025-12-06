from utils import input_file, print_results

with input_file(1) as f:
    steps = f.read().strip()

p1 = 0

for step in steps:
    if step == "(":
        p1 += 1
    else:
        p1 -= 1

p2 = None
floor = 0
for i, step in enumerate(steps, start=1):
    floor += 1 if step == "(" else -1
    if floor < 0:
        p2 = i
        break


print_results(p1, p2)