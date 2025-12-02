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
    total = 0
    for id_range in input_lines[0].split(","):
        start_id, end_id = id_range.split("-")

        for i in range(int(start_id), int(end_id)+1):
            i = str(i)
            if (len(i)%2 == 0):
                l_h = i[:len(i)//2]
                r_h = i[len(i)//2:]
                if(l_h == r_h):
                    total += int(i)

    print(f'Part one: {total}')

def solve_two(input_lines):
    total = 0
    for id_range in input_lines[0].split(","):
        start_id, end_id = id_range.split("-")

        for i in range(int(start_id), int(end_id)+1):
            i = str(i)
            half = len(i)//2
            found_match = False

            for group_size in range(1, half+1):
                group = i[:group_size]
                is_match = True
                for start in range(0, len(i), group_size):
                    if i[start:start+group_size] != group:
                        is_match = False
                        break
                if is_match:
                    found_match = True
                    break

            if found_match:
                total += int(i)

    print(f'Part two: {total}')

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

