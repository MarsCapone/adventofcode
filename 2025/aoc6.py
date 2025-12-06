from utils import print_results, input_file
from operator import add, mul
from functools import reduce

with input_file(6) as f:
    inp = [line.strip().split() for line in f.readlines()]

ops = {'+': add, '*': mul}
p1 = 0

for calc in zip(*inp):
    op, *nums = reversed(calc)
    p1 += reduce(ops[op], map(int, nums))





print_results(p1, None)
    


