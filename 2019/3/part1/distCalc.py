wireOneInput = open("wireOne.txt", "r").read().split(",")
wireTwoInput = open("wireTwo.txt", "r").read().split(",")

wireOneCoords = [[0,0]]
wireTwoCoords = [[0,0]]

def createInstructions(path):
    instructions = []
    for instruction in path:
        direction = instruction.rstrip('0123456789')
        number = instruction[len(direction):]
        instructions.append([direction, number])
    return instructions

def move(coordList, direction, amount):
    while amount > 0:
        lastCoord = coordList[-1]
        lastX = lastCoord[0]
        lastY = lastCoord[1]
        if direction == "U":
            coordList.append([lastX, lastY + 1])
        elif direction == "D":
            coordList.append([lastX, lastY - 1])
        elif direction == "L":
            coordList.append([lastX - 1, lastY])
        elif direction == "R":
            coordList.append([lastX + 1, lastY])
        amount -= 1
    return coordList

for instruction in createInstructions(wireOneInput):
    move(wireOneCoords, instruction[0], int(instruction[1]))

for instruction in createInstructions(wireTwoInput):
    move(wireTwoCoords, instruction[0], int(instruction[1]))

nearestDist = 0

for coordinate in wireOneCoords:
     if coordinate in wireTwoCoords:
        dist = abs(coordinate[0]) + abs(coordinate[1])
        if nearestDist == 0 or dist < nearestDist and dist != 0:
            nearestDist = dist

print(nearestDist)
