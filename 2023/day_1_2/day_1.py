import regex as re

def number_finder(line: list) -> int:
    all_digits = []
    for element in line:
        if element.isdigit():
            all_digits.append(element)
        else:
            digits_from_string = get_number_from_string(element)
            for digit in digits_from_string:
                all_digits.append(digit)


    if len(all_digits) > 1:
        return int(all_digits[0]+all_digits[-1])
    if len(all_digits) == 1:
        return int(all_digits[0]*2)

def get_number_from_string(line: str) -> list:
    digit_strings = re.findall(
                                r'one|'
                                r'two|'
                                r'three|'
                                r'four|'
                                r'five|'
                                r'six|'
                                r'seven|'
                                r'eight|'
                                r'nine', line, overlapped=True
                                )

    converted_digits = []
    for element in digit_strings:
        if element == "one":
            converted_digits.append("1")
        elif element == "two":
            converted_digits.append("2")
        elif element == "three":
            converted_digits.append("3")
        elif element == "four":
            converted_digits.append("4")
        elif element == "five":
            converted_digits.append("5")
        elif element == "six":
            converted_digits.append("6")
        elif element == "seven":
            converted_digits.append("7")
        elif element == "eight":
            converted_digits.append("8")
        elif element == "nine":
            converted_digits.append("9")

    return converted_digits


def main():
    temp_results = []
    with open("../inputs/day_1_input.txt", "r") as file:

        for line in file:
            line_split_list = re.split(r'(\d)', line.strip())
            line_split_list = list(filter(None, line_split_list))
            line_result = number_finder(line_split_list)
            temp_results.append(line_result)

    calibration_value= sum(temp_results)

    print(calibration_value)

if __name__ == "__main__":
    main()
