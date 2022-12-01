def createOctopusMap(inputLines):
    newMap = []
    for line in inputLines:
        newMap.append([int(i) for i in list(line.strip())])
    return newMap

def calculateFlashes(inputLines, steps):
    octopusMap = createOctopusMap(inputLines)
    print(octopusMap)
    print()
    for i in range(0, steps):
        print(i)
        for rowIndex, row in enumerate(octopusMap):
            octopusMap[rowIndex] = list(map(lambda x:x+1, row))
        print(octopusMap)
        for rowIndex, row in enumerate(octopusMap):
            print("ROW: ",row)
            for colIndex, cell in enumerate(row):
                if cell == 10:
                    flashOctopus(octopusMap, rowIndex, colIndex)
                    octopusMap[rowIndex][colIndex] = 0

    for row in octopusMap:
        print(row)
                        
                    
def flashOctopus(octopusMap, rowIndex, colIndex):
    print(octopusMap, rowIndex, colIndex)
    
    if rowIndex < len(octopusMap):
        #check down
        octopusMap[rowIndex+1][colIndex] += 1
        if octopusMap[rowIndex+1][colIndex] == 10:
            flashOctopus(octopusMap, rowIndex+1, colIndex)
    if colIndex < len(octopusMap[0]):
        #check right
        octopusMap[rowIndex][colIndex+1] += 1
        if octopusMap[rowIndex][colIndex+1] == 10:
            flashOctopus(octopusMap, rowIndex, colIndex+1)
    if rowIndex >= 0:
        #check up
        octopusMap[rowIndex-1][colIndex] += 1
        if octopusMap[rowIndex-1][colIndex] == 10:
            flashOctopus(octopusMap, rowIndex-1, colIndex)
    if colIndex >= 0:
        #chekc left
        octopusMap[rowIndex][colIndex-1] += 1
        if octopusMap[rowIndex][colIndex-1] == 10:
            flashOctopus(octopusMap, rowIndex, colIndex-1)
    if rowIndex < len(octopusMap) and colIndex < len(octopusMap[0]):
        #check down right
        octopusMap[rowIndex+1][colIndex+1] += 1
        if octopusMap[rowIndex+1][colIndex+1] == 10:
            flashOctopus(octopusMap, rowIndex+1, colIndex+1)
    if rowIndex < len(octopusMap) and colIndex >= 0:
        #check down left
        octopusMap[rowIndex+1][colIndex-1] += 1
        if octopusMap[rowIndex+1][colIndex-1] == 10:
            flashOctopus(octopusMap, rowIndex+1, colIndex-1)
    if rowIndex >= 0 and colIndex < len(octopusMap[0]):
        #check up right
        octopusMap[rowIndex-1][colIndex+1] += 1
        if octopusMap[rowIndex-1][colIndex+1] == 10:
            flashOctopus(octopusMap, rowIndex-1, colIndex+1)
    if rowIndex >= 0 and colIndex >= 0:
        #check up left
        octopusMap[rowIndex-1][colIndex-1] += 1
        if octopusMap[rowIndex-1][colIndex-1] == 10:
            flashOctopus(octopusMap, rowIndex-1, colIndex-1)
    return octopusMap

def main():
    inputLines =  open("debug2.txt", "r").readlines()

    print(f'Part one: {calculateFlashes(inputLines, 1)}')
    print(f'Part two: ')

if __name__ == "__main__":
    main()
