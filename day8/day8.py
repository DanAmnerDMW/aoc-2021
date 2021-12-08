def part1(values):
    values = [x.strip().split("|") for x in values]
    possible_matches = [x[1].strip().split(" ") for x in values]
    possible_matches = [item for sublist in possible_matches for item in sublist]

    matches = [x for x in possible_matches if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7]

    return len(matches)


def part2(values):
    values = [x.strip().split("|") for x in values]

    result = 0

    for input in values:
        wiring = input[0]
        output = input[1]

        digits = [0] * 10

        blocks = wiring.strip().split(" ")

        for block in list(blocks):
            # Solve for known values
            if len(block) == 2:
                digits[1] = block
                blocks.remove(block)
            elif len(block) == 3:
                digits[7] = block
                blocks.remove(block)
            elif len(block) == 4:
                digits[4] = block
                blocks.remove(block)
            elif len(block) == 7:
                digits[8] = block
                blocks.remove(block)

        for block in list(blocks):
            # If 1 overlaps must be 3,9 or 0
            if all(char in list(block) for char in list(digits[1])):
                if len(block) == 6:
                    if all(char in list(block) for char in list(digits[4])):
                        digits[9] = block
                        blocks.remove(block)
                    else:
                        digits[0] = block
                        blocks.remove(block)
                else:
                    digits[3] = block
                    blocks.remove(block)

        # If 6 long mist be 6, else if subset of 9 must be 5 else 2
        for block in list(blocks):
            if len(block) == 6:
                digits[6] = block
            else:
                if all(char in list(digits[9]) for char in list(block)):
                    digits[5] = block
                else:
                    digits[2] = block

            blocks.remove(block)

        # Iterate through results to get reading
        reading = ""
        for value in output.strip().split(" "):
            for i, digit in enumerate(digits):
                if sorted(list(value)) == sorted(list(digit)):
                    reading += str(i)

        # Add readings
        result += int(reading)
    return result


if __name__ == "__main__":
    input = open("day8/input.txt", "r")
    values = input.readlines()

    print(f"Part 1: {part1(values)}")
    print(f"Part 2: {part2(values)}")
