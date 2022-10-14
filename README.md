# cse210-03
#Jumper Game
Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

Rules of the game:
*The puzzle is a secret word randomly chosen from a list.
*The player guesses a letter in the puzzle.
*If the guess is correct, the letter is revealed.
*If the guess is incorrect, a line is cut on the player's parachute.
*If the puzzle is solved the game is over.
*If the player has no more parachute the game is over.
----
## Getting started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python3 Jumper 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- seeker              (source code for game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0


## Authors
Ron Ron Cabanjin
Robin Dickson
Nefi Perez Martinez
Sariah Tanner


From Sariah:
So our game specification says we need four classes.  I was thinking we could have one for the player, one for the puzzle(including the parachute status), one for randomly selecting from the list of words and one for guessing the letter(and adding to the dashes of the mystery word if it's correct)  

