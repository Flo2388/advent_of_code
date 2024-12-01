#!/usr/bin/env python3
import re

def get_distance_difference(distance_a: int, distance_b:int) -> int:
    if distance_a > distance_b:
        return (distance_a - distance_b)
    else:
        return (distance_b - distance_a)

def return_biggest_number_and_index(list: list) -> tuple[int, int]:
    biggest_number = 0
    index = 0
    index_biggest_number = 0
    for number in list:
        if number > biggest_number:
            biggest_number = number
            index_biggest_number = index
        index = index +1

    
    return biggest_number, index_biggest_number
       

def convert_to_int(line: list[str]) -> list[int]:
    converted_list = []
    for place in line:
        converted_list.append(int(place))
    
#    print(converted_list)
    return converted_list
    


def line_split(line: str) -> list[str]:
    squeezed_line = re.sub(' +', ' ', line)
    split_line = squeezed_line.split()
    
    return split_line
    

def main():
    list_a = []
    list_b = []
    total_distance = 0
    
    with open("../inputs/day_1_input.txt" , "r") as input:
        for line in input:
            split_line = line_split(line)
            conv_list = convert_to_int(split_line)
            list_a.append(conv_list[0])
            list_b.append(conv_list[1])    
    while True:
        if (len(list_a) or len(list_b)) == 0:
            break
        else:
            distance_a, index = return_biggest_number_and_index(list_a)
            del list_a[index]
            distance_b, index = return_biggest_number_and_index(list_b)
            del list_b[index]
            total_distance = total_distance + (get_distance_difference(distance_a, distance_b))
            
    print("Total distance: " + str(total_distance))
            
            

if __name__ == "__main__":
    main()