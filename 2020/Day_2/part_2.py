passwordList = open("input.txt", "r").readlines()
numberOfValidPasswords = 0

for passwordRow in passwordList:
    passwordRowArray = passwordRow.split(" ")
    indexOne = int(passwordRowArray[0].split("-")[0])-1
    indexTwo = int(passwordRowArray[0].split("-")[1])-1

    wantedChar = passwordRowArray[1].replace(":","")
    passwordLetters = list(passwordRowArray[2])

    lettersInRange = 0
    
    if passwordLetters[indexOne] == wantedChar:
        lettersInRange = lettersInRange + 1
    if passwordLetters[indexTwo] == wantedChar:
        lettersInRange = lettersInRange + 1 

    if lettersInRange == 1:
        numberOfValidPasswords = numberOfValidPasswords + 1
            

print(str(numberOfValidPasswords) + " valid passwords found.")
