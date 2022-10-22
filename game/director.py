import random
from game.jumper import Jumper
from game.guesser import Guesser
from game.secretword import random_word


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        guesser:
        jumper:
        secret_word:
        is_playing:

    """

    def __init__(self):
    #construct new Director
        self.guesser = Guesser()
        self.jumper = Jumper()
        self.word = random_word
        self.is_playing = True
    #Starts the game by running by calling the main class
    
    def start_game(self):
    #Starts the game by running the main game loop
        #create a loop to run the game
        while self.is_playing:
        #call the classes created
            self.get_inputs()
            self.do_update()
            self.do_output()
  
    def get_inputs(self):
        self.word
        
    def do_update(self):
        self.jumper.process()

    def do_output(self):
        pass
