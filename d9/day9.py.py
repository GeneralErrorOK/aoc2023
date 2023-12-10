from typing import List


def get_difference_list(working_set: List[int]) -> List[int]:
    differences = []
    for index, number in enumerate(working_set):
        if index == len(working_set) - 1:
            break
        differences.append(working_set[index + 1] - number)
    return differences


def next_number(history: List[int], forwards: bool = True) -> int:
    if not forwards:
        history.reverse()
    operations = [history[-1]]
    while sum(history) != 0:
        history = get_difference_list(history)
        operations.append(history[-1])
    operations.reverse()
    next_number = 0
    for index in range(1, len(operations)):
        next_number = next_number + operations[index]
    return next_number


def part_one(lines: str) -> int:
    lines = lines.split("\n")
    total = 0
    for line in lines:
        total += next_number([int(x) for x in line.split()])
    return total


def part_two(lines: str) -> int:
    lines = lines.split("\n")
    total = 0
    for line in lines:
        total += next_number([int(x) for x in line.split()], forwards=False)
    return total


def day9():
    with open("d9/input.txt", "r") as file:
        lines = file.read()

    answer = part_one(lines)
    print(f"Part one answer = {answer}")

    answer = part_two(lines)
    print(f"Part two answer = {answer}")


if __name__ == "__main__":
    day9()
