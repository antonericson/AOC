# pylint: disable=missing-function-docstring, missing-module-docstring, unused-argument
import time

def main():
    with open('input.txt', 'r', encoding='UTF-8') as file:
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
        cubes = {"red": 12, "green": 13, "blue": 14}
        game_number = line.split(" ")[1].replace(':','')
        game_data = line.strip().split(":")[1::][0]
        sets = game_data.strip().split(";")
        is_possible = True
        for game_set in sets:
            for reveal in game_set.strip().split(', '):
                amount, color = reveal.split(" ")
                if cubes[color] - int(amount) < 0:
                    is_possible = False
                    break
        if is_possible:
            result = result + int(game_number)

    print(f'Part one: {result}')

def solve_two(input_lines):
    result = 0
    for line in input_lines:
        cubes = {"red": 0, "green": 0, "blue": 0}
        game_data = line.strip().split(":")[1::][0]
        sets = game_data.strip().split(";")
        for game_set in sets:
            for reveal in game_set.strip().split(', '):
                amount, color = reveal.split(" ")
                if cubes[color] < int(amount):
                    cubes[color] = int(amount)
        set_power = cubes["red"] * cubes["green"] * cubes["blue"]
        result = result + set_power

    print(f'Part two: {result}')

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()
