if __name__ == "__main__":
    input = open("input.txt", "r")
    values = input.readlines()
    values = [int(x.strip()) for x in values]

    increased = 0

    smoothed = [sum(values[i : (i + 3)]) for i in range(0, len(values[:-2]))]

    for i in range(0, len(smoothed)):
        increased += smoothed[i] > smoothed[i - 1]

    print(increased)
