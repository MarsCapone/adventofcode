from utils import input_file, print_results

with input_file(10) as f:
    inp = f.read().strip()


def look_and_say(string: str) -> str:
    res = ""
    last, count = string[0], 1
    for s in string[1:]:
        if s == last:
            count += 1
        else:
            res += str(count) + last
            last, count = s, 1

    res += str(count) + last
    return res


current = inp
p1 = p2 = 0

for _ in range(40):
    current = look_and_say(current)

p1 = current

for _ in range(10):
    current = look_and_say(current)

p2 = current

print_results(len(p1), len(p2))
