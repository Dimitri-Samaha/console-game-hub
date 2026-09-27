import random


def convert_to_i(text):
    text = text.lower()
    if text == 'rock' or text == 'r':
        i = 1
    elif text == 'paper' or text == 'p':
        i = 2
    elif text == 'scissors' or text == 's':
        i = 3
    return i


def display_title(x):
    if x == 1:
        return 'Rock'
    elif x == 2:
        return 'Paper'
    elif x == 3:
        return 'Scissors'


def choose_comp():
    ## if x=1 x=rock, if x=2 x=paper, if x=3 x=scissors
    x = random.randint(1, 3)
    return x


def check_win(i, x):
    if x == i:
        return ("It's a tie.")
    elif x == 2 and i == 1 or x == 1 and i == 3 or x == 3 and i == 2:
        return ("You lost!")
    elif i == 2 and x == 1 or i == 1 and x == 3 or i == 3 and x == 2:
        return ("You Won!")


def play():

    y = input('Rock, Paper or Scissors? ')

    i = convert_to_i(y)

    x = choose_comp()

    print(check_win(i, x))


if __name__ == "__main__":
    play()
