
import re

def isValid(keyValuePair):

    validEyeColor = {'amb','blu','brn','gry','grn','hzl','oth'}

    key = keyValuePair[0]
    value = keyValuePair[1]
    if key == 'byr':
        return int(value) >= 1920 and int(value) <= 2002
    if key == 'iyr':
        return int(value) >= 2010 and int(value) <= 2020
    if key == 'eyr':
        return int(value) >= 2020 and int(value) <= 2030
    if key == 'hgt':
        regex = re.compile(r'([0-9]+[i][n])|([0-9]+[c][m])')
        if regex.match(value):
            unit = value.strip('0123456789')
            numbers = value.rstrip(unit)
            if unit == 'cm':
                return int(numbers) >= 150 and int(numbers) <= 193
            elif unit == 'in':
                return int(numbers) >= 59 and int(numbers) <= 76
    if key == 'hcl':
        regex = re.compile(r'[#][0-9a-f]{6}')
        return regex.match(value)
    if key == 'ecl':
        return value in validEyeColor
    if key == 'pid':
        regex = re.compile(r'[0-9]')
        return regex.match(value) and len(value) == 9


passportRows = open('input.txt','r').readlines()
wantedKeySet = set(("byr","iyr","eyr","hgt","hcl","ecl","pid"))
validPassports = 0
currentKeySet = set()

for passportRow in passportRows:
    if passportRow != "\n":
        passportFields = passportRow.split(" ")
        for field in passportFields:
            keyValuePair = field.strip().split(":")
            keyField = keyValuePair[0]
            if keyField in wantedKeySet and isValid(keyValuePair):
                currentKeySet.add(keyField)
    else:
        if currentKeySet == wantedKeySet:
            validPassports += 1

        currentKeySet.clear()

if currentKeySet == wantedKeySet:
    validPassports += 1

print("Valid passports: " + str(validPassports))
