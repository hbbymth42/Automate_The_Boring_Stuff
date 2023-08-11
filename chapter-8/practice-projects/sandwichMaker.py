#! python3
import pyinputplus as pyip
breadPrices = {'white': 0.10,
              'wheat': 0.15,
              'sourdough': 0.20}
proteinPrices = {'tofu': 0.50,
                 'chicken': 0.60,
                 'ham': 0.70,
                 'turkey': 0.80}
cheesePrices = {'cheddar': 0.10,
                'mozzarella': 0.20,
                'swiss': 0.30}

numSandwiches = 0
otherOptionsPrice = 0
cheeseResponse = ''

numSandwiches = pyip.inputInt(prompt="How many Sandwiches do you want?\n", min=1)

breadResponse = pyip.inputMenu(list(breadPrices.keys()),prompt="Would you like white, wheat or sourdough bread? (Type one of the below options)\n")

proteinResponse = pyip.inputMenu(list(proteinPrices.keys()), prompt="Would you like tofu, chicken, ham or turkey? (Type one of the below options)\n")

otherOptReponse = pyip.inputYesNo(prompt="Would you like mayo, mustard, lettuce, or tomato? (Yes or No)\n")

if otherOptReponse == 'yes':
    otherOptionsPrice = 0.01
else:
    otherOptionsPrice = 0

cheeseSelect = pyip.inputYesNo(prompt="Would you like cheese? (Yes or No)\n")

if cheeseSelect == 'yes':
    cheeseResponse = pyip.inputMenu(list(cheesePrices.keys()), prompt="Would you like cheddar, mozzarella or swiss cheese? (Type one of the below options)\n")
    print('Total Cost of Sandwich(es): %.2f' % (numSandwiches * (breadPrices[breadResponse] + proteinPrices[proteinResponse] + cheesePrices[cheeseResponse] + otherOptionsPrice)))
else:
    print('Total Cost of Sandwich(es): %.2f' % (numSandwiches * (breadPrices[breadResponse] + proteinPrices[proteinResponse] + otherOptionsPrice)))