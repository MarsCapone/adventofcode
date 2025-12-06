from utils import input_file, print_results
from hashlib import md5

with input_file(4) as f:
    code = f.read().strip()


def get_hash(s: str) -> str:
    return md5(string=s.encode()).digest().hex()


n = 1
p1 = p2 = None
while True:
    h = get_hash(f"{code}{n}")
    if h[:5] == "00000":
        if p1 is None:
            p1 = n
        if h[5] == "0":
            p2 = n
            break
    n += 1

    if n % 10_000 == 0:
        print(n)

print_results(p1, p2)
