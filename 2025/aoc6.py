from utils import print_results, input_file
from operator import add, mul
from functools import reduce

with input_file(6) as f:
    inp = [line.strip("\n") for line in f.readlines()]

ops = {'+': add, '*': mul}
p1 = 0

for calc in zip(*(l.split() for l in inp)):
    op, *nums = reversed(calc)
    p1 += reduce(ops[op], map(int, nums))

# -- 

def get_operations_with_spacing():
    operations_line = inp[-1]
    operations = []
    current_op = operations_line[0]
    space_count = 0
    for c in operations_line[1:]:
        if c == " ":
            space_count += 1
        else:
            operations.append((current_op, space_count))
            current_op = c
            space_count = 0
    
    operations.append((current_op, space_count + 1))
    return operations

p2 = 0

# get each op and the number of characters to read
# for each line, read that many characters
# 3 => ['64 ', '23 ', '314']
# zip => ['623', '431', '  4']
# cast to int and apply op

p2 = 0
start_index = 0
for op, spacing in get_operations_with_spacing():
    next_nums = [l[start_index:start_index+spacing] for l in inp[:-1]]
    start_index += spacing + 1  # account for the space between columns

    new_nums = (int("".join(z).strip()) for z in zip(*next_nums))
    p2 += reduce(ops[op], new_nums)

print_results(p1, p2)
    
