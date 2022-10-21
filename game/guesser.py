from secret_word import random_word

word = random_word.word
print(word)

class guesser:
    def __init__(self, playerGuess):
        self.guess = playerGuess




    def check_letter(self):
        """Checks the letter against the word."""

        for i in range(0,len(self.word)):
            playerGuess = self.word[i]
            if self.guess == playerGuess:
                self.reveal[i] = self.guess
        if '_' not in self.reveal:
            return True
        else:
            return False


playerGuess = input("Enter a letter guess: ")
guesser.checkLetter(playerGuess)