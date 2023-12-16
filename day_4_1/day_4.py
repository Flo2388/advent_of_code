import re
from typing import List, Tuple

def get_formated_split_string(line: str) -> List[str]:
    split_line_list = re.sub(r"\s+", " ",line).strip("\n").split(":")

    return split_line_list

def get_splited_numbers(line: str) -> Tuple[str]:
    splited_numbers = line.split("|")
    return splited_numbers

def convert_to_int_list(line:str) -> List[int]:
    split_numbers = line.strip().split(" ")
    converted_numbers = []
    for number in split_numbers:
        converted_numbers.append(int(number))

    return converted_numbers

def get_card_value(winning_numbers: list, own_numbers: list) -> int:
    match_counter = 0
    for number in own_numbers:
        if number in winning_numbers:
            match_counter += 1

    if match_counter > 0:
        points = 1
        i = 1
        while i < match_counter:
            points *= 2
            i += 1
        return points

    return 0


def main():
    points = 0
    with open("../inputs/day_4_input.txt", "r") as input_file:
         for line in input_file:
            split_list = get_formated_split_string(line)
            winning_numbers_string, own_numbers_string = get_splited_numbers(split_list[1])
            winning_numbers = convert_to_int_list(winning_numbers_string)
            own_numbers = convert_to_int_list(own_numbers_string)
            points += get_card_value(winning_numbers, own_numbers)

    print(points)



if __name__ == "__main__":
    main()
