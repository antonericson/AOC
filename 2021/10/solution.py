def getCorruptedLineScore(inputLines):
    openingCharacters = ["(", "[", "{", "<"]
    closingCharacters = [")", "]", "}", ">"]
    illegalCharactersFound = []
    for line in inputLines:
        lineList = list(line.strip())
        currentlyOpenChunks = []
        for char in lineList:
            if char in openingCharacters:
                currentlyOpenChunks.append(char)
                continue
            if char in closingCharacters:
                if openingCharacters[closingCharacters.index(char)] == currentlyOpenChunks[-1]:
                    del currentlyOpenChunks[-1]
                else:
                    illegalCharactersFound.append(char)
                    break
                
    pointMap = {")":3, "]":57, "}":1197, ">":25137}
    score = 0
    
    for char in illegalCharactersFound:
        score += pointMap.get(char)
    
    return score
        
def getCompleteLinePoints(inputLines):  
    openingCharacters = ["(", "[", "{", "<"]
    closingCharacters = [")", "]", "}", ">"]
    legalLinesOpenChunks = []
    for line in inputLines:
        lineList = list(line.strip())
        currentlyOpenChunks = []
        lineLegal = True
        for char in lineList:
            if char in openingCharacters:
                currentlyOpenChunks.append(char)
                continue
            if char in closingCharacters:
                if openingCharacters[closingCharacters.index(char)] == currentlyOpenChunks[-1]:
                    del currentlyOpenChunks[-1]
                else:
                    lineLegal = False
                    break
        if lineLegal:
            legalLinesOpenChunks.append(currentlyOpenChunks)

    charactersToComplete = []
    for openChunks in legalLinesOpenChunks:
        tmp = []
        openChunks.reverse()
        for char in openChunks:
            tmp.append(closingCharacters[openingCharacters.index(char)])
        charactersToComplete.append(tmp)
    
    pointMap = {")":1, "]":2, "}":3, ">":4}
    scoreList = []
    for charactersToCompleteLine in charactersToComplete:
        score = 0
        for char in charactersToCompleteLine:
            score = score * 5
            score += pointMap.get(char)
        scoreList.append(score)
    scoreList.sort()
    
    return scoreList[int((len(scoreList)-1)/2)]
        

def main():
    inputLines =  open("input.txt", "r").readlines()

    print(f'Part one: {getCorruptedLineScore(inputLines)}')
    print(f'Part two: {getCompleteLinePoints(inputLines)}')

if __name__ == "__main__":
    main()
