from utils import input_file, print_results
import json

with input_file(12) as f:
    content = json.load(f)


def sum_nums(
    j: dict[str, any] | list[str] | list[int] | int,
    *,
    depth: int = 0,
    ignore_red: bool = False,
) -> int:
    if isinstance(j, int):
        return j

    if isinstance(j, list):
        return sum(sum_nums(v, depth=depth + 1, ignore_red=ignore_red) for v in j)

    if isinstance(j, dict):
        if ignore_red and any(v == "red" for v in j.values()):
            return 0
        return sum(
            sum_nums(v, depth=depth + 1, ignore_red=ignore_red) for v in j.values()
        )

    if isinstance(j, str):
        return 0

    raise Warning(f"What is j? {type(j)}")


p1 = sum_nums(content, ignore_red=False)
p2 = sum_nums(content, ignore_red=True)

print_results(p1, p2)
