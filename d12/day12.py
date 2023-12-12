from typing import Tuple
from functools import cache
import time


@cache
def count_combinations(line: str, counts: Tuple[int], positions: int, current_count: int, count_pos: int) -> int:
    if positions == len(line):
        ans = 1 if len(counts) == count_pos else 0
    elif line[positions] == "#":
        ans = count_combinations(line, counts, positions + 1, current_count + 1, count_pos)
    elif line[positions] == "." or count_pos == len(counts):
        if count_pos < len(counts) and current_count == counts[count_pos]:
            ans = count_combinations(line, counts, positions + 1, 0, count_pos + 1)
        elif current_count == 0:
            ans = count_combinations(line, counts, positions + 1, 0, count_pos)
        else:
            ans = 0
    else:
        h_count = count_combinations(line, counts, positions + 1, current_count + 1, count_pos)
        d_count = 0
        if current_count == counts[count_pos]:
            d_count = count_combinations(line, counts, positions + 1, 0, count_pos + 1)
        elif current_count == 0:
            d_count = count_combinations(line, counts, positions + 1, 0, count_pos)
        ans = h_count + d_count
    return ans


def part_one(lines: str) -> int:
    lines = lines.splitlines()

    total_valid_combinations = 0
    for row in lines:
        row = row.split()
        counts = [int(x) for x in row[1].split(",")]
        total_valid_combinations += count_combinations(row[0] + ".", tuple(counts), 0, 0, 0)

    return total_valid_combinations


def part_two(lines: str) -> int:
    lines = lines.splitlines()

    total_valid_combinations = 0
    for row in lines:
        row = row.split()
        counts = [int(x) for x in row[1].split(",")] * 5
        total_valid_combinations += count_combinations("?".join([row[0]] * 5) + ".", tuple(counts), 0, 0, 0)

    return total_valid_combinations


def day12():
    with open("d12/input.txt", "r") as file:
        lines = file.read()

    start = time.time()
    answer = part_one(lines)
    print(f"Part one answer = {answer}")
    runtime = time.time() - start
    print(f"Runtime: {runtime} seconds.")

    start = time.time()
    answer = part_two(lines)
    print(f"Part two answer = {answer}")
    runtime = time.time() - start
    print(f"Runtime: {runtime} seconds.")


if __name__ == "__main__":
    day12()
