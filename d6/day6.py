from functools import reduce
from typing import List


def calculate_distance(time_pressed: int, total_time: int) -> int:
    return time_pressed * (total_time - time_pressed)


def calculate_options(times: List[int], distances: List[int]) -> int:
    race_options = []
    for race in zip(times, distances):
        options = 0
        for i in range(race[0] + 1):
            if calculate_distance(i, race[0]) > race[1]:
                options += 1
        race_options.append(options)
    return reduce(lambda x, y: x * y, race_options)


def part_one(lines: str) -> int:
    split_lines = lines.split("\n")
    times = [int(x) for x in split_lines[0].split(":")[1].split()]
    distances = [int(x) for x in split_lines[1].split(":")[1].split()]
    return calculate_options(times, distances)


def part_two(lines: str) -> int:
    split_lines = lines.split("\n")
    times = [x for x in split_lines[0].split(":")[1].split()]
    distances = [x for x in split_lines[1].split(":")[1].split()]
    time = "".join(times)
    distance = "".join(distances)
    return calculate_options([int(time)], [int(distance)])


def day6():
    with open("d6/input.txt", "r") as file:
        lines = file.read()

    answer = part_one(lines)
    print(f"Part one answer = {answer}")

    answer = part_two(lines)
    print(f"Part two answer = {answer}")


if __name__ == "__main__":
    day6()
