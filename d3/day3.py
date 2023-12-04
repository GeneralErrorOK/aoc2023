from typing import List, Union

SYMBOLS = ["*", "#", "$", "+", "%", "/", "&", "=", "-", "@"]


def get_char_at_index(string: str, index: int) -> Union[str, None]:
    if index < 0:
        return None
    elif index > len(string):
        return None
    else:
        return string[index]


def get_valid_part_numbers(lines: str, line_length: int) -> List:
    part_numbers = []
    candidate_p_nr = []
    for i, c in enumerate(lines):
        if c.isdigit():
            candidate_p_nr.append(c)
            continue
        if c in SYMBOLS and len(candidate_p_nr) == 0:
            continue
        elif c in SYMBOLS and len(candidate_p_nr) > 0:
            parts_number = int("".join(candidate_p_nr))
            part_numbers.append(parts_number)
            candidate_p_nr = []
            continue
        if c == "." and len(candidate_p_nr) > 0:
            parts_nr_length = len(candidate_p_nr)
            parts_number = int("".join(candidate_p_nr))

            cand = get_char_at_index(lines, i - parts_nr_length - 1)
            if cand and cand in SYMBOLS:
                part_numbers.append(parts_number)
                candidate_p_nr = []
                continue

            for j in range(parts_nr_length + 2):
                index_down = (i + line_length) - j
                cand = get_char_at_index(lines, index_down)
                if cand and cand in SYMBOLS:
                    part_numbers.append(parts_number)
                    break

                index_up = (i - line_length) - j
                cand = get_char_at_index(lines, index_up)
                if cand and cand in SYMBOLS:
                    part_numbers.append(parts_number)
                    break
            candidate_p_nr = []
    return part_numbers


def add_or_append_gear_entry(gear_list: dict, gear_index: int, parts_number: int):
    gear_entry = gear_list.get(gear_index)
    if gear_entry:
        gear_entry.append(parts_number)
    else:
        gear_list[gear_index] = [parts_number]


def get_adjacent_to_gears(lines: str, line_length: int) -> List:
    gears = {}
    candidate_p_nr = []
    for i, c in enumerate(lines):
        if c.isdigit():
            candidate_p_nr.append(c)
            continue
        if c == "*" and len(candidate_p_nr) == 0:
            continue
        elif c == "*" and len(candidate_p_nr) > 0:
            parts_number = int("".join(candidate_p_nr))
            add_or_append_gear_entry(gears, i, parts_number)
            candidate_p_nr = []
            continue
        if c == "." and len(candidate_p_nr) > 0:
            parts_nr_length = len(candidate_p_nr)
            parts_number = int("".join(candidate_p_nr))

            index = i - parts_nr_length - 1
            cand = get_char_at_index(lines, index)
            if cand and cand == "*":
                add_or_append_gear_entry(gears, index, parts_number)
                candidate_p_nr = []
                continue

            for j in range(parts_nr_length + 2):
                index_down = (i + line_length) - j
                cand = get_char_at_index(lines, index_down)
                if cand and cand == "*":
                    add_or_append_gear_entry(gears, index_down, parts_number)
                    break

                index_up = (i - line_length) - j
                cand = get_char_at_index(lines, index_up)
                if cand and cand == "*":
                    add_or_append_gear_entry(gears, index_up, parts_number)
                    break
            candidate_p_nr = []
    return gears


def get_gear_ratios(gears: dict) -> List:
    list_of_gear_ratios = []
    for gear_index in gears:
        if len(gears[gear_index]) == 2:
            parts = gears[gear_index]
            list_of_gear_ratios.append(parts[0] * parts[1])
    return list_of_gear_ratios


def day3():
    with open("d3/input1.txt", "r") as file:
        lines = file.read()
    lines = lines.split("\n")
    line_length = len(lines[0])
    lines = "".join(lines)

    part_numbers = get_valid_part_numbers(lines, line_length)
    print(f"Part one: sum of all part numbers = {sum(part_numbers)}")

    adjacent_to_gears = get_adjacent_to_gears(lines, line_length)
    valid_gears = get_gear_ratios(adjacent_to_gears)
    print(f"Part two: sum of all gear ratios = {sum(valid_gears)}")


if __name__ == "__main__":
    day3()
