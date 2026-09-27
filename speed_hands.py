import os
import time
import random as rand
from english_words import get_english_words_set
eng_word = get_english_words_set(["web2"], lower=True, alpha=True)

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
wfilename = os.path.join(_BASE_DIR, "word_ranks.txt")
efilename = os.path.join(_BASE_DIR, "equation_ranks.txt")


def change_ranks(rank_list, filename):
    file = open(filename, "w")
    ranks_string = ""
    for ranks in rank_list:
        ranks_string = ranks_string + ",".join(ranks)
        ranks_string = ranks_string + "\n"
    file.write(ranks_string)
    file.close()
    return ranks_string


def load_top5(filename):
    file = open(filename, "r")
    rank_list = []
    for line in file.readlines():
        line = line[:-1]
        rank_list.append(line.split(","))
    return rank_list


def check_rank(user, score, filename):
    rank_list = load_top5(filename)
    for i in range (0, len(rank_list)):
        rls = float(rank_list[i][1])
        if float(score) < rls:
            rank_list.insert(i, [user, str(score)])
            rank_list.pop()
            print("You are in rank " + str(i+1))
            break
    rank_list = change_ranks(rank_list, filename)
    print(rank_list)
    return rank_list


def rand_5word():
    eng_list = list(eng_word)
    time_list = []
    i = 0
    while i < 5:
        wrong_word = True
        x = rand.randint(0, len(eng_list))
        rand_word = eng_list[x]
        time_1 = time.time()
        while wrong_word:
            user_input = input(rand_word + ": ")
            if user_input == rand_word:
                final_time = time.time() - time_1
                time_list.append(final_time)
                print(int(final_time))
                wrong_word = False
                i += 1
            else:
                print("TRY AGAIN!!")
    moy = (time_list[0] + time_list[1] + time_list[2] + time_list[3] + time_list[4]) / 5
    score = round(moy, 2)
    print("Your average per word is " + str(score))
    return score


def rand_5equation():
    i = 0
    op_list = ["+", "-", "*"]
    time_list = []
    while i < 5:
        a = rand.randint(1, 10)
        b = rand.randint(1, 10)
        o = rand.randint(0,2)
        equat = str(a) + op_list[o] + str(b)
        sol = eval(equat)
        time_1 = time.time()
        not_true = False
        while not not_true:
            user_input = input(equat + "= ")
            if not user_input == "":
                user_input = int(user_input)
                if user_input == sol:
                    final_time = time.time() - time_1
                    print(int(final_time))
                    not_true = True
            else:
                print("WRONG!")
        time_list.append(final_time)
        i += 1
    moy = (time_list[0] + time_list[1] + time_list[2] + time_list[3] + time_list[4]) / 5
    score = round(moy, 2)
    print("Your average per equation is  " + str(score))
    return score


def pbouchon(filename):
    "pBouchon, Score = 3"
    name = "Test"
    score = "3"
    check_rank(name, score, filename)
    return score


def gbouchon(filename):
    "gBouchon, Score = 6"
    name = "Test"
    score = "6"
    check_rank(name, score, filename)
    return score


if __name__ == "__main__":
    choice = input("Word[w] or equations[e]??")
    if choice.lower() == "w":
        rand_5word()
    elif choice.lower() == "e":
        rand_5equation()

    elif choice.lower() == "pbw":
        pbouchon(wfilename)
    elif choice.lower() == "gbw":
        gbouchon(wfilename)
    elif choice.lower() == "pbe":
        pbouchon(efilename)
    elif choice.lower() == "gbe":
        gbouchon(efilename)


## Game manager call this function for words
def game_manager_tt(user):
    score = rand_5word()
    check_rank(user, score, wfilename)


## Game manager call this function for equations
def game_manager_es(user):
    score = rand_5equation()
    check_rank(user, score, efilename)
