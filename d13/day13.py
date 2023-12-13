import time
from typing import List, Union
import numpy as np


def create_list_of_grids(lines: List[str]) -> List[np.ndarray]:
    grids_list = []
    grid = []
    for line in lines:
        if line == "":
            grids_list.append(np.asarray(grid))
            grid = []
            continue
        grid.append([1 if c == "#" else 0 for c in line])
    grids_list.append(np.asarray(grid))
    return grids_list


def is_symmetric(grid: np.ndarray, ti: int, bi: int, dif: int = 0) -> bool:
    if dif < 0:
        return False
    dif = dif - sum(np.bitwise_xor(grid[ti], grid[bi]))
    if ti == 0 or bi == len(grid) - 1:
        if dif == 0:
            return True
        else:
            return False
    if dif >= 0:
        return is_symmetric(grid, ti - 1, bi + 1, dif)
    else:
        return False


def find_symmetry(grid: np.ndarray, max_dif: int = 0) -> Union[int, None]:
    for i in range(len(grid) - 1):
        if is_symmetric(grid, i, i + 1, max_dif):
            return i + 1
    else:
        return None


def part_one(lines: str) -> int:
    grids = create_list_of_grids(lines)
    score = 0
    for grid in grids:
        horizontal = find_symmetry(grid)
        if horizontal:
            score += 100 * horizontal
        vertical = find_symmetry(grid.T)
        if vertical:
            score += vertical
    return score


def part_two(lines: str) -> int:
    grids = create_list_of_grids(lines)
    score = 0
    for grid in grids:
        horizontal = find_symmetry(grid, 1)
        if horizontal:
            score += 100 * horizontal
        vertical = find_symmetry(grid.T, 1)
        if vertical:
            score += vertical
    return score


def day13():
    with open("d13/input.txt", "r") as file:
        lines = file.read()
        lines = lines.splitlines()

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
    day13()
