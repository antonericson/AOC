from collections import Counter
from os import stat


def cleanInput(inputLine):
    return [int(i) for i in inputLine.split(",")]

def simulateGrowth(inputLine, days):

    initialFishData = cleanInput(inputLine)
    state = [{}.setdefault(i, 0) for i in range(9)]
    for i in initialFishData:
        state[i] += 1

    for _ in range(days):
        nrOfDayZero = state[0]
        state[0] = state[1]
        state[1] = state[2]
        state[2] = state[3]
        state[3] = state[4]
        state[4] = state[5]
        state[5] = state[6]
        state[6] = state[7] + nrOfDayZero
        state[7] = state[8]
        state[8] = nrOfDayZero

    return sum(state)


def main():
    inputLine = open("input.txt", "r").readlines()[0]

    print(f'Part 1: {simulateGrowth(inputLine, 80)}')
    # 1741486610023786 is too high
    print(f'Part 2: {simulateGrowth(inputLine, 256)}')


if __name__ == "__main__":
    main()