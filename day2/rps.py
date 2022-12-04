# %%
from typing import List
from collections import Counter

# %%
class RockPaperScissorsCalculator():
    def __init__(self) -> None:
        #maybe easier to just build from first principles
        self.playerChoiceScore = {
            'X' : 1,
            'Y' : 2,
            'Z' : 3
        }

        self.winConditions = {
            #wins
            'C X' : 6,
            'A Y' : 6,
            'B Z' : 6,
            #draws
            'A X' : 3,
            'B Y' : 3,
            'C Z' : 3,
            #losses
            'B X' : 0,
            'C Y' : 0,
            'A Z' : 0,
        }

    def CalculateScore(self, gamesString: str) -> int:
        totalScore = 0
        #games are encoded on lines so we can cycle thru them
        for game in gamesString.strip().split('\n'):
            playerChoice = game[-1]
            totalScore += self.playerChoiceScore[playerChoice] + self.winConditions[game]
        return totalScore

exampleInput = '''A Y
B X
C Z'''

RockPaperScissorsCalculator().CalculateScore(exampleInput)

#%%
with open('input.txt', 'r') as f:
    realInput = f.read()

RockPaperScissorsCalculator().CalculateScore(realInput)


# %%
Counter(realInput.strip().split('\n')).keys()
# %%



outcomes = {
    #game: win? + choice
    'A Z': 0 + 3,
    'B X': 0 + 1,
    'A Y': 6 + 2,
    'C Y': 6 + 2,
    'C X': 6 + 1,
    'B Z': 6 + 3,
    'C Z': 3 + 3,
    'B Y': 2 + 3,
    'A X': 1 + 3
}

# %%
'''
opponent:
A = rock
B = paper
C = scissors

player:
X = rock
Y = paper
Z = scissors
'''
#maybe easier to just build from first principles
playerChoiceScore = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

winConditions = {
    #wins
    'C X' : 6,
    'A Y' : 6,
    'B Z' : 6,
    #draws
    'A X' : 3,
    'B Y' : 3,
    'C Z' : 3,
    #losses
    'B X' : 0,
    'C Y' : 0,
    'A Z' : 0,
}

for possibleOutcome in ['A Z','B X','A Y','C Y','C X','B Z','C Z','B Y','A X']:
    playerChoice = possibleOutcome[-1]
    print(possibleOutcome, playerChoiceScore[playerChoice] + winConditions[possibleOutcome])

# %%

class RockPaperScissorCalculatorPart2():
    def __init__(self) -> None:
        #codes for what player is directed to do
        self.playerShouldDo = {
            'X' : 'Lose',
            'Y' : 'Draw',
            'Z' : 'Win'
        }

        #players choice, always comes second in game
        self.playerChoice = {
            'A' : 1,
            'B' : 2,
            'C' : 3
        }

        #need to do moves based on what we want to happen
        self.movesForWinCondition = {
            #opponent chooses A
            'A Win': 'B',
            'A Draw': 'A',
            'A Lose': 'C',
            #opponent chooses B
            'B Win': 'C',
            'B Draw': 'B',
            'B Lose': 'A',
            #opponent chooses C
            'C Win': 'A',
            'C Draw': 'C',
            'C Lose': 'B',
        }

        #win conditions (same as in original class)
        self.winConditions = {
            #wins
            'C A' : 6,
            'A B' : 6,
            'B C' : 6,
            #draws
            'A A' : 3,
            'B B' : 3,
            'C C' : 3,
            #losses
            'B A' : 0,
            'C B' : 0,
            'A C' : 0,
        }
    
    def CalculateScores(self, gameString) -> int:
        totalScore = 0
        for game in gameString.strip().split('\n'):
            #calculate the player's move
            playersMove = self.movesForWinCondition[game[0] + ' ' + self.playerShouldDo[game[-1]]]
            #construct game
            gameMoves = game[0] + ' ' + playersMove
            #calculate score
            totalScore += self.winConditions[gameMoves] + self.playerChoice[playersMove]
        return totalScore

exampleInput = '''A Y
B X
C Z'''

RockPaperScissorCalculatorPart2().CalculateScores(exampleInput)

# %%
with open('input.txt', 'r') as f:
    realInput = f.read()

RockPaperScissorCalculatorPart2().CalculateScores(realInput)


# %%
