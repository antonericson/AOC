# pylint: disable=missing-function-docstring, missing-module-docstring, unused-argument
import time

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
    number_of_zeros = 0
    current_pos = 50

    for line in input_lines:
        letter = line[0]
        amount = int(line[1::])


        if (letter == "L"):
            current_pos -= amount
        else:
            current_pos += amount

        if (current_pos > 99 or current_pos < 0):
            current_pos = (current_pos % 100)

        if current_pos == 0:
            number_of_zeros += 1

    print(f'Part one: {number_of_zeros}')

def solve_two(input_lines):

    number_of_zeros = 0
    current_pos = 50

    for line in input_lines:
        letter = line[0]
        amount = int(line[1::])    
        for i in range(amount):
            if letter == "L":
                current_pos -= 1
            else:
                current_pos += 1

            if current_pos == 100:
                current_pos = 0
            
            if current_pos == -1:
                current_pos = 99
            
            if current_pos == 0:
                number_of_zeros += 1
            
    print(f'Part two: {number_of_zeros}')

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

