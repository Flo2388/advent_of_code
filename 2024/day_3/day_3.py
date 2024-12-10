#!/usr/bin/env python3

import re

def filter_multiplications(line: str) -> list:
    multiplication_strings = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)
    print(multiplication_strings)
    
def get_multipliers(mp_string: str) -> list:
    mp_string_list = re.findall(r'[0-9]{1,3}')

def main():
    with open('../inputs/day_3.input.txt', 'r') as file:
        for line in file:
            filter_multiplications(line)
            
                    
if __name__ == "__main__":
    main()
            