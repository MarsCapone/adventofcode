from utils import input_file


with input_file(1) as f:
    inp = [(l[0], int(l[1:])) for l in f.readlines()]

current = 50
zeroes = 0

for d, s in inp:
    if d == "L":
        current = (current - s) % 100
    else:
        current = (current + s) % 100
    
    if current == 0:
        zeroes += 1

print(zeroes)