import password_control as pass_cont

import tictactoe as ttt
import madlibs as ml
import rock_paper_scissors as rps
import guess_the_number as gn
import rocket_fight as rf
import hangman as hm
import speed_hands as sh


def account_recognition():
    user = pass_cont.log_sign_func()
    return user


def game_menu(user):
    keep_playing = True
    while keep_playing:
        num_player = input("Singleplayer[sp] or Two[tp]?? press [q] to quit. ")
        if num_player.lower() == "sp":
            schoice = input("What do you want to play?? \nMadlibs[m], Rock Paper Scissors[rps],\nGuess the number[g], Hangman[h], Type test[tt], Equation speed[es]??\n\t press [q] to quit. ").lower()
            if schoice == "m":
                ml.play()
            elif schoice == "rps":
                rps.play()
            elif schoice == "g":
                gn.play()
            elif schoice == "h":
                hm.play()
            elif schoice == "tt":
                sh.game_manager_tt(user)
            elif schoice == "es":
                sh.game_manager_es(user)
        elif num_player.lower() == "tp":
            tchoice = input("What do you want to play?? \nTictactoe[t], Rocket Fight[r]?? ").lower()
            if tchoice == "t":
                ttt.play()
            elif tchoice == "r":
                rf.play()
        elif num_player.lower() == "q":
            keep_playing = False


if __name__ == "__main__":
    game_menu(user = account_recognition())
