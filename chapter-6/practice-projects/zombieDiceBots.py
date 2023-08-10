import zombiedice
import random

class RandomZombie:
    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None and random.randint(0, 1) == 0:
            diceRollResults = zombiedice.roll()

class TwoBrainsZombie:
    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class TwoShotgunsZombie:
    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class InitialDecisionTwoShotgunZombie:
    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        numRolls = random.randint(1,4)
        numRoll = 0
        shotguns = 0
        while diceRollResults is not None and numRoll < numRolls:
            shotguns += diceRollResults['shotgun']
            numRoll += 1
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class MoreShotgunsThanBrainsZombie:
    def __init__(self, name):
        self.name = name
    
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotguns = 0
        brains = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotguns < brains:
                diceRollResults = zombiedice.roll()
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name = 'Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name = 'Stop at 1 Shotgun', minShotguns=1),
    RandomZombie(name = 'Random Zombie'),
    TwoBrainsZombie(name='Two Brains Zombie'),
    TwoShotgunsZombie(name = 'Two Shotguns Zombie'),
    InitialDecisionTwoShotgunZombie(name = 'Initial Decision Two Shotgun Zombie'),
    MoreShotgunsThanBrainsZombie(name = 'More Shotguns Than Brains Zombie')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)