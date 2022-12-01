def getNrOfOnesInEachPos(diagnosticsLines):
    nrOfOnesInPos = [0] * (len(diagnosticsLines[0])-1)
    for binaryNumber in diagnosticsLines:
        bits = list(binaryNumber.strip())
        for index, bit in enumerate(bits):
            nrOfOnesInPos[index] += int(bit)

    return nrOfOnesInPos

def getO2GeneratorRating(checkingIndex, listToCheck):
    if len(listToCheck) == 1:
        return listToCheck[0]
    
    nrOfOnesInEachPos = getNrOfOnesInEachPos(listToCheck)
    newList = []
    if nrOfOnesInEachPos[checkingIndex] >= len(listToCheck)/2:
        #Keep only lines with 1 in checkingIndex
        for binaryNumber in listToCheck:
            if list(binaryNumber)[checkingIndex] == "1":
                newList.append(binaryNumber)
    else:
        for binaryNumber in listToCheck:
            if list(binaryNumber)[checkingIndex] == "0":
                newList.append(binaryNumber)
    
    return getO2GeneratorRating(checkingIndex + 1, newList)

def getCO2ScrubberRating(checkingIndex, listToCheck):
    if len(listToCheck) == 1:
        return listToCheck[0]
    
    nrOfOnesInEachPos = getNrOfOnesInEachPos(listToCheck)
    newList = []
    if nrOfOnesInEachPos[checkingIndex] >= len(listToCheck)/2:
        #Keep only lines with 1 in checkingIndex
        for binaryNumber in listToCheck:
            if list(binaryNumber)[checkingIndex] == "0":
                newList.append(binaryNumber)
    else:
        for binaryNumber in listToCheck:
            if list(binaryNumber)[checkingIndex] == "1":
                newList.append(binaryNumber)
    
    return getCO2ScrubberRating(checkingIndex + 1, newList)
    

def getFuelConsumption(diagnosticsLines):
    # gamma rate => most common bit in each pos
    # epsilon rate => least common bit in each pos
    # fuel consumption => gamma rate * epsilon rate
    epsilonRateBinary = ""
    gammaRateBinary = ""
    
    nrOfOnesInPos = getNrOfOnesInEachPos(diagnosticsLines)   
    for pos in nrOfOnesInPos:
        if pos > len(diagnosticsLines)/2:
            epsilonRateBinary += "0"
            gammaRateBinary += "1"
        else:
           epsilonRateBinary += "1"
           gammaRateBinary += "0"
    
    return int(epsilonRateBinary, 2) * int(gammaRateBinary, 2)
    
def getLifeSupportRating(diagnosticsLines):
    generatorRating = getO2GeneratorRating(0, diagnosticsLines)
    co2ScrubberRating = getCO2ScrubberRating(0, diagnosticsLines)
    
    return int(generatorRating, 2) * int(co2ScrubberRating, 2)

def main():
    inputLines = open("input.txt", "r").readlines()
    print(f'Fuel consumption: {getFuelConsumption(inputLines)}')
    print(f'Life support rating: {getLifeSupportRating(inputLines)}')


if __name__ == "__main__":
    main()