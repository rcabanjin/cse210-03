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
        self._guesser = Guesser()
        self._jumper = Jumper()
        self._word = random_word
        self._is_playing = True
    #Starts the game by running by calling the main class
    
    def start_game(self):
    #Starts the game by running the main game loop
        #create a loop to run the game
        while self._is_playing:
        #call the classes created
            self._get_inputs()
            self._do_update()
            self._do_output()
  
    def _get_inputs(self):
        self._word
        
    def _do_update(self):
        self._jumper.process()

    def _do_output(self):
        pass
