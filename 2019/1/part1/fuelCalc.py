import math as math

inputFile = open("input.txt", "r")
totalFuelNeeded = 0
for moduleMass in inputFile:
    totalFuelNeeded += math.floor(int(moduleMass)/3)-2
print(totalFuelNeeded)
