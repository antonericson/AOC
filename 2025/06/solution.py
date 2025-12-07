# pylint: disable=missing-function-docstring, missing-module-docstring, unused-argument
import time
import math

def main():
    with open("input.txt", "r", encoding="UTF-8") as file:
        input_lines = file.readlines()
        st1 = time.time()
        solve_one(input_lines)
        et1 = time.time()
        print(f'Part one solved in: {print_time(st1, et1)}')


        st2 = time.time()
        solve_two(input_lines)
        et2 = time.time()
        print(f'Part two solved in: {print_time(st2, et2)}')

def solve_one(input_lines):
    original_matrix = []
    for line in input_lines:
        original_matrix.append(line.strip().split())
    
    total = 0
    for calculation_list in zip(*reversed(original_matrix)):
        if(calculation_list[0] == "+"):
            total += sum([int(i) for i in calculation_list[1:]])
        if(calculation_list[0] == "*"):
            total += math.prod([int(i) for i in calculation_list[1:]])

    print(f'Part one: {total}')

def solve_two(input_lines):
    total = 0
    matrix = []
    for line in zip(*reversed(input_lines)):
        matrix.append(line)
    
    matrix.append([""])

    current_numbers = []
    for row in matrix:
        if len(set(row)) == 1:
            #Reset and calculate
            if operand == "+":
                total += sum(current_numbers)
            if operand == "*":
                total += math.prod(current_numbers)
            current_numbers = []
            continue
            
        if row[0] != " ":
            operand = row[0]

        number = "".join(reversed(row[1:])).strip()
        if number != "":
            current_numbers.append(int(number))
        
        


    print(f'Part two: {total}')

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

