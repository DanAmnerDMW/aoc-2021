from day1 import day1


example_input = ["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"]


def test_part1():
    assert day1.part1(example_input) == 7


def test_part2():
    assert day1.part2(example_input) == 5
