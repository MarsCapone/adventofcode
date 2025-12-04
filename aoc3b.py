from utils import input_file
from collections import defaultdict

with input_file(3) as f:
    inp = [list(map(int, line.strip())) for line in f.readlines()]

total = 0

def find_best(bank: list[int], goal: int) -> tuple[int, int]:
    found = []
    remaining = len(bank) - goal

    for j in bank:
        # anything starting with j+1 is going to be bigger than something starting j
        # so start with the first number being j. add the next number whilst there is a next number to add.
        # and if there isn't or j is bigger than the previous number, and there are numbers remaining, restart.
        # print(remaining, found)
        while found and remaining > 0 and found[-1] < j:
            found.pop()
            remaining -= 1
            # print(">", remaining, found)
        found.append(j)
    
    # print(found)

    joltage = 0
    for m, i in enumerate(reversed(found[:goal])):
        joltage +=  i * pow(10, m)
    
    return joltage
        
for bank in inp:
    v = find_best(bank, 12)
    # print(v)
    total += v

print(total)