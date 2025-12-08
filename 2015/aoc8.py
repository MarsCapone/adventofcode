from utils import input_file, print_results

with input_file(8) as f:
    inp = [line.strip() for line in f.readlines()]

p1 = p2 = 0
for line in inp:
    p1 += len(line) - len(eval(line))
    p2 += 2 + line.count("\\") + line.count('"')

print_results(p1, p2)
