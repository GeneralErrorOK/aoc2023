from typing import Union


class Lens:
    def __init__(self, label: str, focal_length: int) -> None:
        self.label = label
        self.fl = focal_length

    def __repr__(self) -> str:
        return f"{self.label} {self.fl}"

    def __eq__(self, other: object) -> bool:
        return self.label == other


class LensBoxes:
    def __init__(self, hashing_algo: callable) -> None:
        self._boxes = {x: [] for x in range(256)}
        self._hash = hashing_algo

    def _label_in_box(self, label: str, box: int) -> bool:
        return any(label == lens.label for lens in self._boxes[box])

    def _remove_lens(self, label: str, box: int) -> Union[None, int]:
        if self._label_in_box(label, box):
            index = self._boxes[box].index(label)
            self._boxes[box].remove(label)
            return index

    def _add_lens(self, label: str, box: int, focal_length: int) -> None:
        if not self._label_in_box(label, box):
            self._boxes[box].append(Lens(label, focal_length))
        if self._label_in_box(label, box):
            index = self._remove_lens(label, box)
            self._boxes[box].insert(index, Lens(label, focal_length))

    def __repr__(self) -> str:
        string = ""
        for key in self._boxes:
            string += f"Box {key}: {[l for l in self._boxes[key]]}\n"
        return string

    def process_operation(self, op: str) -> None:
        if op[-1] == "-":
            label = op[:-1]
            boxnr = self._hash(label)
            self._remove_lens(label, boxnr)
        elif op[-2] == "=":
            label, focal_length = op.split("=")
            boxnr = self._hash(label)
            self._add_lens(label, boxnr, focal_length)

    def focusing_power(self) -> int:
        focusing_power = 0
        for key in self._boxes:
            box = self._boxes[key]
            if len(box) > 0:
                for i, l in enumerate(box):
                    focusing_power = focusing_power + ((key + 1) * (i + 1) * int(l.fl))
        return focusing_power


def holiday_ASCII_string_helper_algorithm(string: str) -> int:
    cv = 0
    for c in string:
        cv += ord(c)
        cv = cv * 17
        cv = cv % 256
    return cv


def part_one(lines: str) -> int:
    init_sequence = lines.split(",")
    answer = 0
    for seq in init_sequence:
        answer += holiday_ASCII_string_helper_algorithm(seq)
    return answer


def part_two(lines: str) -> int:
    init_sequence = lines.split(",")
    lensboxes = LensBoxes(holiday_ASCII_string_helper_algorithm)
    for seq in init_sequence:
        lensboxes.process_operation(seq)
    return lensboxes.focusing_power()


def day15():
    with open("d15/input.txt", "r") as file:
        lines = file.read()

    answer = part_one(lines)
    print(f"Part one answer = {answer}")

    answer = part_two(lines)
    print(f"Part two answer = {answer}")


if __name__ == "__main__":
    day15()
