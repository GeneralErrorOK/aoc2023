from typing import List, Tuple
from itertools import combinations
import numpy


def get_empty_space(universe: List[List[str]]) -> Tuple[List[int]]:
    empty_rows = []
    empty_collumns = []
    universe = numpy.array(universe)
    for i, row in enumerate(universe):
        if "#" not in row:
            empty_rows.append(i)
    for i, collumn in enumerate(universe.transpose()):
        if "#" not in collumn:
            empty_collumns.append(i)
    return empty_rows, empty_collumns


def expand_coords(
    galaxy_coords: List[List[int]],
    empty_rows: List[int],
    empty_collumns: List[int],
    expansion_rate: int,
) -> List[List[int]]:
    new_coords = []
    for galaxy in galaxy_coords:
        x, y = galaxy
        mt_c = empty_collumns.copy()
        mt_c.append(x)
        mt_c.sort()
        x = x + (expansion_rate * mt_c.index(x))
        mt_r = empty_rows.copy()
        mt_r.append(y)
        mt_r.sort()
        y = y + (expansion_rate * mt_r.index(y))
        new_coords.append([x, y])
    return new_coords


def get_galaxy_coords(universe: List[List[str]]) -> List[List[int]]:
    coords = []
    for y, row in enumerate(universe):
        for x, c in enumerate(row):
            if c == "#":
                coords.append([x, y])
    return coords


def get_total_distance(galaxy_coords: List) -> int:
    total = 0
    for g1, g2 in combinations(galaxy_coords, 2):
        dx = abs(g2[0] - g1[0])
        dy = abs(g2[1] - g1[1])
        total += dx + dy
    return total


def part_one(lines: str) -> int:
    universe = [list(c) for c in lines.split("\n")]
    coords = get_galaxy_coords(universe)
    mt_r, mt_c = get_empty_space(universe)
    coords = expand_coords(coords, mt_r, mt_c, 1)
    distance = get_total_distance(coords)
    return distance


def part_two(lines: str) -> int:
    universe = [list(c) for c in lines.split("\n")]
    coords = get_galaxy_coords(universe)
    mt_r, mt_c = get_empty_space(universe)
    coords = expand_coords(coords, mt_r, mt_c, 1000000 - 1)
    distance = get_total_distance(coords)
    return distance


def day11():
    with open("d11/input.txt", "r") as file:
        lines = file.read()

    answer = part_one(lines)
    print(f"Part one answer = {answer}")

    answer = part_two(lines)
    print(f"Part two answer = {answer}")


if __name__ == "__main__":
    day11()
