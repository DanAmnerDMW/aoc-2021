from day3 import day3

example_input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]


def test_part1():
    assert day3.part1(example_input) == 198


def test_part2():
    assert day3.part2(example_input) == 230
