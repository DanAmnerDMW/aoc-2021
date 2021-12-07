import pandas as pd


def part1(values):
    values = values[0].split(",")
    values = [int(x.strip()) for x in values]
    positions = pd.Series(values)

    # Create index of all possible positions
    idx = pd.RangeIndex(positions.min(), positions.max())
    df = pd.DataFrame(index=idx)
    # Set all fuel to 0
    df["Fuel"] = 0

    # For each crab calculate the distance to reach each possible detination
    for position in positions:
        df.loc[df.index, "Fuel"] += abs(df.index - position)

    # Get the minimum distance
    return int(df["Fuel"].min())


def part2(values):
    values = values[0].split(",")
    values = [int(x.strip()) for x in values]
    positions = pd.Series(values)

    # Create index of all possible positions
    idx = pd.RangeIndex(positions.min(), positions.max())
    df = pd.DataFrame(index=idx)
    # Set all fuel to 0
    df["Fuel"] = 0

    # For each crab calculate the distance to reach each possible detination
    for position in positions:
        distance = abs(df.index - position)
        # Calculate the fuel used (1+2+3+4+5...distance)
        df.loc[df.index, "Fuel"] += (distance * (distance + 1)) / 2

    # Get the minimum fuel
    return int(df["Fuel"].min())


if __name__ == "__main__":
    input = open("day7/input.txt", "r")
    values = input.readlines()

    print(f"Part 1: {part1(values)}")
    print(f"Part 2: {part2(values)}")
