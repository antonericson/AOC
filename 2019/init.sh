#!/bin/sh
if [ ! -d "$1" ]; then
    mkdir $1
    touch $1/input.txt $1/debug.txt $1/solution.py
    echo "def main():
    inputLines =  open(\"debug.txt\", \"r\").readlines()

    print(f'Part one: ')
    print(f'Part two: ')

if __name__ == \"__main__\":
    main()" >> $1/solution.py
    echo "$1/ created!"
else
    echo "Files for day $1 already exist"
fi