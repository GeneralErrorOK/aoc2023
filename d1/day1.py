from typing import List
import re


NUMBER_LIST = [
    "one",
    "1",
    "two",
    "2",
    "three",
    "3",
    "four",
    "4",
    "five",
    "5",
    "six",
    "6",
    "seven",
    "7",
    "eight",
    "8",
    "nine",
    "9",
    "ten",
]


def get_numbers_and_words_from_line(number_list: List, line: str) -> int:
    hi_index, lo_index = (0, len(line))
    hi_char = lo_char = None
    for word in number_list:
        for re_match in re.finditer(word, line):
            index = re_match.start()
            if index > hi_index:
                hi_index = index
                hi_char = word
            if index < lo_index:
                lo_index = index
                lo_char = word
    if hi_char is None:
        hi_char = lo_char
    elif lo_char is None:
        lo_char = hi_char

    def round_to_nearest_even(number: int) -> int:
        if number % 2 == 0:
            return number + 1
        else:
            return number

    lo_digit = round_to_nearest_even(number_list.index(lo_char))
    hi_digit = round_to_nearest_even(number_list.index(hi_char))

    magic_number = int(number_list[lo_digit] + number_list[hi_digit])

    return magic_number


def get_number_from_line(line: str) -> int:
    numbers = []
    for c in line:
        if not c.isalpha():
            numbers.append(c)
    return int(numbers[0] + numbers[-1])


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = file.read().split("\n")

    total = 0
    for line in lines:
        total += get_numbers_and_words_from_line(NUMBER_LIST, line)

    print(total)
