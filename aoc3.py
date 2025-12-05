from utils import input_file, print_results

with input_file(3) as f:
    inp = [list(map(int, line.strip())) for line in f.readlines()]

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
        found.append(j)

    joltage = 0
    for m, i in enumerate(reversed(found[:goal])):
        joltage +=  i * pow(10, m)
    
    return joltage

p1 = p2 = 0

for bank in inp:
    p1 += find_best(bank, 2)
    p2 += find_best(bank, 12)

print_results(p1, p2)