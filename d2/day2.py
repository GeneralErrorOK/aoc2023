class CubeDraw:
    def __init__(self, blue: int, red: int, green: int) -> None:
        self.blue = blue
        self.red = red
        self.green = green

    def is_valid(self, blue_limit: int, red_limit: int, green_limit: int) -> bool:
        return (
            blue_limit >= self.blue
            and red_limit >= self.red
            and green_limit >= self.green
        )


class CubeGame:
    def __init__(self, game_number: int) -> None:
        self.id = game_number
        self.draws = []

    def add_draw(self, draw: CubeDraw):
        self.draws.append(draw)

    def all_draws_are_valid(
        self, blue_limit: int, red_limit: int, green_limit: int
    ) -> bool:
        valid = True
        for draw in self.draws:
            valid = draw.is_valid(blue_limit, red_limit, green_limit)
            if not valid:
                break
        return valid

    def power(self) -> int:
        max_blue = max_red = max_green = 0
        for draw in self.draws:
            if draw.blue > max_blue:
                max_blue = draw.blue
            if draw.red > max_red:
                max_red = draw.red
            if draw.green > max_green:
                max_green = draw.green
        return max_blue * max_red * max_green


def create_cube_game(elf_record_line: str) -> CubeGame:
    game_id = int(elf_record_line.split(":")[0].split(" ")[1])
    cubegame = CubeGame(game_id)
    clean_elf_record_line = elf_record_line.replace(",", " ")
    draws = clean_elf_record_line.split(";")
    for draw in draws:
        split_draw = draw.split()
        try:
            blue_count = int(split_draw[split_draw.index("blue") - 1])
        except ValueError:
            blue_count = 0
        try:
            red_count = int(split_draw[split_draw.index("red") - 1])
        except ValueError:
            red_count = 0
        try:
            green_count = int(split_draw[split_draw.index("green") - 1])
        except ValueError:
            green_count = 0
        cubegame.add_draw(CubeDraw(blue_count, red_count, green_count))
    return cubegame


def day2() -> (int, int):
    sum_of_possible_games = 0
    sum_of_game_powers = 0
    with open("d2/input1.txt", "r") as file:
        elf_game_record = file.read()
    for elf_record_line in elf_game_record.split("\n"):
        cubegame = create_cube_game(elf_record_line)
        if cubegame.all_draws_are_valid(blue_limit=14, red_limit=12, green_limit=13):
            sum_of_possible_games += cubegame.id
        sum_of_game_powers += cubegame.power()
    return (sum_of_possible_games, sum_of_game_powers)


if __name__ == "__main__":
    part_one, part_two = day2()
    print(f"Part one: sum of valid game numbers = {part_one}")
    print(f"Part two: sum of all game powers = {part_two}")
