def split_list(list):
    half = len(list)//2
    return (list[:half],list[half:])

def find_missing_seat(listToSearch):
    sortedList = sorted(listToSearch)
    return [seatId for seatId in range(sortedList[0], sortedList[-1]+1) if seatId not in sortedList]


codes = open('input.txt','r').readlines()
minRow = 0
maxRow = 127
minCol = 0
maxCol = 7

defaultRowRange = list(range(minRow,maxRow+1))
defaultColRange = list(range(minCol,maxCol+1))
allSeatIds = list()

for code in codes:
    currentRowRange = defaultRowRange
    currentColRange = defaultColRange
    finalRow = 0
    finalCol = 0


    lettersInCode = list(code)
    for letter in lettersInCode:
        splitRowList = split_list(currentRowRange)
        splitColList = split_list(currentColRange)

        if letter == 'F':
            currentRowRange = splitRowList[0]
        if letter == 'B':
            currentRowRange = splitRowList[1]
        if letter == 'L':
            currentColRange = splitColList[0]
        if letter == 'R':
            currentColRange = splitColList[1]

        if len(currentRowRange) == 1:
            finalRow = currentRowRange[0]
        
        if len(currentColRange) == 1:
            finalCol = currentColRange[0]
    allSeatIds.append((finalRow * 8) + finalCol)

print("Your seatID: " + str(find_missing_seat(allSeatIds)))
print("Highest seat ID: " + str(max(allSeatIds)))