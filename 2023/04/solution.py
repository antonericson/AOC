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
    for scratchcard in input_lines:
        winning_numbers, your_numbers = scratchcard.split(":")[1].strip().split(" | ")
        winning_numbers = [int(number) for number in winning_numbers.strip().replace("  ", " ").split(" ")]
        your_numbers = [int(number) for number in your_numbers.strip().replace("  ", " ").split(" ")]
        number_of_matches = set(winning_numbers).intersection(your_numbers)
        result += int(2 ** (len(number_of_matches) - 1))
    print(f'Part one: {result}')

def solve_two(input_lines):
    scratchcards = [1] * len(input_lines)
    for i, scratchcard in enumerate(input_lines):
        number_of_matches = 0
        winning_numbers, your_numbers = scratchcard.split(":")[1].strip().split(" | ")
        winning_numbers = [int(number) for number in winning_numbers.strip().replace("  ", " ").split(" ")]
        your_numbers = [int(number) for number in your_numbers.strip().replace("  ", " ").split(" ")]
        number_of_matches = len(set(winning_numbers).intersection(your_numbers))
        for n in range(1, number_of_matches+1):
            scratchcards[i+n] += 1 * scratchcards[i]

    print(f'Part two: {sum(scratchcards)}')

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()
