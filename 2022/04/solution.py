import time

def main():
    with open("input.txt", "r") as file:
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

    totalOverlap = 0
    for pair in input:
        elfOne, elfTwo = pair.strip().split(',')
        listOne = [int(x) for x in elfOne.split('-')]
        listTwo = [int(x) for x in elfTwo.split('-')]
        rangeOne = range(listOne[0], listOne[1]+1)
        rangeTwo = range(listTwo[0], listTwo[1]+1)        
        
        if(isRangeSubsetOf(rangeOne, rangeTwo)):
            totalOverlap += 1

    print(f'Part one: {totalOverlap}')
    return # Return nothing, print results before this

def solve_two(input):

    anyOverlap = 0
    for pair in input:
        elfOne, elfTwo = pair.strip().split(',')
        listOne = [int(x) for x in elfOne.split('-')]
        listTwo = [int(x) for x in elfTwo.split('-')]
        rangeOne = range(listOne[0], listOne[1]+1)
        rangeTwo = range(listTwo[0], listTwo[1]+1)        
        
        if(hasOverlap(rangeOne, rangeTwo)):
            anyOverlap += 1
    
    print(f'Part two: {anyOverlap}')
    return # Return nothing, print results before this

def isRangeSubsetOf(rangeOne, rangeTwo):
    return (rangeOne.start in rangeTwo and rangeOne[-1] in rangeTwo) or (rangeTwo.start in rangeOne and rangeTwo[-1] in rangeOne)

def hasOverlap(rangeOne, rangeTwo):
        return (rangeOne.start in rangeTwo or rangeOne[-1] in rangeTwo) or (rangeTwo.start in rangeOne or rangeTwo[-1] in rangeOne)


def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

