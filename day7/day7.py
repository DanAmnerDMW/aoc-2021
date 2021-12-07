import pandas as pd


def part1(values):
    values = values[0].split(",")
    values = [int(x.strip()) for x in values]
    positions = pd.Series(values)

    idx = pd.RangeIndex(positions.min(), positions.max())
    df = pd.DataFrame(index=idx)
    df["Distance"] = 0

    for position in positions:
        df.iloc[df.index, 0] += abs(df.index - position)

    return df["Distance"].min()


def part2(values):
    values = values[0].split(",")
    values = [int(x.strip()) for x in values]
    positions = pd.Series(values)

    idx = pd.RangeIndex(positions.min(), positions.max())
    df = pd.DataFrame(index=idx)
    df["Distance"] = 0

    for position in positions:
        distance = abs(df.index - position)
        df.iloc[df.index, 0] += (distance * (distance + 1)) / 2

    return df["Distance"].min()


if __name__ == "__main__":
    input = open("day7/input.txt", "r")
    values = input.readlines()

    print(f"Part 1: {part1(values)}")
    print(f"Part 2: {part2(values)}")
