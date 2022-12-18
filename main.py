from gameManager import GameManager

# -------------------------------- #
# -------- YOUR CODE HERE -------- #
# -------------------------------- #
def PlayCoinFlip(self):
    coinFlipResult = self.coinFlipResult
    playerGuess = self.userInput

    print(f'You Picked: {playerGuess}')
    print(f'Flip Result: {coinFlipResult}')
    
    # CODE GOES HERE


# -------------------------------- #
# -------- END YOUR CODE! -------- #
# -------------------------------- #
GameManager.PlayGame = PlayCoinFlip

game = GameManager()
game.Play()