import re


def read_input(filename):
    data = ""
    with open(filename, "r") as file:
        data = file.read()

    rows = data.strip().split("\n")
    return rows


def part_1(filename):
    rows = read_input(filename)
    total = 0
    for row in rows:
        matches = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', row)
        for (a, b) in matches:
            mult = int(a) * int(b)
            total = total + mult
    print(total)


# OVERCOMPLICATED IT
def part_2(filename):
    total = 0
    rows = read_input(filename)

    data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))\n"
    data = "\n".join(rows)
    cleaned_data = re.sub(r'don\'t\(\)(.*)do\(\)', "", data)
    # cleaned_data = re.sub(r'don\'t\(\)(.*)\n', "", data)
    matches = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', cleaned_data)
    for (a, b) in matches:
        mult = int(a) * int(b)
        total = total + mult
    print(total)


def reddit(filename):
    # Inspired by some tips i saw on redit to use "or" in the match
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, open(filename).read())
    total = 0
    flag = True
    for match in matches:
        if match == "do()":
            flag = True
        elif match == "don't()":
            flag = False
        else:
            if flag:
                x, y = map(int, match[4:-1].split(","))
                total += x * y
    print(total)


if __name__ == "__main__":
    input_name = "input.txt"
    print("part 1")
    part_1(input_name)
    print("part 1")
    reddit(input_name)
