def part1(values):
    values = [list(value.split()) for value in values]
    # Remove ->
    for value in values:
        del value[1]

    # Get coords
    values = [convert_to_coords(value) for value in values]

    points = {}

    for input in values:
        x_diff = input["x1"] - input["x2"]
        y_diff = input["y1"] - input["y2"]

        # Plot horizontal lines
        if abs(x_diff) > 0 and abs(y_diff) == 0:
            points = plot_horizontal_line(input, points, x_diff)
        # Plot vertical lines
        elif abs(y_diff) > 0 and abs(x_diff) == 0:
            points = plot_vertical_line(input, points, y_diff)

    # Count all values 2 and above
    counter = 0
    for value in points.values():
        if value >= 2:
            counter += 1

    return counter


def part2(values):
    values = [list(x.split()) for x in values]
    # Remove ->
    for value in values:
        del value[1]

    # Get coords
    values = [convert_to_coords(x) for x in values]

    points = {}

    for input in values:
        x_diff = input["x1"] - input["x2"]
        y_diff = input["y1"] - input["y2"]

        # Plot diagonal lines
        if abs(x_diff) == abs(y_diff):
            points = plot_diagonal_line(input, points, x_diff, y_diff)
        # Plot horizontal lines
        elif abs(x_diff) > 0 and abs(y_diff) == 0:
            points = plot_horizontal_line(input, points, x_diff)
        # Plot vertical lines
        elif abs(y_diff) > 0 and abs(x_diff) == 0:
            points = plot_vertical_line(input, points, y_diff)

    # Count all values 2 and above
    counter = 0
    for value in points.values():
        if value >= 2:
            counter += 1

    return counter


def convert_to_coords(input):
    # Convert to coords
    coord1 = input[0].split(",")
    coord2 = input[1].split(",")

    return {
        "x1": int(coord1[0]),
        "y1": int(coord1[1]),
        "x2": int(coord2[0]),
        "y2": int(coord2[1]),
    }


def plot_horizontal_line(input, points, x_diff):
    # Plot start and end points
    points = plot_point((input["x1"], input["y1"]), points)
    points = plot_point((input["x2"], input["y2"]), points)
    for x in range(1, abs(x_diff)):
        # 2 different horiz types
        if x_diff < 0:
            points = plot_point((input["x1"] + x, input["y1"]), points)
        else:
            points = plot_point((input["x1"] - x, input["y1"]), points)

    return points


def plot_vertical_line(input, points, y_diff):
    # Plot start and end points
    points = plot_point((input["x1"], input["y1"]), points)
    points = plot_point((input["x2"], input["y2"]), points)
    for y in range(1, abs(y_diff)):
        # 2 different vert types
        if y_diff < 0:
            points = plot_point((input["x1"], input["y1"] + y), points)
        else:
            points = plot_point((input["x1"], input["y1"] - y), points)

    return points


def plot_diagonal_line(input, points, x_diff, y_diff):
    # Plot start and end points
    points = plot_point((input["x1"], input["y1"]), points)
    points = plot_point((input["x2"], input["y2"]), points)
    for x in range(1, abs(x_diff)):
        # 4 different diag types
        if x_diff < 0 and y_diff > 0:
            points = plot_point((input["x1"] + x, input["y1"] - x), points)
        elif x_diff < 0 and y_diff < 0:
            points = plot_point((input["x1"] + x, input["y1"] + x), points)
        elif x_diff > 0 and y_diff > 0:
            points = plot_point((input["x1"] - x, input["y1"] - x), points)
        elif x_diff > 0 and y_diff < 0:
            points = plot_point((input["x1"] - x, input["y1"] + x), points)

    return points


def plot_point(point, points):
    # Increment existing point or add new point
    if point in points:
        points[point] += 1
    else:
        points[point] = 1

    return points


if __name__ == "__main__":
    input = open("day5/input.txt", "r")
    values = input.readlines()
    values = [x.strip() for x in values]

    print(f"Part 1: {part1(values)}")
    print(f"Part 2: {part2(values)}")
