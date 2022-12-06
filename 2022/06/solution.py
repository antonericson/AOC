import time

def main():
    with open("input.txt", "r") as file:
        input = file.read()
        st1 = time.time()
        solve_one(input)
        et1 = time.time()
        print(f'Part one solved in: {print_time(st1, et1)}')


        st2 = time.time()
        solve_two(input)
        et2 = time.time()
        print(f'Part two solved in: {print_time(st2, et2)}')

def solve_one(input):
    isMarkerFound = False
    markerIndex = 0
    si = 0
    ei = 4
    while not isMarkerFound:
        if ei >= len(input):
            break
        if(len(set(input[si:ei])) == 4):
            isMarkerFound = True
            markerIndex = ei
        si += 1
        ei += 1

    print(f'Part one: {markerIndex}')
    return # Return nothing, print results before this

def solve_two(input):
    isMarkerFound = False
    markerIndex = 0
    si = 0
    ei = 14
    while not isMarkerFound:
        if ei >= len(input):
            break
        if(len(set(input[si:ei])) == 14):
            isMarkerFound = True
            markerIndex = ei
        si += 1
        ei += 1
        
    print(f'Part two: {markerIndex}')
    return # Return nothing, print results before this


def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

