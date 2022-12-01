def prettyPrintMap(map):
    for line in map:
        print(line)

def getLineSegments(inputLines):
    # [ [[1,2],[1,3]], [[1,5],[2,5]] ]
    coordinateList = []
    for lineIndex, line in enumerate(inputLines):
        splitCoords = line.strip().split(" -> ")
        coordinateList.append([])
        for coordPair in splitCoords:
            coordinateList[lineIndex].append([int(i) for i in coordPair.split(",")])
    
    return coordinateList

def getOnlyHorizontalOrLinear(segments):
    newVentLineSegments = []
    for segment in segments:
        if segment[0][0] == segment[1][0] or segment[0][1] == segment[1][1]:
            newVentLineSegments.append(segment)
    return newVentLineSegments

def getEmptyMap(ventLineSegments):
    maxX, maxY = 0, 0
    for segment in ventLineSegments:
        for coordPair in segment:
            if coordPair[0] > maxX:
                maxX = coordPair[0]
            if coordPair[1] > maxY:
                maxY = coordPair[1]
    maxX += 1
    maxY += 1
    emptyMap = []

    for i in range(maxY):
        emptyMap.append([0] * maxX)
    
    return emptyMap

def createMap(ventLineSegments, shouldCountDiagonal):
    map = getEmptyMap(ventLineSegments)
    for segment in ventLineSegments:
        if segment[0][0] == segment[1][0]:
            currentX = segment[0][0]
            currentY = min(segment[0][1], segment[1][1])
            endY = max(segment[0][1], segment[1][1])
            while currentY <= endY:
                map[currentY][currentX] += 1
                currentY += 1
        elif segment[0][1] == segment[1][1]:
            currentY = segment[0][1]
            currentX = min(segment[0][0], segment[1][0])
            endX = max(segment[0][0], segment[1][0])
            while currentX <= endX:
                map[currentY][currentX] += 1
                currentX += 1
        elif shouldCountDiagonal:
            #Do diagnoal
            xNegative = False
            yNegative = False
            
            if segment[0][0] > segment[1][0]:
                xNegative = True
            if segment[0][1] > segment[1][1]:
                yNegative = True
            currentX = segment[0][0]
            endX = segment[1][0]
            currentY = segment[0][1]
            endY = segment[1][1]
            while True:
                map[currentY][currentX] += 1
                if xNegative:
                    currentX -= 1
                    if currentX < endX:
                        break
                else:
                    currentX += 1
                    if currentX > endX:
                        break
                if yNegative:
                    currentY -= 1
                    if currentY < endY:
                        break
                else:
                    currentY += 1
                    if currentY > endY:
                        break

    return map
                

def findNumberOfOverlaps(inputLines, shouldCountDiagonal):
    # split input to [[x,y],[x,y]]
    ventLineSegments = getLineSegments(inputLines)
    # remove non horizontal or vertical lines
    if not shouldCountDiagonal:
        ventLineSegments = getOnlyHorizontalOrLinear(ventLineSegments);
    
    ventMap = createMap(ventLineSegments, shouldCountDiagonal)

    nrOfOverlaps = 0
    for row in ventMap:
        nrOfOverlaps += len([int(i) for i in row if i >= 2])
    
    return nrOfOverlaps
    
    

def main():
    inputLines = open("input.txt", "r").readlines()

    print(f'Overlap without diagonals: {findNumberOfOverlaps(inputLines,False)}')
    print(f'Overlap with diagonals: {findNumberOfOverlaps(inputLines, True)}')


if __name__ == "__main__":
    main()