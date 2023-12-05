# pylint: disable=missing-function-docstring, missing-module-docstring, unused-argument
import time
import re


def main():
    with open("input.txt", "r", encoding="UTF-8") as file:
        input_lines = file.read()
        st1 = time.time()
        solve_one(input_lines)
        et1 = time.time()
        print(f"Part one solved in: {print_time(st1, et1)}")

        st2 = time.time()
        solve_two(input_lines)
        et2 = time.time()
        print(f"Part two solved in: {print_time(st2, et2)}")


def solve_one(input_text):
    seeds = [
        int(seed)
        for seed in input_text.split("\n")[0].replace("seeds:", "").strip().split(" ")
    ]
    locations = []
    input_lines = input_text.strip().split("\n")
    for seed in seeds:
        li = 3
        current_number = seed
        while li < len(input_lines):
            if input_lines[li] == "" or "map:" in input_lines[li]:
                li += 1
                continue
            destination_start, source_start, number_range = [
                int(n) for n in input_lines[li].split(" ")
            ]
            if (
                source_start <= current_number
                and (source_start + number_range) >= current_number
            ):
                current_number = destination_start + abs(source_start - current_number)
                if li + 1 == len(input_lines):
                    break
                while input_lines[li + 1] != "":
                    if li + 1 == len(input_lines) - 1:
                        break
                    li += 1
                    continue
            li += 1
        locations.append(current_number)

    print(f"Part one: {min(locations)}")


def solve_two(input_text):
    seed_row = [
        int(seed)
        for seed in input_text.split("\n")[0].replace("seeds:", "").strip().split(" ")
    ]
    seeds = []
    si = 0
    while si < len(seed_row)-1:
        seeds.extend([*range(seed_row[si], seed_row[si]+seed_row[si+1])])
        si += 2
    print(seeds)
    locations = []
    input_lines = input_text.strip().split("\n")
    for seed in seeds:
        li = 3
        current_number = seed
        while li < len(input_lines):
            if input_lines[li] == "" or "map:" in input_lines[li]:
                li += 1
                continue
            destination_start, source_start, number_range = [
                int(n) for n in input_lines[li].split(" ")
            ]
            if (
                source_start <= current_number
                and (source_start + number_range) >= current_number
            ):
                current_number = destination_start + abs(source_start - current_number)
                if li + 1 == len(input_lines):
                    break
                while input_lines[li + 1] != "":
                    if li + 1 == len(input_lines) - 1:
                        break
                    li += 1
                    continue
            li += 1
        locations.append(current_number)
    print(f"Part two: {min(locations)}")


def print_time(st, et):
    res = et - st
    if res < 1:
        return f"{res * 1000} milliseconds"
    return f"{res} seconds"


if __name__ == "__main__":
    main()
