
def getDraws(inputLines):
    return [int(i) for i in inputLines[0].split(",")]

def mapBingoBoards(inputLines):
    bingoBoards = [[]]
    boardIndex = 0
    isFirstLinebreak = False
    for line in inputLines:
        if line.__contains__(","):
            isFirstLinebreak = True
            continue
        if isFirstLinebreak:
            isFirstLinebreak = False
            continue
        if line == "\n":
            boardIndex += 1
            if boardIndex > 0:
                bingoBoards.append([])
            continue
        currentRow = {int(i): False for i in line.strip().replace("  ", " ").split(" ")}
        bingoBoards[boardIndex].append(currentRow)
        
    return bingoBoards

def drawNumbers(draws, bingoBoards, shouldWin):
    numbersDrawn = 0
    winners = []
    lastWinner = []
    for draw in draws:
        numbersDrawn += 1
        for boardIndex, board in enumerate(bingoBoards):
            if boardIndex not in winners:
                markBoard(draw, board)
                if numbersDrawn >= 5:
                    #check for winners
                    isWinner = checkBoard(board)
                    if isWinner:
                        if shouldWin:
                            return [boardIndex, draw]
                        else:
                            winners.append(boardIndex)
                            lastWinner =  [boardIndex, draw]
    return lastWinner
                    

def markBoard(draw, board):
    for row in board:
        if row.get(draw) != None:
            row[draw] = True

def checkBoard(board):
    columns = [0] * 5
    for row in board:
        if False not in row.values():
            return True
        for colIndex, dictEntry in enumerate(row):
            if row[dictEntry]:
                columns[colIndex] += 1
    if 5 in columns:
        return True
    return False
        
def calculateScore(winningBoard, winningDraw):
    score = 0
    for row in winningBoard:
        for number in row:
            if not row[number]:
                score += number
                
    return score * winningDraw

def simulateBingo(inputLines, shouldWin):
     # Get bingo draws
    draws = getDraws(inputLines)
    # Map boards
    bingoBoards = mapBingoBoards(inputLines)
    # Draw numbers
    winningInformation = drawNumbers(draws, bingoBoards, shouldWin)
    winningBoardIndex = winningInformation[0]
    winningDraw = winningInformation[1]
    # Calculate score
    return calculateScore(bingoBoards[winningBoardIndex], winningDraw)

def main():
    inputLines = open("input.txt", "r").readlines()

    print(f'Part one: {simulateBingo(inputLines, True)}')
    print(f'Part two: {simulateBingo(inputLines, False)}')


if __name__ == "__main__":
    main()