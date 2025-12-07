# pylint: disable=missing-function-docstring, missing-module-docstring, unused-argument
import time
import copy

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
    matrix = [list(i.strip()) for i in input_lines]
    max_y = len(matrix)
    max_x = len(matrix[0])
    first_y = 0
    first_x = 0
    last_y = max_y-1
    last_x = max_x-1
    
    for y in range(max_y):
        for x in range(max_x):
            current_count = 0
            # Check all directions
            # Return false if >3
            if (matrix[y][x] != "@"):
                continue
            if (y != first_y):
                #Check N
                if matrix[y-1][x] == "@":
                    current_count += 1
            if (y != first_y and x != last_x):
                #Check NE
                if matrix[y-1][x+1] == "@":
                    current_count += 1
            if (x != last_x):
                #Check E
                if matrix[y][x+1] == "@":
                    current_count += 1
            if (x != last_x and y != last_y):
                # Check SE
                if matrix[y+1][x+1] == "@":
                    current_count += 1
            if (y != last_y):
                # Check S
                if matrix[y+1][x] == "@":
                    current_count += 1
            if (y != last_y and x != first_x):
                #Check SW
                if matrix[y+1][x-1] == "@":
                    current_count += 1
            if (x != first_x):
                # Check W
                if matrix[y][x-1] == "@":
                    current_count += 1
            if (x != first_x and y != first_y):
                if matrix[y-1][x-1] == "@":
                    current_count += 1
            if current_count < 4:
                result += 1

    print(f'Part one: {result}') # 1564

def solve_two(input_lines):
    removed_rolls = 0
    matrix = [list(i.strip()) for i in input_lines]
    max_y = len(matrix)
    max_x = len(matrix[0])
    first_y = 0
    first_x = 0
    last_y = max_y-1
    last_x = max_x-1

    running = True
    loop = 0
    while(running):
        loop += 1
        new_matrix = copy.deepcopy(matrix)
        for y in range(max_y):
            for x in range(max_x):
                current_count = 0
                # Check all directions
                # Return false if >3
                if (matrix[y][x] != "@"):
                    continue
                if (y != first_y):
                    #Check N
                    if matrix[y-1][x] == "@":
                        current_count += 1
                if (y != first_y and x != last_x):
                    #Check NE
                    if matrix[y-1][x+1] == "@":
                        current_count += 1
                if (x != last_x):
                    #Check E
                    if matrix[y][x+1] == "@":
                        current_count += 1
                if (x != last_x and y != last_y):
                    # Check SE
                    if matrix[y+1][x+1] == "@":
                        current_count += 1
                if (y != last_y):
                    # Check S
                    if matrix[y+1][x] == "@":
                        current_count += 1
                if (y != last_y and x != first_x):
                    #Check SW
                    if matrix[y+1][x-1] == "@":
                        current_count += 1
                if (x != first_x):
                    # Check W
                    if matrix[y][x-1] == "@":
                        current_count += 1
                if (x != first_x and y != first_y):
                    # Check NW
                    if matrix[y-1][x-1] == "@":
                        current_count += 1
                if current_count < 4:
                    new_matrix[y][x] = "."
                    removed_rolls += 1

        if matrix == new_matrix:
            running = False
        matrix = new_matrix

    print(f'Part two: {removed_rolls}')

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

