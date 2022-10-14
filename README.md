# cse210-03
# Jumper Game
Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

## Rules of the game:
* The puzzle is a secret word randomly chosen from a list.
* The player guesses a letter in the puzzle.
* If the guess is correct, the letter is revealed.
* If the guess is incorrect, a line is cut on the player's parachute.
* If the puzzle is solved the game is over.
* If the player has no more parachute the game is over.
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
* Ron Ron Cabanjin
* Robin Dickson
* Nefi Perez Martinez
* Sariah Tanner

```
Director (Ron)
•	Start_game – Start the game by running a loop
•	Get_inputs – Prompt user to guess a letter from A to Z 
•	Do_updates – compare the letters from the random words  to user input
•	Do_outputs – Add letter to the secret word or remove a part from a parachute

Secret_word (Rob)
•	_init__ = Make a list of randoms words
•	Get_hint = display message to inform the guesser
•	Letter_found = Whether or not the guesser found the letter

Guesser (Nefi)
•	_unit_ = choose a new secret word from the list
•	Read_input = convert all text to lowercase

Display (Sariah)
•	Num_characters = Display the number of characters
•	Make_Parachute = Display the parachute 
```