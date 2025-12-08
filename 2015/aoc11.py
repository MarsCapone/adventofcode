from utils import input_file, print_results
from typing import Iterator
import string
import re

with input_file(11) as f:
    start = f.read().strip()

b26_translation = (
    string.ascii_lowercase,  # passwords alphabet
    string.digits + string.ascii_lowercase[:16],  # base26
)


def b26int_to_code(n: int) -> str:
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % 26))
        n //= 26
    return "".join(b26_translation[0][i] for i in digits[::-1])


def gen_codes(start: str) -> Iterator[str]:
    i = 1
    val = int(start.translate(str.maketrans(*b26_translation)), 26)
    while True:
        yield b26int_to_code(val + i)
        i += 1


STRAIGHTS = {
    "".join(z)
    for z in zip(
        string.ascii_lowercase, string.ascii_lowercase[1:], string.ascii_lowercase[2:]
    )
}


def is_valid(code: str) -> bool:
    if any(c in code for c in "iol"):
        return False

    if not any(s in code for s in STRAIGHTS):
        return False

    if not re.search(r"^.*(.)\1.*(.)\2.*$", code):
        return False

    return True


gen = gen_codes(start)

while True:
    p1 = next(gen)
    if is_valid(p1):
        break


while True:
    p2 = next(gen)
    if is_valid(p2):
        break

print_results(p1, p2)
