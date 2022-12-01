pwRange = [235741,706948]

numberOfPws = 0

def isValid(password):
    numbers = list(password)
    hasAdjecent = False
    isAcending = True
    lastNumber = ''

    first = True
    for number in numbers:
        if not first:
            if number < lastNumber:
                isAcending = False
                break
            if number == lastNumber or hasAdjecent:
                hasAdjecent = True
        first = False
        lastNumber = number
        
    if hasAdjecent and isAcending:
        print("match")
        return 1
    else:
        return 0

current = pwRange[0]
while current <= pwRange[1]:
    numberOfPws += isValid(str(current))
    current += 1

print(numberOfPws)
