from tkinter import Variable
from secret_word import SecretWord
from jumper import Display

random_word = SecretWord()
word = random_word.word
print(word)

p = Display()
print(p)

class guesser:
    def __init__(self, playerGuess):
        self.guess = playerGuess

    def checkLetter(self):
        if not(playerGuess.isdigit()):
            for character in word:
                if(character == playerGuess):
                    output = "Match"
                    print(output)
                else:
<<<<<<< HEAD
                    
                    print (character)
=======
                    output = "Not Match"
                    print(output)
>>>>>>> 7d316bd6707436c03fcdd747e5c7a664df924876
        else:
            print("Please enter a letter, not a number")

playerGuess = input("Enter a letter guess: ")
guesser.checkLetter(playerGuess)    