#Hangman by: Visaagan Sivagnanasuntharam


#The graphics of the hangman are located in a different module
import hangmanGraphics
import random
import time

def introduction():
    print("Hello, Welcome to Hangman by Visaagan!")
    username = input("What is your name? ")
    print(f"Hey {username}, Welcome to Hangman. We will being in 3 seconds.")

def timer():
    for i in (3,2,1):
        print(i)
        time.sleep(1)
        i -= 1

def playAgain(user_answer):
    if user_answer == "y" or "Y" :
        return True
    else:
        return False

introduction()
timer()

words = ['The Office', 'Big Bang Theory', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']


answer = random.choice(words)

print("Guess the word")

guesses = ''

# any number of turns can be used here
turns = 7
graphics = 0

while turns > 0:

    # counts the number of times a user fails
    failed = 0

    # all characters from the input
    # word taking one at a time.
    for char in answer:

        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char)

        else:
            print("_")

            # for every failure 1 will be
            # incremented in failure
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")

        # this print the correct word
        print(f"The word is: {answer}")
        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("guess a character: ")

    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess not in answer:

        turns -= 1

        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")
        print(hangmanGraphics.get[graphics])
        graphics += 1

        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
