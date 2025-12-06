from utils import input_file, print_results
from itertools import combinations

with input_file(2) as f:
    dims = [tuple(map(int, line.split("x"))) for line in f.readlines()]

p1 = p2 = 0
for dim in dims:
    areas, perimeters = zip(*((a * b, 2 * (a + b)) for a, b in combinations(dim, 2)))
    
    p1 += 2 * sum(areas) + min(areas)

    x, y, z = dim
    p2 += min(perimeters) + x * y * z


print_results(p1, p2)