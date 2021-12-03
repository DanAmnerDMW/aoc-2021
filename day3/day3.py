import pandas as pd


def part1(values):

    # Split each char in string into seperate columns in dataframe
    chars = [list(x.strip()) for x in values]
    df = pd.DataFrame(chars)

    # Convert to boolean values
    df = df.astype(int).astype(bool)

    # Get the Modal value for each column
    gamma_df = df.mode(axis=0)
    # Invert the Modal value to get the least common value
    epsilon_df = ~gamma_df

    # Convert back to string
    gamma_df = gamma_df.astype(int).astype(str)
    epsilon_df = epsilon_df.astype(int).astype(str)

    # Merge all column values into one column
    gamma_df["merged"] = gamma_df.apply(lambda x: "".join(x), axis=1)
    epsilon_df["merged"] = epsilon_df.apply(lambda x: "".join(x), axis=1)

    # Convert binary representation to int
    gamma = binary_to_decimal(gamma_df["merged"])
    epsilon = binary_to_decimal(epsilon_df["merged"])

    return gamma * epsilon


def part2(values):

    # Split each char in string into seperate columns in dataframe
    chars = [list(x.strip()) for x in values]
    df = pd.DataFrame(chars)

    # Convert to boolean values
    df = df.astype(int).astype(bool)

    # Get the gamma and epsilon values again
    gamma_df = df.mode(axis=0)
    epsilon_df = ~gamma_df

    # Get ratings
    oxygen = find_rating(source_df=df.copy(), modal_df=gamma_df.copy().max(), use_min=False)
    co2 = find_rating(source_df=df.copy(), modal_df=epsilon_df.copy().max(), use_min=True)

    return oxygen * co2


def binary_to_decimal(binary: str) -> int:
    return int(binary[0], 2)


def find_rating(source_df: pd.DataFrame, modal_df: pd.DataFrame, use_min: bool) -> int:
    # Iterate through each column getting the matching on each columns modal value
    for column in source_df.columns:
        source_df = source_df[source_df[column] == modal_df[column]]
        # Re-calculate the mode from remaining values
        modal_df = source_df.mode(axis=0).max(axis=0).astype(bool)
        if use_min:
            modal_df = ~modal_df

        # Exit loop when we have found the rating
        if source_df.shape[0] == 1:
            break

    # Convert back to string
    source_df = source_df.astype(int).astype(str)

    # Merge all column values into one column
    source_df["merged"] = source_df.apply(lambda x: "".join(x), axis=1)
    source_df = source_df.reset_index()
    # Convert binary representation to int
    return binary_to_decimal(source_df["merged"])


if __name__ == "__main__":
    input = open("input.txt", "r")
    values = input.readlines()

    print(f"Part 1: {part1(values)}")
    print(f"Part 2: {part2(values)}")
