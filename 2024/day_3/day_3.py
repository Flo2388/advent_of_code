#!/usr/bin/env python3

import re

def filter_and_convert_multiplicators(multiplications: list) -> list:
    multiplicator_list =[]
    for multiplication in multiplications:
        multiplicator_list.append(re.findall(r'[0-9]{1,3}',multiplication))
    
    for set in multiplicator_list:
        for i in range(len(set)):
            set[i] = int(set[i])
    
    return multiplicator_list

def multiply_line_set(multiplicators: list) -> int:
    line_result = 0
    for multiplication_set in multiplicators:
        set_result = 1
        for multiplicator in multiplication_set:
            set_result = set_result * multiplicator
        line_result = line_result + set_result
    return line_result
        

def filter_multiplications(line: str) -> list:
    multiplication_strings = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)
    print(multiplication_strings)
    return multiplication_strings
    
def get_multipliers(mp_string: str) -> list:
    mp_string_list = re.findall(r'[0-9]{1,3}')

def main():
    multiplications = []
    multiplicator_list = []
    result = 0
    with open('../inputs/day_3.input.txt', 'r') as file:
        for line in file:
            multiplications = filter_multiplications(line)
            result = result + multiply_line_set(filter_and_convert_multiplicators(multiplications))
            
    print("Result: " + str(result))
    
            
            
                    
if __name__ == "__main__":
    main()
            