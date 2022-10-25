from tkinter import SE
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
        self._word = random_word
        self._guess = ""
        self._reveal = list(len(self._word)*'_')
        self._lives = 4
        self._won = False
        self._lose = False

    def _check_letter(self, letter, _word):

        for i in range(0,len(self._word)):
            letter = self._word[i]
            if self._guess == letter:
                self._reveal[i] = self._guess
        if '_' not in self._reveal:
            return True
        else:
            return False

    def show(self):
        """show prints out a picture of the Chute"""
        
        print(chute[4 - self._lives])
        print(self._reveal)


    def process(self):
        """This is the logic while trying to get the guessing game to work
        It checks the letter"""
        while self._won == False and self._lives > 0:
            self.show()
            self._guess = input('Please guess a letter: ')
            self._guess = self._guess.upper()
          
            if self._guess == self._word:
                self._won = True
                self._reaveal = self._word

            if len(self._guess) == 1 and self._guess in self._word:
                self._won = self._check_letter(self._guess, self._word)  

            else:
                self._lives-=1

            #Print a winning message!
            if self._won == True: 
                print(f"Nice! you guessed {self._word}")
                print("")

            else:
                print("Keep Guessing")
                print(" ")

            #Print a losing message :(
            if self._lives == 0:
                self._lose = True
            if self._lose == True:
                print(chute[4])
                print("I am sorry, you've lost!")
                print("You have failed to save the jumper!")
                print(f"The word was, {self._word}")
                self._lost = False
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


