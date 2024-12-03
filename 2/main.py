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


if __name__ == "__main__":
    count = 0
    data = ""
    with open("sample.txt", "r") as file:
        data = file.read()

    print(data)
    rows = data.strip().split("\n")

    for idx, row in enumerate(rows):
        readings = row.split(" ")
        print(idx, readings)
        if check_increasing(readings) or check_decreasing(readings):
            if check_distance(readings, 3):
                count = count + 1
                print("valid")
        else:
            print("invalid")
    print(count)
