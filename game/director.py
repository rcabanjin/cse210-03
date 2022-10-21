
from game.guesser  import guesser
from game.jumper  import Display
from game.secret_word  import SecretWord

#class that handles the game events
class Director:
#Director class will control the sequence of play.

#sources / parts if game is:

    def __init__(self):
    #construct new Director
        self._guesser = guesser()
        self._display = Display()
        self._is_playing = True
    #Starts the game by running by calling the main class
    
    def start_game(self):
    #Starts the game by running the main game loop
        #create a loop to run the game
        while self._is_playing:
        #call the classes created
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    #call the classes created for getting the guesser's input letter    
    def _get_inputs(self):
        playmore_game = input ("Want to play more game?")
        self._is_playing = (playmore_game == "y".upper)

    #Update the guesser's correct letter    
    def _do_update(self):
        print (guesser.checkLetter(output))


    #call the classes created for showing the guesser input letters and remaining characters
    def _do_output(self):
        pass 