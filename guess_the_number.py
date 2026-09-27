import random


def guess(x):
    random_number = random.randint(1, x)

    while x != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > random_number:
            print("Sorry. Too High!")
        elif guess < random_number:
            print('Sorry. Too low!')
        else:
            print('YAY!')
    return


def computer_guess():
    low = 1
    high = 100
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??')
        if feedback.lower() == 'h':
            high = guess - 1
        elif feedback.lower() == 'l':
            low = guess + 1
        elif feedback == "c" or 'C':
            print('YAY!!')
    return

        
def play():
    choice = input("Do u want to guess[g] or do u want the computer to guess[c]?? ")
    if choice == "g":
        choose_X = int(input("x: "))
        guess(choose_X)
    if choice == "c":
        computer_guess()


if __name__ == "__main__":
    play()
