#!/bin/sh
if [ ! -d "$1" ]; then
    mkdir $1
    touch $1/input.txt $1/debug.txt $1/solution.py
    echo "import time

def main():
    with open(\"debug.txt\", \"r\") as file:
        input = file.readlines()
        st1 = time.time()
        solve_one(input)
        et1 = time.time()
        print(f'Part one solved in: {print_time(st1, et1)}')


        st2 = time.time()
        solve_two(input)
        et2 = time.time()
        print(f'Part two solved in: {print_time(st2, et2)}')

def solve_one(input):

    print(f'Part one: {\"\"}')
    return # Return nothing, print results before this

def solve_two(input):

    print(f'Part two: {\"\"}')
    return # Return nothing, print results before this


def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == \"__main__\":
    main()
" >> $1/solution.py
    echo "$1/ created!"
else
    echo "Files for day $1 already exist"
fi