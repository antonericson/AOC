from collections import Counter

allLines = open('input.txt','r').readlines()
currentGroupAnswers = list()
allGroupAnswers = list()
numberOfPeopleInGroup = 0

for line in allLines:
    if line != '\n':
        numberOfPeopleInGroup += 1
        for letter in line.strip():
            currentGroupAnswers.append(letter.strip())
    else:
        answerDict = Counter(currentGroupAnswers)
        for letter, occurances in answerDict.items():
            if occurances == numberOfPeopleInGroup:
                allGroupAnswers.append(letter)

        currentGroupAnswers = list()
        numberOfPeopleInGroup = 0
    
answerDict = Counter(currentGroupAnswers)
for letter, occurances in answerDict.items():
    if occurances == numberOfPeopleInGroup:
        allGroupAnswers.append(letter)
                
print('Sum of all group answers: ' + str(len(allGroupAnswers)))
