import math
from typing import List


def get_l_or_r_node(inst: str, node: List[str]) -> str:
    if inst == "L":
        return node[0]
    elif inst == "R":
        return node[1]
    else:
        raise ValueError


def create_node_dict(lines: List[str]) -> dict:
    nodes = {}
    for line in lines:
        node_parent = line.split("=")[0].strip()
        node_children = (
            "".join(line.split("=")[1].strip()[1:9]).replace(" ", "").split(",")
        )
        nodes[node_parent] = node_children
    return nodes


def part_one(lines: str) -> int:
    lines = lines.split("\n")
    instructions = [c for c in lines[0]]
    lines = lines[2:]
    nodes = create_node_dict(lines)
    current_node = "AAA"
    instr_index = steps_taken = 0
    while current_node != "ZZZ":
        instruction = instructions[instr_index]
        current_node = get_l_or_r_node(instruction, nodes[current_node])
        steps_taken += 1
        # make sure to wrap around:
        instr_index = (instr_index + 1) % len(instructions)
    return steps_taken


def part_two(lines: str) -> int:
    lines = lines.split("\n")
    instructions = [c for c in lines[0]]
    lines = lines[2:]
    nodes = create_node_dict(lines)
    starting_nodes = [node for node in nodes if node.endswith("A")]
    lcm_list = []
    for current_node in starting_nodes:
        instr_index = steps_taken = 0
        while not current_node.endswith("Z"):
            instruction = instructions[instr_index]
            current_node = get_l_or_r_node(instruction, nodes[current_node])
            steps_taken += 1
            # make sure to wrap around:
            instr_index = (instr_index + 1) % len(instructions)
        lcm_list.append(steps_taken)
    return math.lcm(*lcm_list)


def day8():
    with open("d8/input.txt", "r") as file:
        lines = file.read()

    answer = part_one(lines)
    print(f"Part one answer = {answer}")

    answer = part_two(lines)
    print(f"Part two answer = {answer}")


if __name__ == "__main__":
    day8()
