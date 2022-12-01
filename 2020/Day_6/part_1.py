allLines = open('input.txt','r').readlines()
currentGroupAnswers = set()
allGroupAnswers = list()

for line in allLines:
    if line != '\n':
        for letter in line.strip():
            currentGroupAnswers.add(letter.strip())
    else:
        allGroupAnswers.append(len(currentGroupAnswers))
        currentGroupAnswers = set()
    
allGroupAnswers.append(len(currentGroupAnswers))
print('Sum of all group answers: ' + str(sum(allGroupAnswers)))
