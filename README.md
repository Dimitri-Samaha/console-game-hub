# Game Hub

A terminal game launcher bundling several small single- and two-player games behind one menu (`game_manager.py`).

## Games included
- **Madlibs** (`madlibs.py`)
- **Rock Paper Scissors** (`rock_paper_scissors.py`)
- **Guess the Number** (`guess_the_number.py`)
- **Hangman** (`hangman.py`) — picks a random English word via the `english_words` package
- **Tic-Tac-Toe** (`tictactoe.py`, two-player)
- **Rocket Fight** (`rocket_fight.py`, two-player pygame spaceship duel)
- **Speed Hands** (`speed_hands.py`) — typing and mental-arithmetic speed tests, with high scores saved to `word_ranks.txt` / `equation_ranks.txt`

Login/guest access is handled by `password_control.py`, which stores accounts in `p_file.txt`.

## Requirements
```
pip install pygame english-words
```

## Running it
```
python game_manager.py
```
