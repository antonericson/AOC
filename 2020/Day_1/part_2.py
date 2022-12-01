
expense_report = open("input.txt", "r").readlines()
wantedSum = 2020

for number in expense_report:
    for secondNumber in expense_report:
        tmpSum = wantedSum - int(number) - int(secondNumber)

        for thirdNumber in expense_report:
            if tmpSum == int(thirdNumber):
                print(int(number) * int(secondNumber) * int(thirdNumber))
                break
        else:
            continue
        break
    else:
        continue
    break
