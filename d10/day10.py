from typing import List, Tuple
from matplotlib.path import Path


lookup = {
    "|": {"n": (0, -1, "n"), "s": (0, 1, "s")},
    "-": {"e": (1, 0, "e"), "w": (-1, 0, "w")},
    "L": {"s": (1, 0, "e"), "w": (0, -1, "n")},
    "J": {"s": (-1, 0, "w"), "e": (0, -1, "n")},
    "7": {"n": (-1, 0, "w"), "e": (0, 1, "s")},
    "F": {"w": (0, 1, "s"), "n": (1, 0, "e")},
}


def make_grid(lines: str) -> List[List[str]]:
    vertical = lines.split("\n")
    grid = [list(line) for line in vertical]
    return grid


def find_starting_position(grid: List[List[str]]) -> Tuple[int, int]:
    for index, line in enumerate(grid):
        if "S" in line:
            return line.index("S"), index


def get_polygon_coords(grid: List[List[str]], start_pos: Tuple[int, int]) -> int:
    dir = "s"
    x, y = (start_pos[0], start_pos[1] + 1)
    polys = [(x, y)]
    while grid[y][x] != "S":
        char = grid[y][x]
        dx, dy, dir = lookup[char][dir]
        x += dx
        y += dy
        polys.append((x, y))
    return polys


def get_length_of_loop(grid: List[List[str]], start_pos: Tuple[int, int]) -> int:
    steps = 1
    dir = "s"
    x, y = (start_pos[0], start_pos[1] + 1)
    while grid[y][x] != "S":
        char = grid[y][x]
        dx, dy, dir = lookup[char][dir]
        x += dx
        y += dy
        steps += 1
    return steps


def part_one(lines: str) -> int:
    grid = make_grid(lines)
    x, y = find_starting_position(grid)
    steps = get_length_of_loop(grid, (x, y))
    return steps // 2


def part_two(lines: str) -> int:
    grid = make_grid(lines)
    x, y = find_starting_position(grid)
    polys = get_polygon_coords(grid, (x, y))
    path = Path(polys)
    tiles = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in polys:
                continue
            if path.contains_point((x, y)):
                tiles += 1
    return tiles


def day10():
    with open("d10/input.txt", "r") as file:
        lines = file.read()

    answer = part_one(lines)
    print(f"Part one answer = {answer}")

    answer = part_two(lines)
    print(f"Part two answer = {answer}")


if __name__ == "__main__":
    day10()
