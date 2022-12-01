import math as math
inputFile = open("input.txt", "r")

def calcFuelReq(mass, tot):
    fuelReq = math.floor(int(mass)/3)-2
    return calcFuelReq(fuelReq, tot+fuelReq) if fuelReq > 0 else tot

totalFuel = 0

for moduleMass in inputFile:
    totalFuel += calcFuelReq(moduleMass, 0)
print(totalFuel)

