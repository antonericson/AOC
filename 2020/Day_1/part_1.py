
expense_report = open("input.txt", "r").readlines()
wantedSum = 2020

for number in expense_report:
    tmpSum = wantedSum - int(number)

    for secondNumber in expense_report:
        if tmpSum == int(secondNumber):
            print(int(number) * int(secondNumber))
            break
    else:
        continue
    break
