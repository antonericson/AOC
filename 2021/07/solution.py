def cleanInput(inputLine):
    return [int(i) for i in inputLine.split(",")]

def alignHorizontallyConstantFuelRate(inputLine):
    positionList = cleanInput(inputLine)
    
    potentialPositionsList = [0] * max(positionList)
    for i in range(max(positionList)):
        for crabPos in positionList:
            potentialPositionsList[i] += (max(crabPos, i) - min(crabPos, i))        
    
    return min(potentialPositionsList)
        
def alignHorizontallyIncreasingFuelRate(inputLine):
    positionList = cleanInput(inputLine)
    
    potentialPositionsList = [0] * max(positionList)
    for i in range(max(positionList)):
        for crabPos in positionList:
            potentialPositionsList[i] += (sum(range((max(crabPos, i) - min(crabPos, i))+1)))        
    
    return min(potentialPositionsList)

def main():
    inputLine = open("input.txt", "r").readlines()[0]
    
    print(f'Part 1: {alignHorizontallyConstantFuelRate(inputLine)}')
    print(f'Part 2: {alignHorizontallyIncreasingFuelRate(inputLine)}')


if __name__ == "__main__":
    main()