from utils import input_file, factors, print_results

with input_file(2) as f:
    inp = "".join([l.strip() for l in f.readlines() if l.strip()])

id_ranges = [tuple(map(int, r.split("-"))) for r in inp.split(",")]

def is_valid_id_2(s: str | int) -> bool:
    s = str(s).lstrip("0")
    mid = len(s) // 2
    return s[:mid] != s[mid:]

def is_valid_id_any(s: str | int) -> bool:
    s = str(s).lstrip("0")
    length_factors = factors(len(s))
    for lf in length_factors:
        m = len(s) // lf
        parts = [p for p in (s[m*i:m*(i+1)] for i in range(lf+1)) if p]
        setparts = set(parts)
        if len(parts) > 1 and len(setparts) == 1:
            return False
    return True

p1 = p2 = 0
for a, b in id_ranges:
    for i in range(a, b+1):
        if not is_valid_id_2(i):
            p1 += i
        if not is_valid_id_any(i):
            p2 += i

print_results(p1, p2)