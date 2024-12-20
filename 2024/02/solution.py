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
    safe_reports = 0
    for report in input_lines:
        report = [int(i) for i in report.strip().split()]
        if report != sorted(report) and report != sorted(report, reverse=True):
            continue
        is_safe = True
        for i in range(len(report)-1):
            if abs(report[i] - report[i+1]) > 3 or abs(report[i] - report[i+1]) == 0:
                is_safe = False
                break
        if is_safe:
            safe_reports += 1
            

    print(f'Part one: {safe_reports}')

def is_valid_sequence(numbers):
    if len(numbers) < 2:
        return True
    for i in range(len(numbers)-1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff == 0 or diff > 3:
            return False
    return True

def solve_two(input_lines):
    safe_reports = 0
    for report in input_lines:
        numbers = [int(i) for i in report.strip().split()]
        # Try removing each number once
        for i in range(len(numbers)):
            temp_numbers = numbers[:i] + numbers[i+1:]
            if (temp_numbers == sorted(temp_numbers) or 
                temp_numbers == sorted(temp_numbers, reverse=True)) and \
                is_valid_sequence(temp_numbers):
                safe_reports += 1
                break            

    print(f'Part two: {safe_reports}')

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

