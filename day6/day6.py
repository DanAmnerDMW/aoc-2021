class Lanternfish:
    def __init__(self, initial_value) -> None:
        self.timer = initial_value

    def increment_day(self):
        if self.timer == 0:
            self.timer = 6
            return Lanternfish(8)

        self.timer -= 1

        return None


def part1(values):

    values = values[0].split(",")
    values = [int(x) for x in values]

    fish = [Lanternfish(x) for x in values]

    for day in range(80):
        for a_fish in list(fish):
            new_fish = a_fish.increment_day()
            if new_fish:
                fish.append(new_fish)

    return len(fish)


def part2(values):
    values = values[0].split(",")
    values = [int(x) for x in values]

    ages = [0] * 9

    for value in values:
        ages[value] += 1

    for day in range(256):
        ages[(day + 7) % 9] += ages[day % 9]

    return sum(ages)


if __name__ == "__main__":
    input = open("day6/input.txt", "r")
    values = input.readlines()
    values = [x.strip() for x in values]

    print(f"Part 1: {part1(values)}")
    print(f"Part 2: {part2(values)}")
