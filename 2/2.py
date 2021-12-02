horizontal = 0
depth = 0
aim = 0

input = open("input.txt", "r")
values = [x.strip() for x in input.readlines()]

for value in values:
    split = value.split()

    if split[0] == "down":
        aim += int(split[1])
    elif split[0] == "up":
        aim -= int(split[1])
    elif split[0] == "forward":
        horizontal += int(split[1])
        depth += aim * int(split[1])

print(horizontal * depth)
