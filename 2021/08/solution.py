def count1478(inputLines):
    correctLengths = [2, 4, 3, 7]
    nrOfCorrectDigits = 0
    for line in inputLines:
        digits = line.split(" | ")[1]
        for digit in digits.strip().split(" "):
            if len(digit) in correctLengths:
                nrOfCorrectDigits += 1

    return nrOfCorrectDigits

def decodeDigits(inputLines):
    finalSum = 0
    for line in inputLines:
        sumString = ""
        digitMap = [""] * 10
        lineData = line.split(" | ")
        referenceDigits = lineData[0].split(" ")
        digitsToDecode = lineData[1].strip().split(" ")
        for reference in referenceDigits:
            if len(reference) == 2:
                digitMap[1] = reference
            if len(reference) == 4:
                digitMap[4] = reference
            if len(reference) == 3:
                digitMap[7] = reference
            if len(reference) == 7:
                digitMap[8] = reference
        
        for reference in referenceDigits:
            if len(reference) == 5:
                if len(set(reference) & set(digitMap[8])) == len(digitMap[8])-2 and len(set(reference) & set(digitMap[7])) == len(digitMap[7]):
                    digitMap[3] = reference
                elif len(set(reference) & set(digitMap[8])) == len(digitMap[8])-2 and len(set(reference) & set(digitMap[4])) == 3:
                    digitMap[5] = reference
                else:
                    digitMap[2] = reference
            if len(reference) == 6:
                if len(set(reference) & set(digitMap[8])) == len(digitMap[8])-1 and len(set(reference) & set(digitMap[1])) == 2 and len(set(reference) & set(digitMap[4])) == len(digitMap[4])-1:
                    digitMap[0] = reference
                elif len(set(reference) & set(digitMap[8])) == len(digitMap[8])-1 and len(set(reference) & set(digitMap[4])) == len(digitMap[4]):
                    digitMap[9] = reference
                elif len(set(reference) & set(digitMap[8])) == len(digitMap[8])-1 and len(set(reference) & set(digitMap[4])) == len(digitMap[4])-1:
                    digitMap[6] = reference

        for digitCode in digitsToDecode:
            for index, digit in enumerate(digitMap):
                if ''.join(sorted(digitCode)) == ''.join(sorted(digit)):
                    sumString += str(index)

        finalSum += int(sumString)
    return finalSum
   

def main():
    inputLines =  open("input.txt", "r").readlines()

    print(f'Part one: {count1478(inputLines)}')
    print(f'Part two: {decodeDigits(inputLines)}')

if __name__ == "__main__":
    main()
