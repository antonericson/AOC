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
    tmpStacks = []
    stacks = {}
    numberOfStacks = 0
    startOfInstructions = 0
    heightOfMap = 0

    for index, line in enumerate(input):
        if line == '\n':
            startOfInstructions = index + 1
            break
        if '1' in line:
            numberOfStacks = int(line.strip().replace(' ','')[-1])
        else:
            tmpStacks.append(line.replace('    ',' ').replace('\n', '').split(' '))
            heightOfMap += 1
    
    for x in range(0,int(numberOfStacks)):
        for column in range(0, heightOfMap).__reversed__():
            if x in stacks.keys():
                stacks[x] = stacks[x] + (tmpStacks[column][x].replace(' ','').replace('[','').replace(']',''))
            else:
                stacks[x] = tmpStacks[column][x].replace(' ','').replace('[','').replace(']','')
        
    for instruction in input[startOfInstructions:]:
        currentInstructions = instruction.strip().replace('move ','').replace('from ','').replace('to ','').split(' ');
        numberToMove, fromStack, toStack = [int(x) for x in currentInstructions]
        fromStack -= 1
        toStack -= 1
        stacks[toStack] += stacks[fromStack][numberToMove*-1:][::-1]
        stacks[fromStack] = stacks[fromStack][:numberToMove*-1]
        
    res = ''
    for stack in stacks:
        res += stacks[stack][-1:]
        
    print(f'Part one: {res}')
    return # Return nothing, print results before this

def solve_two(input):
        tmpStacks = []
        stacks = {}
        numberOfStacks = 0
        startOfInstructions = 0
        heightOfMap = 0

        for index, line in enumerate(input):
            if line == '\n':
                startOfInstructions = index + 1
                break
            if '1' in line:
                numberOfStacks = int(line.strip().replace(' ','')[-1])
            else:
                tmpStacks.append(line.replace('    ',' ').replace('\n', '').split(' '))
                heightOfMap += 1
        
        for x in range(0,int(numberOfStacks)):
            for column in range(0, heightOfMap).__reversed__():
                if x in stacks.keys():
                    stacks[x] = stacks[x] + (tmpStacks[column][x].replace(' ','').replace('[','').replace(']',''))
                else:
                    stacks[x] = tmpStacks[column][x].replace(' ','').replace('[','').replace(']','')
            
        for instruction in input[startOfInstructions:]:
            currentInstructions = instruction.strip().replace('move ','').replace('from ','').replace('to ','').split(' ');
            numberToMove, fromStack, toStack = [int(x) for x in currentInstructions]
            fromStack -= 1
            toStack -= 1
            stacks[toStack] += stacks[fromStack][numberToMove*-1:]
            stacks[fromStack] = stacks[fromStack][:numberToMove*-1]
            
        res = ''
        for stack in stacks:
            res += stacks[stack][-1:]
            
        print(f'Part two: {res}')
        return # Return nothing, print results before this


def print_time(st, et):
    res = et - st
    if res < 1:
        return f'{res * 1000} milliseconds'
    return f'{res} seconds'


if __name__ == "__main__":
    main()

