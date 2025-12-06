from utils import input_file, print_results
import re

with input_file(5) as f:
    lines = [line.strip() for line in f.readlines()]

forbidden_strings = ("ab", "cd", "pq", "xy")
vowels = set("aeiou")


def is_nice(s: str) -> bool:
    if any(f in s for f in forbidden_strings):
        return False

    vs = [c for c in s if c in vowels]
    if len(vs) < 3:
        return False

    pairs = [(s[i], s[i + 1]) for i in range(len(s) - 1)]
    if all(a != b for a, b in pairs):
        return False

    return True


rep = re.compile(r"(.)(.).*\1\2")
alt = re.compile(r"(.).\1")


def is_nice2(s: str) -> bool:
    if not rep.search(s):
        return False
    if not alt.search(s):
        return False
    return True


p1 = p2 = 0
for line in lines:
    if is_nice(line):
        p1 += 1
    if is_nice2(line):
        p2 += 1

print_results(p1, p2)
