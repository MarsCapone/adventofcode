from utils import input_file, print_results
from collections import defaultdict

with input_file(7) as f:
    instructions = [line.strip().split(" -> ") for line in f.readlines()]

signals = defaultdict(int)
actions = {
    "NOT": lambda i: (1 << 16) - 1 - i,
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "LSHIFT": lambda a, b: a << b,
    "RSHIFT": lambda a, b: a >> b,
}


def int_or_var(n: str) -> int:
    if n.isdigit():
        return int(n)
    return signals[n]


for command, output in instructions:
    # print(signals)
    parts = command.split()
    if len(parts) == 1:
        signals[output] = int_or_var(parts[0])

    if len(parts) == 2:
        not_, var = parts
        assert not_ == "NOT"
        signals[output] = actions["NOT"](int_or_var(var))

    if len(parts) == 3:
        a, action, b = parts
        assert action in actions
        signals[output] = actions[action](int_or_var(a), int_or_var(b))

print(signals)

p1 = signals["a"] if "a" in signals else None

print_results(p1, None)
