mapRows = open("input.txt", "r").readlines()
treesHit = 0
stepSizeRight = 3
currentRowIndex = 0
firstRow = True

for row in mapRows:
    rowArray = list(row.strip())
    
    currentPlace = rowArray[currentRowIndex]
    if currentPlace == '#':
        treesHit += 1
    
    if (currentRowIndex + stepSizeRight) > len(rowArray)-1:
        currentRowIndex = (currentRowIndex + stepSizeRight) - len(rowArray)
    else:
        currentRowIndex += stepSizeRight
print("Trees hit: " + str(treesHit))
