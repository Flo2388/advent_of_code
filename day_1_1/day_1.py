def number_finder(line: str) -> int:
    all_digits = []
    for char in line:
            if char.isdigit():
                all_digits.append(char)
                # print(len(all_digits))
    if len(all_digits) > 1:
        return int(all_digits[0]+all_digits[-1])
    if len(all_digits) == 1:
        return int(all_digits[0]*2)


def main():
    temp_results = []
    with open("../inputs/day_1_input.txt", "r") as file:

        for line in file:
            line_result = number_finder(line.strip())
            print(line_result)
            temp_results.append(line_result)

    calibration_value= sum(temp_results)

    print(calibration_value)

if __name__ == "__main__":
    main()
