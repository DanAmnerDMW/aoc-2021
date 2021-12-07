from day7 import day7

example_input = ["16,1,2,0,4,2,7,1,2,14"]


def test_part1():
    assert day7.part1(example_input) == 37


def test_part2():
    assert day7.part2(example_input) == 168
