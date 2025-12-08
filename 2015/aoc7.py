from utils import input_file, print_results
from collections import defaultdict

with input_file(7) as f:
    instructions = [tuple(line.strip().split(" -> ")) for line in f.readlines()]

actions = {
    "NOT": lambda i: (1 << 16) - 1 - i,
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "LSHIFT": lambda a, b: a << b,
    "RSHIFT": lambda a, b: a >> b,
}


def int_or_var(signals: dict[str, int | None], n: str) -> int | None:
    if n.isdigit():
        return int(n)
    return signals[n]


def resolve(signals: dict[str, int | None], command: str) -> int | None:
    parts = command.split()
    if len(parts) == 1:
        return int_or_var(signals, parts[0])

    if len(parts) == 2:
        not_, var = parts
        assert not_ == "NOT"
        if (v := int_or_var(signals, var)) is None:
            return None
        return actions["NOT"](v)

    if len(parts) == 3:
        a, action, b = parts
        assert action in actions
        if (av := int_or_var(signals, a)) is None or (
            bv := int_or_var(signals, b)
        ) is None:
            return None
        return actions[action](av, bv)

    return None


def eval_wires(
    initial_signals: dict[str, int],
    search_value: str,
) -> dict[str, int | None]:
    signals = defaultdict(lambda: None)
    signals.update(initial_signals.copy())
    insts = set(instructions)

    while signals[search_value] is None or insts:
        for command, outvar in insts:
            if outvar in initial_signals and command.isdigit():
                continue
            output = resolve(signals, command)
            if output is not None:
                signals[outvar] = output
                insts.remove((command, outvar))
                break
    return signals


p1_signals = eval_wires({}, "a")
p1 = p1_signals["a"]
print(p1_signals["b"])

p2_signals = eval_wires({"b": p1}, "a")
p2 = p2_signals["a"]

print_results(p1, p2)
