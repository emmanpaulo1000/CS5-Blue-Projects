from random import random
class Event:

    def __init__(self, title):
        self.title = title

    def getTitle(self):
        return self.title

class Challenge(Event):

    def __init__(self, statsRequired, challengeProgress):

        Event.__init__(self, title)

        self.statsRequired     = statsRequired
        self.challengeProgress = challengeProgress

    def getStatsRequired(self):
        return self.statsRequired

    def getChallengeProgress(self):
        return self.challengeProgress

class Opportunity(Event):

    def __init__(self, successPercent, successEffects, failEffects):

        Event.__init__(self, title)

        self.successPercent = successPercent
        self.successEffects = successEffects
        self.failEffects    = failEffects
        

    def getSuccessPercent(self):
        return self.successPercent
    
    def getSuccessEffects(self):
        return self.successEffects

    def getFailEffects(self):
        return self.failEffects

class Fight(Event):
    
    def __init__(self, enemy, statsCompared, winReward, loseEffect):

        Event.__init__(self, title)

        self.enemy = enemy
        self.statsCompared = statsCompared
        self.winReward     = winReward
        self.loseEffect    = loseEffect

    def getStatsCompared(self):
        return self.statsCompared

    def getEnemy(self):
        return self.enemy

    def getWinReward(self):
        return self.winReward

    def getLoseEffect(self):
        return self.loseEffect
   
class Character:

    def __init__(self, name, gender):
        self.name   = name
        self.gender = gender

    def getName(name):
        self.name   = name

    def getGender(gender):
        self.gender = gender

class Fightable(Character):

    def __init__(self, health, strength, intelligence, charisma):

        Character.__init__(self, name, gender)

        # stats should always be in this order
        self.stats        = [health, strength,
                            intelligence,
                            charisma]
        
        self.winLine      = "You win!"
        self.loseLine     = "You lose."

    def getStats(self):
        return self.stats

    def getWinLine(self):
        return self.winLine

    def getLoseLine(self):
        return self.loseLine

class MainCharacter(Fightable):

    def __init__(self, challengeNumber):

        Fightable.__init__(self, health, strength, intelligence, charisma)
        
        self.challengeNumber = challengeNumber

    def getChallengeNumber(self):
        return self.challengeNumber

    def takeChallenge(self, challenge):
        for i in range(4):
            if self.stats[i] < challenge.getStatsRequired()[i]:
                self.challengeNumber -= challenge.getChallengeProgress()
                return
        self.challengeNumber += challenge.getChallengeProgress()

    def takeOpportunity(self, opportunity):
        if random() <= opportunity.getSuccessPercent():
            for i in range(4):
                self.stats[i] += opportunity.getSuccessEffects()[i]
        else:
            for i in range(4):
                self.stats[i] -= opportunity.getFailEffects()[i]

    def battle(self, fight):
        for i in range(4):
            if self.stats[i] > fight.getEnemy().getStats()[i]:
                self.stats[i] += fight.getWinReward()[i]
            else:
                self.stats[i] -= fight.getLoseEffect()[i]

"""
This is where we write our main code.
What happens now?
"""


print ("hello")
