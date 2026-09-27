from os import remove
import random

from english_words import get_english_words_set
eng_word = get_english_words_set(["web2"], lower=True, alpha=True)
eng_list = list(eng_word)


def chooseWord(wordlist):
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
lettersNotGuessed = letters.split(" ")


def getGuessedWord(secretWord, lettersGuessed):
    guessedWord = "_ " * len(secretWord)
    guessedWord = guessedWord.split(" ")
    for l in lettersGuessed:
      t = secretWord.count(l)
      if t == 1:
        letterIndex = secretWord.index(l)
        del(guessedWord[letterIndex])
        guessedWord.insert(letterIndex, l)
      else:
        for _ in range(0, t):
          letterIndex = secretWord.index(l)
          secretWord = secretWord[:letterIndex] + " " + secretWord[letterIndex+1:]
          del(guessedWord[letterIndex])
          guessedWord.insert(letterIndex, l)
    guessedWord = "".join(guessedWord)
    return guessedWord


def isWordGuessed(secretWord, guessedWord):
  return guessedWord == secretWord


def getAvailableLetters(lettersUsed):
  for l in lettersUsed:
    if l in lettersNotGuessed:
      letterIndex = lettersNotGuessed.index(l)
      del(lettersNotGuessed[letterIndex])
  availableLetters = "".join(lettersNotGuessed)
  return availableLetters
    

def hangman(secretWord):
  leng = len(secretWord)
  print(f"Welcome to the game Hangman!!\n"
        f"I am thinking of a word that is {leng} letters long.")
  lettersGuessed = []
  lettersUsed = []
  i = 10
  while not isWordGuessed(secretWord, getGuessedWord(secretWord, lettersGuessed)) == True and i != 0:
    print(f"You have {i} wrong guesses left!")
    print("Available letters: " + getAvailableLetters(lettersUsed))
    playerInput = input("Please guess a letter: ").lower()
    if playerInput in "".join(lettersUsed):
      print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
    elif playerInput in secretWord:
      lettersGuessed.append(playerInput)
      print("Good guess: " + getGuessedWord(secretWord, lettersGuessed)) 
    else:
      print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
      i -= 1
    lettersUsed.append(playerInput)
  if isWordGuessed(secretWord, getGuessedWord(secretWord, lettersGuessed)) == True:
    print("Congratulations!")
  elif i == 0:
    print("Sorry you ran out of guesses!!")
    print("The secret word was " + secretWord)
    playAgain = input("Do you want to play again??[yes] [no] ").lower()
    if playAgain == "yes":
      secretWord = chooseWord(eng_list).lower()
      hangman(secretWord)


def play():
    secretWord = chooseWord(eng_list).lower()
    hangman(secretWord)
    return 

if __name__ == "__main__":
    play()
