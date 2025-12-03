import sys
from utils import input_file

with input_file(2) as f:
    inp = "".join([l.strip() for l in f.readlines() if l.strip()])

id_ranges = [tuple(map(int, r.split("-"))) for r in inp.split(",")]

# print(id_ranges)

def is_valid_id(s: str | int) -> bool:
    s = str(s).lstrip("0")
    mid = len(s) // 2
    return s[:mid] != s[mid:]

c = 0
for a, b in id_ranges:
    for i in range(a, b+1):
        if not is_valid_id(i):
            c += i

print(c)