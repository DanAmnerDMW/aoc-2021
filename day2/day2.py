from typing import List


def part1(values: List) -> int:
    horizontal = 0
    depth = 0

    values = [x.strip() for x in values]

    for value in values:
        split = value.split()

        if split[0] == "down":
            depth += int(split[1])
        elif split[0] == "up":
            depth -= int(split[1])
        elif split[0] == "forward":
            horizontal += int(split[1])

    return horizontal * depth


def part2(values: List) -> int:
    horizontal = 0
    depth = 0
    aim = 0

    values = [x.strip() for x in values]

    for value in values:
        split = value.split()

        if split[0] == "down":
            aim += int(split[1])
        elif split[0] == "up":
            aim -= int(split[1])
        elif split[0] == "forward":
            horizontal += int(split[1])
            depth += aim * int(split[1])

    return horizontal * depth


if __name__ == "__main__":
    input = open("input.txt", "r")
    values = input.readlines()

    print(f"Part 1: {part1(values)}")
    print(f"Part 2: {part2(values)}")
