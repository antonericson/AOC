passwordList = open("input.txt", "r").readlines()
numberOfValidPasswords = 0

for passwordRow in passwordList:
    passwordRowArray = passwordRow.split(" ")
    minNumberOfChars = passwordRowArray[0].split("-")[0]
    maxNumberOfChars = passwordRowArray[0].split("-")[1]

    wantedChar = passwordRowArray[1].replace(":","")
    numberOfWantedChars = 0

    password = passwordRowArray[2]

    for letter in password:
        if letter == wantedChar:
            numberOfWantedChars = numberOfWantedChars + 1
    
    if numberOfWantedChars >= int(minNumberOfChars) and numberOfWantedChars <= int(maxNumberOfChars):
        numberOfValidPasswords = numberOfValidPasswords + 1

print(str(numberOfValidPasswords) + " valid passwords found.")
