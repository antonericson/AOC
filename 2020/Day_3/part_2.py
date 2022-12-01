import math

def calculate_hits(map, incrementRight, incrementDown):
    treesHit = 0
    currentRowIndex = 0
    for i in range(0, len(map), incrementDown):
        rowArray = list(list(map)[i].strip())
        currentPlace = rowArray[currentRowIndex]
        if currentPlace == '#':
            treesHit += 1
        
        if (currentRowIndex + incrementRight) > len(rowArray)-1:
            currentRowIndex = (currentRowIndex + incrementRight) - len(rowArray)
        else:
            currentRowIndex += incrementRight
    return treesHit


mapRows = open("input.txt", "r").readlines()

hitArray = []
hitArray.append(calculate_hits(mapRows, 1, 1))
hitArray.append(calculate_hits(mapRows, 3, 1))
hitArray.append(calculate_hits(mapRows, 5, 1))
hitArray.append(calculate_hits(mapRows, 7, 1))
hitArray.append(calculate_hits(mapRows, 1, 2))

print("All hits: " + str(hitArray))
print("Hits multiplied: " + str(math.prod(hitArray)))
