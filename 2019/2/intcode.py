def getInput():
    input = open("input.txt", "r")
    strInput = input.read().split(",")
    return [int(i) for i in strInput]

def run(index):
    currentOp = integers[index]
    if currentOp == 99:
        return integers

    valueOneIndex = integers[index+1]
    valueTwoIndex = integers[index+2]
    outputIndex = integers[index+3]
    
    if currentOp == 1:
        integers[outputIndex] = integers[valueOneIndex] + integers[valueTwoIndex]
    elif currentOp == 2:
        integers[outputIndex] = integers[valueOneIndex] * integers[valueTwoIndex]
        
    run(index+4)

nounIndex = 1
verbIndex = 2
noun = 0
verb = 0
correctAnswer = 19690720

while noun <= 99:
    verb = 0
    while verb <= 99:
        integers = getInput()
        integers[nounIndex] = noun
        integers[verbIndex] = verb
        run(0)
        if(integers[0] == correctAnswer):
            break
        verb += 1
    if(integers[0] == correctAnswer):
        break
    noun += 1

print('Verb: ' + str(verb))
print('Noun: ' + str(noun))
print('Answer:')
print(100*noun+verb)

