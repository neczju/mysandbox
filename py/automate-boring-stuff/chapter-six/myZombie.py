import zombiedice, random

class MyZombie:
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

class RandomBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:
            if random.randint(0, 1):
                diceRollResults = zombiedice.roll()
            else:
                break

class TwoBrainStopBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains == 2:
                break
            else:
                diceRollResults = zombiedice.roll()

class TwoShotgunStop:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun == 2:
                break
            else:
                diceRollResults = zombiedice.roll()

class TwoShotgunStopAlt:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        botDecision = random.randint(0, 3)
        diceRollResults = zombiedice.roll()
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if botDecision == 0 and shotguns == 2:
                break
            else:
                diceRollResults = zombiedice.roll()

class BotStopsWhenGunsGreaterThanBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotguns > brains:
                break
            else:
                diceRollResults = zombiedice.roll()




 

zombies = (zombiedice.examples.RandomCoinFlipZombie(name='RandomCoinFlip'),
          zombiedice.examples.RollsUntilInTheLeadZombie(name='UntilInTheLead'),
          zombiedice.examples.MinNumShotgunsThenStopsZombie(name='2ShotStop', minShotguns=2),
          zombiedice.examples.MinNumShotgunsThenStopsZombie(name='1ShotStop', minShotguns=1),
          MyZombie(name='MyZombie'),
          RandomBot(name='RandomBot'),
          TwoBrainStopBot(name='TwoBrainStopBot'),
          TwoShotgunStop(name='TwoShotgunStop'),
          TwoShotgunStopAlt(name='TwoShotgunStopAlt'),
          BotStopsWhenGunsGreaterThanBrains(name='BotStopWhenGunsGreaterThanBrains'))

zombiedice.runTournament(zombies=zombies, numGames=1000)
