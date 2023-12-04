# pylint: disable=missing-function-docstring, missing-module-docstring, unused-argument
import time
import re


def main():
    with open("input.txt", "r", encoding="UTF-8") as file:
        input_lines = file.readlines()
        st1 = time.time()
        solve_one(input_lines)
        et1 = time.time()
        print(f"Part one solved in: {print_time(st1, et1)}")

        st2 = time.time()
        solve_two(input_lines)
        et2 = time.time()
        print(f"Part two solved in: {print_time(st2, et2)}")


def solve_one(schematic):
    part_numbers = []
    symbols = []
    valid_coords = set()
    numbers = []
    symbol_pattern = r"[^\w.\n]|[_]"

    for y, line in enumerate(schematic):
        for symbol_matcher in re.finditer(symbol_pattern, line):
            symbols.append((y, symbol_matcher.span()[0]))
        for number_matcher in re.finditer(r"\d+", line):
            number_coords = [(y, number_matcher.start())]

            x = number_matcher.start() + 1
            while x < number_matcher.end():
                number_coords.append((y, x))
                x += 1
            numbers.append((number_matcher.group(), number_coords))
    for symbol in symbols:
        valid_coords = valid_coords.union(
            set((coord[0], coord[1]) for coord in list(adjac(symbol)))
        )

    for (number, coords) in numbers:
        if any(coord in valid_coords for coord in coords):
            part_numbers.append(int(number))
    print(f"Part one: {sum(part_numbers)}")


def adjac(ele, sub=[]):
    if not ele:
        yield sub
    else:
        yield from (
            idx
            for j in range(ele[0] - 1, ele[0] + 2)
            for idx in adjac(ele[1:], sub + [j])
        )


def solve_two(input_lines):
    print(f'Part two: {""}')


def print_time(st, et):
    res = et - st
    if res < 1:
        return f"{res * 1000} milliseconds"
    return f"{res} seconds"


if __name__ == "__main__":
    main()
