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

    # One-liner
    print(sum([abs(int(sorted([left.strip().split("   ")[0] for left in input_lines])[i]) - int(sorted([right.strip().split("   ")[1] for right in input_lines])[i])) for i in range(len(input_lines))]))
    
    # Cody :-)
    print(sum(abs(a - b) for a, b in zip(sorted(int(line.split()[0]) for line in input_lines), sorted(int(line.split()[1]) for line in input_lines))))

    # Initial solution
    total_distance = 0
    left_list = []
    right_list = []
    
    
    for x, y in [line.strip().split("   ") for line in input_lines]:
        left_list.append(int(x))
        right_list.append(int(y))
    left_list.sort()
    right_list.sort()
    for i in range(len(left_list)):
        tmp = abs(left_list[i] - right_list[i])
        total_distance += tmp
        
    print(f'Part one: {total_distance}')

def solve_two(input_lines):

    print(f'Part two: {""}')

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

