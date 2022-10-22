from game.secretword import random_word
from game.parachute import chute

import random


class Jumper():
    """Jumper 
    
    Attriibutes:
        word: 
        guess:
        reveal:
        lives:
        won:
        lose:
    """

    def __init__(self):
        self.word = random_word
        self.guess = ""
        self.reveal = list(len(self.word)*'_')
        self.lives = 4
        self.won = False
        self.lose = False

    def check_letter(self, letter, word):

        for i in range(0,len(self.word)):
            letter = self.word[i]
            if self.guess == letter:
                self.reveal[i] = self.guess
        if '_' not in self.reveal:
            return True
        else:
            return False

    def show(self):
        """show prints out a picture of the Chute"""
        
        print(chute[4 - self.lives])
        print(self.reveal)


    def process(self):
        """This is the logic while trying to get the guessing game to work
        It checks the letter"""
        while self.won == False and self.lives > 0:
            self.show()
            self.guess = input('Please guess a letter: ')
            self.guess = self.guess.upper()
          
            if self.guess == self.word:
                self.won = True
                self.reaveal = self.word

            if len(self.guess) == 1 and self.guess in self.word:
                self.won = self.check_letter(self.guess, self.word)  

            else:
                self.lives-=1

            #Print a winning message!
            if self.won == True: 
                print(f"Nice! you guessed {self.word}")
                print("")

            else:
                print("Keep Guessing")
                print(" ")

            #Print a losing message :(
            if self.lives == 0:
                self.lose = True
            if self.lose == True:
                print(chute[4])
                print("I am sorry, you've lost!")
                print("You have failed to save the jumper!")
                print(f"The word was, {self.word}")
                self.lost = False
                print("""
             ___   ___                   ___   
            |   | |   |                 |   |   
            \   \ /   / _____  ___ ___  |   |     _____  ____   ____
             \       / /     \ |  |  |  |   |    /     \/  __\_/ __ \ 
              \     /  |  |  | |  |  |  |   |___ |  |  |\__  \|  ___/
               |___|   \_____/ \_____/  |_______|\_____//____/ \____|     
           ________                          _______
          /   ____/_____    _____   ____    /       \ __  __  ____  _____  
         /   /  ___\__  \  /     \_/ __ \   |   |   ||  ||  |/ __ \|  ___|
         \   \__\  \/ __ ||  Y Y  |  ___/   |   |   | \  Y /|  ___/|  |    
          \_______/|_____||__|_|__|\____|   \_______/  \__/  \____||__|        
                              
""")


