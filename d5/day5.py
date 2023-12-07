from typing import List
import itertools


class AlmanacMapRange:
    def __init__(self, dest: int, src: int, length: int) -> None:
        self.src = src
        self.dest = dest
        self.length = length

    def __repr__(self) -> str:
        return f"[{self.dest}, {self.src}, {self.length}]"

    def in_range_fwd(self, input: int) -> bool:
        return self.src <= input <= (self.src + self.length)

    def in_range_rev(self, input: int) -> bool:
        return self.dest <= input <= (self.dest + self.length)

    def map_fwd(self, input: int) -> int:
        return input - (self.src - self.dest)

    def map_rev(self, input: int) -> int:
        return input - (self.dest - self.src)


class AlmanacMapEntry:
    def __init__(self, name: str, verbose: bool = False) -> None:
        self.name = name
        self.ranges = []
        self.verbose = verbose

    def __repr__(self) -> str:
        return f"{self.name} map containing: {self.ranges}"

    def add_range(self, dest: int, src: int, length: int):
        self.ranges.append(AlmanacMapRange(dest, src, length))

    def map(self, input: int) -> int:
        if self.verbose:
            print(f"Mapping {self.name}:")
        for range in self.ranges:
            if range.in_range_fwd(input):
                output = range.map_fwd(input)
                if self.verbose:
                    print(f"{input} -> {output}")
                return output
        if self.verbose:
            print(f"{input} -> {input}")
        return input

    def map_reverse(self, input: int) -> int:
        if self.verbose:
            print(f"Mapping {self.name}:")
        for range in self.ranges:
            if range.in_range_rev(input):
                output = range.map_rev(input)
                if self.verbose:
                    print(f"{input} -> {output}")
                return output
        if self.verbose:
            print(f"{input} -> {input}")
        return input


class AlmanacMapper:
    def __init__(self, almanac_text: List[str], verbose: bool = False) -> None:
        self.verbose = verbose
        self.entries = []

        index = 0
        for line in almanac_text:
            if ":" in line:
                self.entries.append(AlmanacMapEntry(line.split()[0], self.verbose))
            elif line == "":
                index += 1
            else:
                dest, src, length = line.split()
                self.entries[index].add_range(int(dest), int(src), int(length))

        if verbose:
            for entry in self.entries:
                print(entry)

    def get_location(self, seed_nr: int) -> int:
        for map_entry in self.entries:
            seed_nr = map_entry.map(seed_nr)
        return seed_nr

    def get_seed(self, location_nr: int) -> int:
        for map_entry in reversed(self.entries):
            location_nr = map_entry.map_reverse(location_nr)
        return location_nr


def part_one(lines: str) -> int:
    split_lines = lines.split("\n")
    seed_nrs = [int(x) for x in split_lines[0].split(":")[1].split()]

    mapper = AlmanacMapper(split_lines[2:])

    locations = map(mapper.get_location, seed_nrs)
    return min(locations)


def part_two(lines: str, lower_bound: int):
    split_lines = lines.split("\n")
    seed_nrs = [int(x) for x in split_lines[0].split(":")[1].split()]

    mapper = AlmanacMapper(split_lines[2:])

    seed_ranges = []
    for index, seed_entry in enumerate(seed_nrs):
        if index % 2 == 0:
            seed_ranges.append((seed_entry, seed_entry + seed_nrs[index + 1]))
        else:
            continue

    candidate_seeds = map(mapper.get_seed, itertools.count(start=lower_bound))
    for candidate in candidate_seeds:
        for seed_range in seed_ranges:
            if candidate in range(seed_range[0], seed_range[1]):
                return mapper.get_location(candidate)


def day5():
    with open("d5/input.txt", "r") as file:
        lines = file.read()

    answer = part_one(lines)
    print(f"Part one answer = {answer}")
    # 802763513
    answer = part_two(lines, answer // 4)
    print(f"Part two answer = {answer}")


if __name__ == "__main__":
    day5()
