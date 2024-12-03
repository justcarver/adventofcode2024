def check_decreasing(readings):
    for idx, reading in enumerate(readings):
        if idx > 0:
            if int(reading) >= int(readings[idx - 1]):
                return False
    print("decreasing")
    return True


def check_increasing(readings):
    for idx, reading in enumerate(readings):
        if idx > 0:
            if int(reading) <= int(readings[idx - 1]):
                return False
    print("increasing")
    return True


def check_distance(readings, val):
    for idx, reading in enumerate(readings):
        if idx > 0:
            check_value = abs(int(reading) - int(readings[idx - 1]))
            if check_value > val:
                return False
    print("within limits")
    return True


def read_input(filename):
    data = ""
    with open(filename, "r") as file:
        data = file.read()

    rows = data.strip().split("\n")
    return rows


def check_row(readings):
    if check_increasing(readings) or check_decreasing(readings):
        if check_distance(readings, 3):
            return True
    else:
        return False


def dampener(readings):
    if check_row(readings):
        return True
    else:
        for i in range(len(readings)):
            if check_row(readings[:i] + readings[i+1:]):
                return True
    return False


def part_1(filename):
    count = 0

    rows = read_input(filename)
    for idx, row in enumerate(rows):
        readings = row.split(" ")
        print(idx, readings)
        if check_row(readings):
            count = count + 1
            print("valid")
        else:
            print("invalid")
    print(count)


def part_2(filename):
    count = 0

    rows = read_input(filename)
    for idx, row in enumerate(rows):
        readings = row.split(" ")
        print(idx, readings)
        if dampener(readings):
            count = count + 1
            print("valid")
        else:
            print("invalid")
    print(count)


if __name__ == "__main__":
    input_name = "input.txt"
    # part_1(input_name)
    part_2(input_name)
