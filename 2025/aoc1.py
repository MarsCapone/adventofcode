from utils import input_file, print_results

with input_file(1) as f:
    inp = [(l[0], int(l[1:])) for l in f.readlines()]

current = 50
zeroes = 0
passes = 0

for d, step in inp:
    mul = -1 if d == "L" else 1

    for i in range(step):
        current += mul
    
        current %= 100
        if current == 0:
            passes += 1
    
    if current == 0:
        zeroes += 1

print_results(zeroes, passes)