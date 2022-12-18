import random 
from gameInputException import GameInputException

class GameManager:
    def __init__(self):
        self.gameNumber = 0
        self.finished = False
        self.moves = ['heads', 'tails']
    
    def Play(self):
        while (not self.finished):
            try:
                self.StartNewGame()
                self.PlayGame()
                self.RestartGame()
            except GameInputException:
                continue

        print("quitting game")

    def StartNewGame(self):
        # Increment game number
        print(f'STARTING GAME {self.gameNumber}')
        self.gameNumber += 1

        # Get user input
        self.userInput = input("Enter Your Move: ").strip().lower()

        # Input parsing
        if (not self.userInput in self.moves):
            print("Invalid coin flip guess. Please try again")
            raise GameInputException(f'Input Error: {self.userInput} is not a valid coin flip result. Please try again')

        # Randomly generate a new coin flip result
        self.coinFlipResult = random.choice(self.moves)

    def RestartGame(self):
        continueGame = input("Do you want to continue? [yes / no]: ").strip().lower()

        if (continueGame == 'yes'): 
            pass
        elif (continueGame == 'no'):
            self.finished = True
        else:
            raise GameInputException()
            