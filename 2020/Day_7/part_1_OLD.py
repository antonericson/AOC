import re

class Bag:
    def __init__(self, name, containsBags):
        self.name = name
        self.containsBags = containsBags
        self.canContainGold = False
        
    def addContainBag(self, bagToAdd):
        self.containsBags.append(bagToAdd)
        if bagToAdd == 'shiny gold':
            self.canContainGold = True

def couldContainGold(bag):
    for innerBagName in bag.containsBags:
        for bagInstance in allBags:
            if bagInstance.name == innerBagName:
                innerBag = bagInstance
                print(innerBag)
                break
            innerBag = Bag("DUMMY", ('no other'))

        if 'no other' not in innerBag.containsBags:
            if 'shiny gold' in innerBag.containsBags or innerBag.canContainGold:
                return True
            else:
                return couldContainGold(innerBag)
        else:
            return False
        

allInputLines = open('input.txt','r').readlines()
allBags = list()
nrOfBagsCouldContainGold = 0
# light red bags contain 1 bright white bag, 2 muted yellow bags.
for bagDescription in allInputLines:
    descriptionList = bagDescription.split(' bags contain ')
    currentBag = Bag(descriptionList[0], list())
    cleanedDescription = descriptionList[1].replace('bags.', '').replace('bag.', '')
    cleanedDescription = re.sub(r'[0-9]', '', cleanedDescription).strip()
    containsBagsList = cleanedDescription.split(',')
    for bag in containsBagsList:
        currentBag.addContainBag(bag.strip())
    allBags.append(currentBag)

for bag in allBags:
    if couldContainGold(bag):
        nrOfBagsCouldContainGold += 1

print('{} bags could contain golden bag'.format(nrOfBagsCouldContainGold))