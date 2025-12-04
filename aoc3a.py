from utils import input_file

with input_file(3) as f:
    inp = [list(map(int, line.strip())) for line in f.readlines()]

total = 0

def find_best(bank: list[int]) -> tuple[int, int]:
    best =  0
    for i, a in enumerate(bank):
        for b in bank[i+1:]:
            n = a * 10 + b
            if n > best:
                best = n
        if a * 10 < best:
            continue
    return best
        
for bank in inp:
    v = find_best(bank)
    # print(v)
    total += v

print(total)