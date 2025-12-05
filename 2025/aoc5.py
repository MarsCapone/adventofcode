from utils import input_file

with input_file(5) as f:
    ranges, ingredients = f.read().split("\n\n")

tuples = [list(map(int, line.split("-"))) for line in ranges.splitlines()]
ranges = [range(a, b+1) for a, b in tuples]
ingredients = set(map(int, ingredients.splitlines()))

fresh = 0

for ing in ingredients:
    if any(ing in r for r in ranges):
        fresh += 1

print("Part 1:", fresh)

sorted_ranges = sorted(tuples, key=tuple)
merged_ranges = [sorted_ranges[0]]

for sr in sorted_ranges[1:]:
    last = merged_ranges[-1]
    
    if sr[0] <= last[1]:
        # push the range outwards
        last[1] = max(last[1], sr[1])
    else:
        # it's a new range
        merged_ranges.append(sr)

total_fresh = sum((rb + 1 - ra) for ra, rb in merged_ranges)
print("Part 2:", total_fresh)