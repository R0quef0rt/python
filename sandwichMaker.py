import pyinputplus as pyip 

breadType = {'wheat': 1.00, 'white': 1.00, 'sourdough': 1.75}
proteinType = {'chicken': 2.50, 'turkey': 2.00, 'ham': 2.00, 'tofu': 3.50}
cheeseType = {'cheddar': 1.00, 'swiss': 1.00, 'mozzarella': 1.00}

def sandwichMaker():
    numSandwiches = pyip.inputNum(prompt='How many sandwiches would you like?')
    totalCost = 0.00

    while numSandwiches > 0:
        bread = pyip.inputMenu(list(breadType.keys()))
        protein = pyip.inputMenu(list(proteinType.keys()))
        askCheese = pyip.inputYesNo(prompt='Add cheese?')

        if askCheese == 'yes':
            cheese = pyip.inputMenu(list(cheeseType.keys()))
            totalCost = totalCost + cheeseType[cheese]

        pyip.inputYesNo(prompt='Add mayo?')
        pyip.inputYesNo(prompt='Add mustard?')
        pyip.inputYesNo(prompt='Add lettuce?')
        pyip.inputYesNo(prompt='Add tomato?')

        totalCost = totalCost + breadType[bread] + proteinType[protein]
        numSandwiches -= 1

    print(totalCost)
sandwichMaker()