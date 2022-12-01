input_lines =  [int(i) for i in open("input.txt", "r").readlines()]

def solvePartOne():
    numberOfIncreases = 0
    prevNumber = int(input_lines[0])
    
    for number in input_lines:
        if (int(number) > int(prevNumber)):
            numberOfIncreases += 1
            
        prevNumber = number

    return numberOfIncreases

def solvePartTwo():
    numberOfIncreases = 0
    prevSum = input_lines[0] + input_lines[1] + input_lines[2]
    
    for i in range(0, len(input_lines)):
        if len(input_lines) <= i+2:
            break
        
        currentSum = input_lines[i] + input_lines[i+1] + input_lines[i+2]
        if currentSum > prevSum:
            numberOfIncreases += 1

        prevSum = currentSum

    return numberOfIncreases

def main():
    print(f'Part one: {solvePartOne()}')
    print(f'Part two: {solvePartTwo()}')

if __name__ == "__main__":
    main()