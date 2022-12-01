passportRows = open('input.txt','r').readlines()
wantedKeySet = set(("byr","iyr","eyr","hgt","hcl","ecl","pid"))
validPassports = 0
currentKeySet = set()

for passportRow in passportRows:
    if passportRow != "\n":
        passportFields = passportRow.split(" ")
        for field in passportFields:
            keyField = field.strip().split(":")[0]
            if keyField in wantedKeySet:
                currentKeySet.add(keyField)

    else:
        if currentKeySet == wantedKeySet:
            validPassports += 1

        currentKeySet.clear()

if currentKeySet == wantedKeySet:
    validPassports += 1

print("Valid passports: " + str(validPassports))
