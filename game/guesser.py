from secret_word import random_word

word = random_word.word
print(word)

class guesser:
    def __init__(self, playerGuess):
        self.guess = playerGuess

    def checkLetter(self):
        if not(playerGuess.isdigit()):
            for character in word:
                if(character == playerGuess):
                    print("Correct!")
                else:
                    print("Try Again!")
        else:
            print("Please enter a letter, not a number")


playerGuess = input("Enter a letter guess: ")
guesser.checkLetter(playerGuess)