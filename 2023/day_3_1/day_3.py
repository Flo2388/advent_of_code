def get_digit_indexes(current_line: str, previous_line: str, next_line: str) -> dict:
    part_list = []
    index = 0
    number_to_check = ""

    while index < len(current_line):
        if current_line[index].isdigit():
            number_to_check += current_line[index]
            if current_line[index-1] == ".":
                start_index = index
            if current_line[index+1] == ".":
                end_index = index
                if get_adjacent_symbol(previous_line, next_line, current_line, start_index, end_index):
                    part_list.append(number_to_check)

        index += 1

    return part_list


def get_adjacent_symbol(previous_line: str, next_line: str, current_line: str, start_index: int, end_index: int) -> bool:
    for index in range(start_index-1, end_index+2,1):
        if end_index+2 == "\n":
            if not (previous_line[index].isdigit() or previous_line[index] == "."):
                return True
            elif not (current_line[index].isdigit() or current_line[index] == "."):
                return True
            elif not (next_line[index].isdigit() or next_line[index] == "."):
                return True

        return False




def main():
    with open("../inputs/day_3_input.txt", "r") as input_file:
        current_line_number = 1
        previous_line_number = 1
        next_line_number = 2
        file = input_file.readlines()
        while True:
            current_line = file[current_line_number]
            previous_line = input_file.readline(previous_line_number)
            next_line = input_file.readline(next_line_number)

            print(get_digit_indexes(current_line, previous_line, next_line))

            current_line_number += 1
            next_line_number = current_line_number+1
            previous_line_number = current_line_number-1

            if next_line_number == len(file):
                next_line = current_line
            elif current_line_number == len(file):
                break



if __name__ == "__main__":
    main()
