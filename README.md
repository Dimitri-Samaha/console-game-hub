# Game Hub

A terminal game launcher bundling several small games for one or two players behind one menu (`game_manager.py`).

## Games included
- **Madlibs** (`madlibs.py`)
- **Rock Paper Scissors** (`rock_paper_scissors.py`)
- **Guess the Number** (`guess_the_number.py`)
- **Hangman** (`hangman.py`): picks a random English word using the `english_words` package.
- **Tic Tac Toe** (`tictactoe.py`, for two players)
- **Rocket Fight** (`rocket_fight.py`, a pygame spaceship duel for two players)
- **Speed Hands** (`speed_hands.py`): typing and mental arithmetic speed tests, with high scores saved to `word_ranks.txt` and `equation_ranks.txt`.

Login and guest access are handled by `password_control.py`, which stores accounts in `p_file.txt`.

## Requirements
```
pip install pygame english-words
```

## Running it
```
python game_manager.py
```
