def part_one(lines: str) -> int:
    return None


def part_two(lines: str) -> int:
    return None


def dayx():
    with open("dx/input.txt", "r") as file:
        lines = file.read()

    answer = part_one(lines)
    print(f"Part one answer = {answer}")

    answer = part_two(lines)
    print(f"Part two answer = {answer}")


if __name__ == "__main__":
    dayx()
