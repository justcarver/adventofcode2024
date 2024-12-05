def read_input(filename):
    data = ""
    with open(filename, "r") as file:
        data = file.read()

    rows = data.strip().split("\n")
    grid = []
    for row in rows:
        grid.append(list(row))
    return grid


def search2D(grid, row, col, word):
    m = len(grid)
    n = len(grid[0])

    # if the current chracter does not match first character of word
    # return False
    if grid[row][col] != word[0]:
        return False

    word_length = len(word)

    # Directions for searching
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    numberTrue = 0

    for dir in range(8):
        curX, curY = row + x[dir], col + y[dir]
        k = 1

        while k < word_length:
            # Check boundaries
            if curX >= m or curX < 0 or curY >= n or curY < 0:
                break

            # Check match
            if grid[curX][curY] != word[k]:
                break

            curX += x[dir]
            curY += y[dir]
            k += 1

        if k == word_length:
            # If k == word lennth, then the word was found
            numberTrue += 1
    # if word was not found in any direction
    return numberTrue


def searchWord(grid, word):
    m = len(grid)
    n = len(grid[0])

    ans = 0

    for i in range(m):
        for j in range(n):
            # if the word is found, append its coordinate to the result
            timesFound = search2D(grid, i, j, word)
            if timesFound > 0:
                ans += timesFound

    return ans


def check_for_x(grid, x, y):
    if x > 0 and x < len(grid) - 1:
        if y > 0 and y < len(grid[x]) - 1:
            first_leg = f"{grid[x-1][y-1]}{grid[x][y]}{grid[x+1][y+1]}"
            second_leg = f"{grid[x-1][y+1]}{grid[x][y]}{grid[x+1][y-1]}"
            if (first_leg == "MAS" or first_leg == "SAM") and (second_leg == "MAS" or second_leg == "SAM"):
                return True
    return False


def searchX(grid):
    m = len(grid)
    n = len(grid[0])

    ans = []

    center_letter = "A"

    for i in range(m):
        for j in range(n):
            if grid[i][j] == center_letter:
                if check_for_x(grid, i, j):
                    ans.append((i, j))

    return ans


def part_1(filename):
    grid = read_input(filename)
    count = searchWord(grid, "XMAS")
    print(count)


def part_2(filename):
    grid = read_input(filename)
    exes = searchX(grid)
    print(len(exes))


if __name__ == "__main__":
    input_name = "input.txt"
    part_1(input_name)
    part_2(input_name)
