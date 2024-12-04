#!/usr/bin/env python3

import sys

def split_levels(report: str) -> list[int]:
    levels = report.split()
    converted_report = list(map(int, levels))
    return converted_report
    
def check_report_safety(report: list[int]) -> bool:
    increase = False
    decrease = False
    difference = 0
    for i in range(len(report)-1):
        if difference > 3 or report[i] == report[i+1]:
            #print(difference)
            #print(report[i], report)
        #if difference < 3:
            return False
            print(report[i], report[i+1])
            print("false tree")
        elif report[i] > report[i+1]:
            decrease = True
            difference = report[i] - report[i+1]
        elif report[i] < report[i+1]:
            increase = True
            difference = report[i+1] - report[i]
        print(increase, decrease, difference)
    if increase != decrease:   
        return True

    
            
    


def main():
    reports = []
    with open("../inputs/day_2_input.txt" , "r") as data:
        for report in data:
            reports.append(report.rstrip('\n'))     

    converted_reports = []
    for report in reports:
        converted_reports.append(split_levels(report))
        
    # print(len(converted_reports))
    count_safe_reports = 0
    for report in converted_reports:
        if check_report_safety(report):
            count_safe_reports = count_safe_reports + 1
   
    print(f"We have {str(count_safe_reports)} safe reports." )     

if __name__ == "__main__":
    main()
