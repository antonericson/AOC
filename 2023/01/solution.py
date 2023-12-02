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
    for line in input_lines:
        first_number = 0
        last_number = 0
        for char in line:
            try:
                first_number = int(char)
            except ValueError:
                continue
            break

        for char in reversed(line):
            try:
                last_number = int(char)
            except ValueError:
                continue
            break
        result += int(str(first_number) + str(last_number))
    print(f'Part one: {result}')

def solve_two(input_lines):
    numbers = {'one':'o1e', 'two':'t2o', 'three':'t3e', 'four':'f4r', 'five':'f5e', 'six':'s6x',
               'seven':'s7n', 'eight':'e8t', 'nine':'n9e'}
    result = 0
    for line in input_lines:
        for i in range(0,10):
            options = {}
            tmp_line = ""
            for word, number in numbers.items():
                tmp_line = line.replace(word, str(number))
                if tmp_line != line:
                    options[word] = line.find(word)
            if options:
                print(options)
            print(line)
            options = sorted(options.items(), key=lambda item: item[1])
            for replacement in options:
                print(replacement)
                line_before_change = line
                line = line.replace(replacement[0], str(numbers[replacement[0]]))
                if line_before_change != line:
                    print("break")
                    break
            for replacement in reversed(options):
                print(replacement)
                line_before_change = line
                line = line.replace(replacement[0], str(numbers[replacement[0]]))
                if line_before_change != line:
                    print("break")
                    break
            print(line)
        for char in line:
            try:
                first_number = int(char)
            except ValueError:
                continue
            break

        for char in reversed(line):
            try:
                last_number = int(char)
            except ValueError:
                continue
            break
        int(str(first_number) + str(last_number))
        result += int(str(first_number) + str(last_number))
    print(f'Part two: {result}')


def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()
