
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def read_input(filename):
    data = ""
    with open(filename, "r") as file:
        data = file.read()

    rows = data.strip().split("\n")
    map = []
    player = {"x": 0, "y": 0, "direction": (0, -1)}
    for idx, line in enumerate(rows):
        if "^" in line:
            player["x"] = line.index("^")
            player["y"] = idx
        map.append(list(line))

    return map, player


def check_presense(player, dimensions):
    # print("check_presence")
    # print(player, dimensions)
    if player["x"] < 0 or player["x"] >= dimensions["x"]:
        return False
    if player["y"] < 0 or player["y"] >= dimensions["y"]:
        return False
    return True


def check_clear(map, coords):
    if map[coords["y"]][coords["x"]] == '#':
        return False
    return True


def turn_player(player, direction):
    # direction is 1 or -1, 1 for turning right, -1 for turning left
    dir_idx = directions.index(player["direction"]) + direction
    if dir_idx < 0:
        dir_idx = len(directions) - 1
    if dir_idx >= len(directions):
        dir_idx = 0
    player["direction"] = directions[dir_idx]
    return player


def rotate_player(player, map, dimensions):
    destination_coords = {
        "x": player["x"] + player["direction"][0],
        "y": player["y"] + player["direction"][1],
    }

    if check_presense(destination_coords, dimensions):
        if not check_clear(map, destination_coords):
            map[player["y"]][player["x"]] = "+"

            player = turn_player(player, 1)

    return player


def check_distinct(map, char):
    count = 0
    for row in map:
        for x in row:
            if x in char:
                count += 1
    return count


def part_1(map, player):
    player_in_map = True
    steps = 0
    dimensions = {"x": len(map[0]), "y": len(map)}
    print(dimensions)

    while player_in_map:

        map[player["y"]][player["x"]] = "X"
        player = rotate_player(player, map, dimensions)
        # check if obstruction, and if obstruction, turn right
        # destination_obstructed = False
        #     print(map[player["y"]][player["x"]])
        #     destination = {"x": player["x"] + player["direction"]
        #                    [0], "y": player["y"] + player["direction"][1]}
        #     print("destination", destination)
        #     if map[destination["y"]][destination["x"]] == "#":
        #         destination_obstructed = True
        #         break
        #     player_direction_idx = directions.index(player["direction"]) + 1
        #     if player_direction_idx + 1 > len(directions):
        #         player_direction_idx = 0
        #     player["direction"] = directions[player_direction_idx]
        # in the map, and not obstructed, move the player in the direction
        player["x"] += player["direction"][0]
        player["y"] += player["direction"][1]
        steps += 1
        # check if player outside the map
        if not check_presense(player, dimensions):
            player_in_map = False
    for row in map:
        print(row)
    print(check_distinct(map, ["X", "+"]))
    return map


def part_2(map, player, initial_position):
    obstacles = [
        (3, 6),
        (6, 7),
        (7, 7),
        (1, 8),
        (3, 8),
        (7, 9),
    ]
    for obstacle in obstacles:
        print(map[obstacle[1]][obstacle[0]])

    symbols = ["X", "+"]

    for y, row in enumerate(guard_path):
        for x, col in enumerate(row):
            player["x"] = initial_position[0]
            player["y"] = initial_position[1]

    pass


if __name__ == "__main__":
    input_name = "sample.txt"
    map, player = read_input(input_name)
    for row in map:
        print(row)
    print(player)
    initial_position = (player["x"], player["y"])

    guard_path = part_1(map, player)
    part_2(guard_path, player, initial_position)
