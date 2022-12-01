directionLines = open("input.txt", "r").readlines()

def calculatePosNoAim():
    directions = dict(forward=0, up=0, down=0)
    for line in directionLines:
        currentDirectionData = line.replace("\n","").split(" ")
        currentDirection = currentDirectionData[0]
        currentMovement = int(currentDirectionData[1])
        
        directions[currentDirection] += currentMovement 

        
    xPos = directions["forward"]
    yPos = directions["down"] - directions["up"]
    
    return xPos * yPos

def calculatePosWithAim():
    xPos = 0
    yPos = 0
    aim = 0
    for line in directionLines:
        currentDirectionData = line.replace("\n","").split(" ")
        currentDirection = currentDirectionData[0]
        currentMovement = int(currentDirectionData[1])
        if currentDirection == "forward":
           xPos += currentMovement
           yPos += currentMovement * aim 
        if currentDirection == "up":
            aim -= currentMovement
        if currentDirection == "down":
            aim += currentMovement 
        
    
    return xPos * yPos

def main():
    print(f'Part one: {calculatePosNoAim()}')
    print(f'Part two: {calculatePosWithAim()}')


if __name__ == "__main__":
    main()