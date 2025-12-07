# pylint: disable=missing-function-docstring, missing-module-docstring, unused-argument
import itertools
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
    nr_of_fresh_ids = 0
    separator_index = input_lines.index("\n")
    fresh_range_arrays = [[int(r) for r in line.strip().split("-")] for line in input_lines[:separator_index]]
    fresh_id_ranges = []
    for range_array in fresh_range_arrays:
        fresh_id_ranges.append(range(range_array[0], range_array[1]+1))
            
    ids = [int(line.strip()) for line in input_lines[separator_index+1:]]
    

    for id in ids:
        for fresh_range in fresh_id_ranges:
            if id in fresh_range:
                nr_of_fresh_ids += 1
                break

    print(f'Part one: {nr_of_fresh_ids}')

def solve_two(input_lines):
    separator_index = input_lines.index("\n")
    fresh_range_arrays = [[int(r) for r in line.strip().split("-")] for line in input_lines[:separator_index]]
    # Sort ranges by start
    sorted_ranges = sorted(fresh_range_arrays, key=lambda x: x[0])
    merged = []
    for start, end in sorted_ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    # Count unique IDs
    nr_of_fresh_ids = sum(end - start + 1 for start, end in merged)
    print(f'Part two: {nr_of_fresh_ids}')

def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

