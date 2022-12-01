import re

class Bag:
    def __init__(self, name, containsBags):
        self.name = name
        self.containsBags = containsBags

def createBagInstance(bagName):
    newBagInstance = Bag(bagName, list())
    for innerBagName in bagDefinitions[bagName]:
        newBagInstance.containsBags.append(createBagInstance(innerBagName))
        if innerBagName == 'shiny gold':
            bagsContainingGold.add(bagName)
    return newBagInstance

def couldContainGold(bag):
    #print("CHECKING: " + str(bag.containsBags))
    foundSet = list()
    for innerBag in bag.containsBags:
        if innerBag.name in bagsContainingGold and bag.name != 'shiny gold':
            foundSet.append(bag.name)
            foundSet.extend(couldContainGold(innerBag))
    return foundSet
        

allInputLines = open('input.txt', 'r').readlines()
allBags = list()
bagDefinitions = dict()
nrOfBagsCouldContainGold = 0
bagsContainingGold = set()

for bagDescription in allInputLines:
    descriptionList = bagDescription.split(' bags contain ')
    bagDefinitions[descriptionList[0]] = list()
    cleanedDescription = descriptionList[1].replace('bags.', '').replace('bag.', '').replace('bags','').replace('bag', '')
    cleanedDescription = re.sub(r'[0-9]', '', cleanedDescription).strip()
    innerBagNamesList = cleanedDescription.split(',')
    for innerBagName in innerBagNamesList:
        if innerBagName != 'no other':
            currentInnerBags = bagDefinitions.get(descriptionList[0])
            currentInnerBags.append(innerBagName.strip())
            bagDefinitions[descriptionList[0]] = currentInnerBags

for bagName in bagDefinitions:
    allBags.append(createBagInstance(bagName))
allFound = list()
for bag in allBags:
    allFound.extend(couldContainGold(bag))
print(set(allFound))

print(bagsContainingGold)
print(len(bagsContainingGold))
print('{} bags could contain golden bag'.format(len(set(allFound))))