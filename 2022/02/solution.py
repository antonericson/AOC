# First column, opponent
# A = ROCK 0
# B = PAPER 1
# C = SCISSORS 2

# Second column, me
# X = ROCK 0
# Y = PAPER 1
# Z = SCISSORS 2

# Score based on MY PLAY + outcome:
# (ROCK)X = 1
# (PAPER)Y = 2
# (SCISSORS)Z = 3

# LOST = 0
# DRAW = 3
# WIN = 6

opponentPlay = ['A','B','C']
myPlay = ['X','Y','Z']

def main():
    inputLines =  open("input.txt", "r").readlines()

    totalP1Score = 0
    for turn in inputLines:
        totalP1Score = totalP1Score + playTurn(turn)

    print(f'Part one: {totalP1Score}')
    
# Second column, outcome
# X = LOSS
# Y = DRAW
# Z = WIN
    
    totalP2Score = 0
    for turn in inputLines:
        turnList = turn.strip().split(' ')
        opponentTurn = turnList[0]
        outcome = turnList[1]
                
        totalP2Score = totalP2Score + playTurn(f'{opponentTurn} {myPlay[(opponentPlay.index(opponentTurn) + (myPlay.index(outcome) - 1)) % 3]}')
            
    print(f'Part two: {totalP2Score}')

def playTurn(turn):
    turnList = turn.strip().split(' ')
    opponentTurn = turnList[0]
    myTurn = turnList[1]
    score = myPlay.index(myTurn) + 1
    
    if myPlay.index(myTurn) == (opponentPlay.index(opponentTurn) + 1) % 3:
        # WIN
        score = score + 6 
    elif opponentPlay.index(opponentTurn) == myPlay.index(myTurn):
        # DRAW
        score = score + 3
        
    return score

if __name__ == "__main__":
    main()
