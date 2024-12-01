import re

TOTAL_CUBE_AMOUNT = {"red": 12, "green": 13, "blue": 14}
COLOURS = ("red", "green", "blue")


def parser(line:str) -> list:           #list of dicts
    round_list = []
    line = strip_game_id(line)
    rounds = split_different_rounds(line)
    for round in rounds:
        round_list.append(parse_round(round))

    return(round_list)

def parse_round(round:str) -> dict:
    colour_dict = {}
    colours = split_colours_per_round(round)
    for colour in colours:
        temp_list = colour.split()
        colour_dict.update( {temp_list[1]: int(temp_list[0])} )

    return colour_dict

def split_colours_per_round(round:str) -> list:         #list of strings
    return(round.split(sep=","))

def split_different_rounds(line: str) -> list:
    return(line.split(sep=";"))

def strip_game_id(line: str) -> str:
    return re.sub(r"Game\s\d+:", "", line).strip()

def is_game_possible(game: list) -> bool:
    for round in game:
        if not (round.get("green", 0) <= TOTAL_CUBE_AMOUNT["green"] and round.get("red", 0) <= TOTAL_CUBE_AMOUNT["red"] and round.get("blue", 0) <= TOTAL_CUBE_AMOUNT["blue"]):
            return False

    return True

def get_game_id(line: str) -> int:
    game = re.search(r'\w+:', line)
    game_id = re.search(r'\d+', game.group(0))
    return int(game_id.group(0))

def get_fewest_colour_amount_per_game(game: list)-> dict:
    colours = ("red", "green", "blue")
    fewest_colour = {colour:0 for colour in colours}
    for round in game:
        for colour in colours:
            if (round.get(colour) and round.get(colour) > fewest_colour[colour]):
                fewest_colour.update({colour:round[colour]})

    return fewest_colour

def get_power_per_game(fewest_colour_amount_per_game: dict) -> int:
    game_power = 1
    for colour in COLOURS:
        game_power *= fewest_colour_amount_per_game[colour]
    return game_power

def main():
    id_sum = 0
    power_of_cubes = 0

    with open("../inputs/day_2_input.txt", "r") as file:
        for line in file:
            game = parser(line)
            fewest_colour_amount_per_game = get_fewest_colour_amount_per_game(game)
            power_of_cubes += get_power_per_game(fewest_colour_amount_per_game)
            if is_game_possible(game):
                id_sum += get_game_id(line)

    print(f"Sum of valid game IDs:\t {id_sum}")
    print(f"Power of cubes:\t {power_of_cubes}")

if __name__ == "__main__":
    main()
