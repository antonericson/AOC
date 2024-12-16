# pylint: disable=missing-function-docstring, missing-module-docstring, unused-argument
import time

def main():
    with open("debug.txt", "r", encoding="UTF-8") as file:
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
        report = report.strip().split()
        print("report", report)
        print(sorted(report))
        print(sorted(report, reverse=True))
        if report != sorted(report) or report != sorted(report, reverse=True):
            continue
        for i in range(len(report)-1):
            print(abs(report[i] - report[i+1]))
            if abs(report[i] - report[i+1]) > 3:
                continue
            safe_reports += 1
            

    print(f'Part one: {safe_reports}')

def solve_two(input_lines):

    print(f'Part two: {""}')

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

