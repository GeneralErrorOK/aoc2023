import time
from typing import List
import numpy as np


def sort_line(line: List[str]) -> List[str]:
    for i, c in enumerate(line):
        j = i
        if c == "O":
            line[i] = "."
            while j > 0 and line[j - 1] != "O" and line[j - 1] != "#":
                j -= 1
            line[j] = c
            continue
    return line


def sort_all_lines(grid: np.ndarray) -> np.ndarray:
    for line in grid:
        line = sort_line(line)
    return grid[:]


def cycle_grid(grid: np.ndarray) -> np.ndarray:
    # north (rotate 90 degrees ccw)
    grid = sort_all_lines(np.rot90(grid, 1))

    # west - rotate 270 degrees ccw
    grid = sort_all_lines(np.rot90(grid, 3))

    # south - rotate 270 degrees ccw
    grid = sort_all_lines(np.rot90(grid, 3))

    # east - rotate 270 degrees ccw
    grid = sort_all_lines(np.rot90(grid, 3))

    # reset grid to original position - rotate 180
    restored_grid = np.rot90(grid, 2)
    return restored_grid


def score_of_line(line: List[str]) -> int:
    total = 0
    for i, c in enumerate(line):
        if c == "O":
            total += len(line) - i
    return total


def part_one(lines: str) -> int:
    grid = []
    for line in lines:
        grid.append([c for c in line])
    grid = np.asarray(grid)
    print()
    answer = 0
    for line in np.rot90(grid, 1):
        answer += score_of_line(sort_line(line))

    return answer


def part_two(lines: str) -> int:
    grid = []
    for line in lines:
        grid.append([c for c in line])
    grid = np.asarray(grid)

    cycle_period = None
    cycled_grids = []
    for i in range(300):
        grid = cycle_grid(grid)
        cycled_grids.append(grid.copy())

        if not cycle_period:
            for j, old_grid in enumerate(cycled_grids):
                if j != i and np.array_equal(grid, old_grid):
                    cycle_period = i - j
        elif (1000000000 - (i + 1)) % cycle_period == 0:
            answer = 0
            for line in np.rot90(grid, 1):
                answer += score_of_line(line)
            break

    return answer


def day14():
    with open("d14/input.txt", "r") as file:
        lines = file.read()
        lines = lines.splitlines()

    answer = part_one(lines)
    print(f"Part one answer = {answer}")

    answer = part_two(lines)
    print(f"Part two answer = {answer}")


if __name__ == "__main__":
    day14()
