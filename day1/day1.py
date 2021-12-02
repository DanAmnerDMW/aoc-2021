from typing import List


def part1(values: List) -> int:
    values = [int(x.strip()) for x in values]

    increased = 0

    for i in range(0, len(values)):
        increased += values[i] > values[i - 1]

    return increased


def part2(values: List) -> int:
    values = [int(x.strip()) for x in values]

    increased = 0

    smoothed = [sum(values[i : (i + 3)]) for i in range(0, len(values[:-2]))]

    for i in range(0, len(smoothed)):
        increased += smoothed[i] > smoothed[i - 1]

    return increased


if __name__ == "__main__":
    input = open("input.txt", "r")

    print(f"Part 1: {part1(input.readlines())}")
    print(f"Part 2: {part2(input.readlines())}")
