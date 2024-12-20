# pylint: disable=missing-function-docstring, missing-module-docstring, unused-argument
import time
import re

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
    for line in input_lines:
        mul_list = re.findall(r'mul\((\d+),(\d+)\)', line)
        for tuple in mul_list:
            result += int(tuple[0]) * int(tuple[1])
        
    print(f'Part one: {result}')

def solve_two(input_lines):
    result = 0
    line = ''.join(input_lines)
    mul_matches = list(re.finditer(r'mul\((\d+),(\d+)\)', line))
    do_matches = list(re.finditer(r'do()', line))
    dont_matches = list(re.finditer(r'don\'t()', line))
    for mul_match in mul_matches:
        enabled = True
        start = mul_match.start()
        i = start-1
        while i >= 0:
            if i in [match.end() for match in do_matches]:
                enabled = True
                break
            if i in [match.end() for match in dont_matches]:
                enabled = False
                break
            i -= 1
        if enabled:
            result += int(mul_match.group(1)) * int(mul_match.group(2))
            
    print(f'Part two: {result}')

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

