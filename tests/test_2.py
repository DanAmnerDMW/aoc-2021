from day2 import day2

example_input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def test_part1():
    assert day2.part1(example_input) == 150


def test_part2():
    assert day2.part2(example_input) == 900
