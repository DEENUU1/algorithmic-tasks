r, g, b = 12, 13, 14

with open("day2a_input.txt", "r") as file:
    data = file.read().splitlines()


def is_possible(game, red, green, blue):
    count = {"red": 0, "green": 0, "blue": 0}

    for subset in game:
        cubes = subset.split(";")
        for cube in cubes:
            color = cube
            print(color)
            count[color] += 1

    # Check if the counts match the given constraint
    return count['red'] == red and count['green'] == green and count['blue'] == blue


def possible_games(games, red, green, blue):
    possible_idx = []
    for idx, game in enumerate(games):
        if is_possible(game, red, green, blue):
            possible_idx.append(idx)

    return possible_idx


res = possible_games(data, r, g, b)
print(sum(res))