# Import random module to picks random word out of the imported file
import random

# (OPTIONAL) Prints out the hangman welcome
print("||===================================================||")
print("||===================================================||")
print('||  _                                                ||')
print('|| | |                                               ||')
print('|| | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __     ||')
print("|| | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    ||")
print('|| | | | | (_| | | | | (_| | | | | | | (_| | | | |   ||')
print('|| |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|   ||')
print("||                     __/ |                         ||")
print("||                     |___/                         ||")
print("||===================================================||")
print("||===================================================||")
print('\033[1m' + '---------------- [Welcome To Hangman] -----------------' + '\033[0m')
print('\n')

# Prints out a piece of the man everytime a letter has been guessed wrong
HANGMAN = ['''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''', '''
  +---+
  |   |
  O   |
 \|/  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 \|/  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 \|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

# opening the file of the hangman words that will be used
with open("HangMan Words.txt", "r") as f:
    # read the contents in the file
    f_contents = f.read()
    # reads the content and extract individual words and store them in a list for used
    RandomWord = list(map(str, f_contents.split()))
# Random word that will be guessed
word = RandomWord
# selecting a random string in the list
words = random.choice(word)
# amount of guesses the player has
guesses = 6
# empty string for words the user needs to type in
guess = " "

# While loop to begin the game until the user loses or wins
while True:
    letter = input("Enter a letter [IN UPPER CASE]: ")
    capitalized_letter = letter.upper()

    # Ensures that there is only one guess
    if letter not in guess:
        guess += letter
    # Print out letter(s) if the letter(s) is in the word and how many times it is in the word
    if letter in words:
        print(f"Letter is in word!({words.count(letter)})times")

    # Takes away a guess if the letters(s) is not in the word
    elif letter not in words:
        guesses -= 1
        print(HANGMAN[guesses])
        print("Letter is not in word: ", guesses, "turns left")
    # If player runs out of guesses they lose the game
    if guesses == 0:
        print("GAME OVER: You Lose! ")
        break
    # checks if the user has guessed the word correctly or not
    failed = False

    # iterates through the letters in the string by converting the string into a set of unique characters
    for letter in ''.join(set(words)):
        # check to see if that letter is in that unique set of characters that was guessed
        if letter not in guess:
            # if a letter is not in the word the failure is true
            failed = True

    # iterating through the letter in the word
    for letter in words:
        # if the letter is guessed it prints out the letter on the same line
        if letter in guess:
            print(letter, end="")
        # print out an underscore (_) for the amount of letters in the word, as well as the letters that are not guessed
        else:
            print(" _ ", end="")
    print("\n")
    # if the user gets all the letters in the word they win and the loop breaks
    if not failed:
        print("YOU WON!!")
        break

# print out what the word was
print(f"The word is {words}")
