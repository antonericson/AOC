import math

def generateHeatmap(inputLines):
    heatMap = []
    for row in inputLines:
        heatMap.append([int(i) for i in list(row.strip())])
    return heatMap

def findLowPoints(heatMap):
    lowPoints = []
    for rowIndex, row in enumerate(heatMap):
        for colIndex, number in enumerate(row):
            isLowPoint = False
            if rowIndex > 0:
                # check above
                isLowPoint = number < heatMap[rowIndex-1][colIndex]
                if not isLowPoint:
                    continue
            if rowIndex < len(heatMap)-1:
                #check below
                isLowPoint = number < heatMap[rowIndex+1][colIndex]
                if not isLowPoint:
                    continue
            if colIndex > 0:
                #check left (-1)
                isLowPoint = number < heatMap[rowIndex][colIndex-1]
                if not isLowPoint:
                    continue
            if colIndex < len(row)-1:
                #check right (+1)
                isLowPoint = number < heatMap[rowIndex][colIndex+1]
                if not isLowPoint:
                    continue
            if isLowPoint:
                lowPoints.append(number)
    return lowPoints

def findLowPointsCoordinates(heatMap):
    lowPoints = []
    for rowIndex, row in enumerate(heatMap):
        for colIndex, number in enumerate(row):
            isLowPoint = False
            if rowIndex > 0:
                # check above
                isLowPoint = number < heatMap[rowIndex-1][colIndex]
                if not isLowPoint:
                    continue
            if rowIndex < len(heatMap)-1:
                #check below
                isLowPoint = number < heatMap[rowIndex+1][colIndex]
                if not isLowPoint:
                    continue
            if colIndex > 0:
                #check left (-1)
                isLowPoint = number < heatMap[rowIndex][colIndex-1]
                if not isLowPoint:
                    continue
            if colIndex < len(row)-1:
                #check right (+1)
                isLowPoint = number < heatMap[rowIndex][colIndex+1]
                if not isLowPoint:
                    continue
            if isLowPoint:
                lowPoints.append([rowIndex, colIndex])
    return lowPoints

def findRiskLevelOfHeatmap(inputLines):
    heatMap = generateHeatmap(inputLines)
    lowPoints = findLowPoints(heatMap)
    return sum(lowPoints) + len(lowPoints)

def findBasins(inputLines):
    heatMap = generateHeatmap(inputLines)
    lowPointCoordinates = findLowPointsCoordinates(heatMap)
    basins = []
    for lowPointCoordinate in lowPointCoordinates:
        basins.append(findBasin(heatMap, lowPointCoordinate[0], lowPointCoordinate[1],)) 
 
    return basins
 

def findBasin(heatMap, rowIndex, colIndex):
    if rowIndex >= len(heatMap) or colIndex >= len(heatMap[0]) or rowIndex < 0 or colIndex < 0:
        return 0
    
    currentValue = heatMap[rowIndex][colIndex]
    if (currentValue < 9):
        heatMap[rowIndex][colIndex] = 10
        return 1 + findBasin(heatMap, rowIndex+1, colIndex)+findBasin(heatMap, rowIndex, colIndex+1,)+findBasin(heatMap, rowIndex-1, colIndex)+findBasin(heatMap, rowIndex, colIndex-1)
    return 0

def findLargestBasinProduct(inputLines):
    basins = findBasins(inputLines)
    basins.sort(reverse=True)
    largestBasins = basins[:3]
    return math.prod(largestBasins)

def main():
    inputLines =  open("input.txt", "r").readlines()
    
    print(f'Part one: {findRiskLevelOfHeatmap(inputLines)}')
    print(f'Part two: {findLargestBasinProduct(inputLines)}')

if __name__ == "__main__":
    main()
