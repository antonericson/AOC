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
    result = 0
    for bank in input_lines:
        number_array = [int(n) for n in list(bank.strip())]
        bank_number = 0
        for i in reversed(range(1,10)):
            if (i in number_array and number_array.index(i) < len(number_array)-1):
                bank_number = int(str(i)+str(max(number_array[number_array.index(i)+1:])))
                break
        result += bank_number


    print(f'Part one: {result}')

def find_largest_with_padding_right(list, padding_right):
    if padding_right == -1:
        return ""
    for i in reversed(range(1,10)):
        if(i in list and list.index(i) < len(list)-padding_right):
            return str(i) + find_largest_with_padding_right(list[list.index(i)+1:], padding_right-1)

def solve_two(input_lines):
    result = 0
    for bank in input_lines:
        number_array = [int(n) for n in list(bank.strip())]
        bank_number = int(find_largest_with_padding_right(number_array, 11))
        result += bank_number

    print(f'Part two: {result}')

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()
