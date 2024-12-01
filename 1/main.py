def parse_locations(location_lists):
    list_1 = []
    list_2 = []
    for line in location_lists.split("\n"):
        if line:
            test = line.split(" ")
            list_1.append(int(test[0]))
            list_2.append(int(test[-1]))
    return list_1, list_2


def compare_lists(list_1, list_2):
    total = 0
    for i, val in enumerate(list_1):
        total = total + abs(list_1[i] - list_2[i])
    return total


def part_1(location_lists):
    first_list, second_list = parse_locations(location_lists)
    first_list.sort()
    second_list.sort()
    total_distance = compare_lists(first_list, second_list)
    print(total_distance)


def part_2(location_lists):
    first_list, second_list = parse_locations(location_lists)

    total = 0
    for val in first_list:
        print(val)
        print(second_list.count(val))
        print("=====")

        total = total + (val * second_list.count(val))
    print(total)


if __name__ == "__main__":
    test_input = ""
    with open("input1.txt", "r") as file:
        test_input = file.read()
    # part_1(test_input)
    part_2(test_input)
