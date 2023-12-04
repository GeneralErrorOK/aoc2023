from typing import List, Union

SYMBOLS = ["*", "#", "$", "+", "%", "/", "&", "=", "-", "@"]


def get_char_at_index(string: str, index: int) -> Union[str, None]:
    if index < 0 or index > len(string):
        return None
    else:
        return string[index]


def add_or_append_part_number(parts_list: dict, symbol_index: int, parts_number: int):
    parts_entry = parts_list.get(symbol_index)
    if parts_entry:
        parts_entry.append(parts_number)
    else:
        parts_list[symbol_index] = [parts_number]


def get_part_numbers_adjacent_to_symbols(
    lines: str, line_length: int, symbols: List[str]
) -> List:
    parts = {}
    candidate_p_nr = []
    for i, c in enumerate(lines):
        if c.isdigit():
            candidate_p_nr.append(c)
            continue
        if c in symbols and len(candidate_p_nr) == 0:
            continue
        elif c in symbols and len(candidate_p_nr) > 0:
            parts_number = int("".join(candidate_p_nr))
            add_or_append_part_number(parts, i, parts_number)
            candidate_p_nr = []
            continue
        if c == "." and len(candidate_p_nr) > 0:
            parts_nr_length = len(candidate_p_nr)
            parts_number = int("".join(candidate_p_nr))

            index = i - parts_nr_length - 1
            cand = get_char_at_index(lines, index)
            if cand and cand in symbols:
                add_or_append_part_number(parts, index, parts_number)
                candidate_p_nr = []
                continue

            for j in range(parts_nr_length + 2):
                index_down = (i + line_length) - j
                cand = get_char_at_index(lines, index_down)
                if cand and cand in symbols:
                    add_or_append_part_number(parts, index_down, parts_number)
                    break

                index_up = (i - line_length) - j
                cand = get_char_at_index(lines, index_up)
                if cand and cand in symbols:
                    add_or_append_part_number(parts, index_up, parts_number)
                    break
            candidate_p_nr = []
    return parts


def get_gear_ratios(gears: dict) -> List:
    list_of_gear_ratios = []
    for gear_index in gears:
        if len(gears[gear_index]) == 2:
            parts = gears[gear_index]
            list_of_gear_ratios.append(parts[0] * parts[1])
    return list_of_gear_ratios


def get_sum_of_all_parts(parts_list: dict) -> int:
    sum_part_nrs = 0
    for symbol in parts_list:
        for part_number in parts_list[symbol]:
            sum_part_nrs += part_number
    return sum_part_nrs


def day3():
    with open("d3/input1.txt", "r") as file:
        lines = file.read()
    lines = lines.split("\n")
    line_length = len(lines[0])
    lines = "".join(lines)

    all_symbols = get_part_numbers_adjacent_to_symbols(lines, line_length, SYMBOLS)
    part_numbers = get_sum_of_all_parts(all_symbols)
    print(f"Part one: sum of all part numbers = {part_numbers}")

    adjacent_to_gears = get_part_numbers_adjacent_to_symbols(lines, line_length, ["*"])
    valid_gears = get_gear_ratios(adjacent_to_gears)
    print(f"Part two: sum of all gear ratios = {sum(valid_gears)}")


if __name__ == "__main__":
    day3()
