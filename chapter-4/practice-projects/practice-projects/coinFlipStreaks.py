import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    experimentList = []
    coinFlip = 0
    for coinFlipNum in range(100): # Generates List of Heads/Tails Coin Flips
        coinFlip = random.randint(0,1)
        if coinFlip == 0:
            experimentList.append("H")
        else:
            experimentList.append("T")
    for i in range(len(experimentList) - 6): # Checks for Streaks, iterates through list by each value
        if experimentList[i] == experimentList[i+1] == experimentList[i+2] == experimentList[i+3] == experimentList[i+4] == experimentList[i+5]:
            numberOfStreaks += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))