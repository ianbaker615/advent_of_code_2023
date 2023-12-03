import math


def day2(input_file_path: str) -> int:
    total = 0
    color_num_map = {"red": 12, "green": 13, "blue": 14}

    with open(input_file_path, "r") as file:
        for game_id, line in enumerate(file, start=1):
            line = line.rstrip("\n")  # Remove newline at end of line
            line = line.split(": ")[1]  # Remove Game # information
            valid_game = True
            for round in line.split(";"):
                for num_color in round.split(","):
                    combo = num_color.strip().split(" ")
                    num = int(combo[0])
                    color = combo[1]
                    if num > color_num_map[color]:
                        valid_game = False
                        break
                if valid_game is False:
                    break
            if valid_game is True:
                total += game_id

    return total


test = day2("test_input.txt")
print(f"Test result: {test}")
assert test == 8
print(f"Real result: {day2('input.txt')}")


def day2_2(input_file_path: str) -> int:
    total = 0

    with open(input_file_path, "r") as file:
        for line in file:
            color_num_map = {"red": 1, "green": 1, "blue": 1}
            line = line.rstrip("\n")
            line = line.split(": ")[1]
            for round in line.split(";"):
                for num_color in round.split(","):
                    combo = num_color.strip().split(" ")
                    num = int(combo[0])
                    color = combo[1]
                    if num > color_num_map[color]:
                        color_num_map[color] = num
            power = math.prod(color_num_map.values())
            total += power

    return total


test = day2_2("test_input.txt")
print(f"Test result: {test}")
assert test == 2286
print(f"Real result: {day2_2('input.txt')}")
