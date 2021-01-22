# Hangman by: Visaagan Sivagnanasuntharam
# The graphics of the hangman are located in a different module


import random

# Module where Hangman Graphics are held
import hangmanGraphics
pictures = hangmanGraphics.get


def introduction():
    print("Hello, Welcome to Hangman by Visaagan!")
    username = input("What is your name? ")
    print(f"Hey {username}, Welcome to Hangman. We will being in 3 seconds.")


def gameBoard(pictures, incorrectLetters, correctLetters, answer):
    print()
    print("   HANGMAN")
    print(pictures[len(incorrectLetters)])
    print()
    print("Incorrect Letters:", end=" ")
    for char in incorrectLetters:
        print(char, end=" ")
    print()
    spaces = "_" * len(answer)

    for n in range(len(answer)):
        if answer[n] in correctLetters:
            spaces = spaces[:n] + answer[n] + spaces[n+1:]

    for char in spaces:
        print(char, end=" ")
    print()


def userGuess(preconditionGuess):
    while True:
        guess = input("Guess the character or type the whole word to solve: ").lower().strip()
        if guess == answer:
            return answer
        if len(guess) != 1:
            print("You guessed the word incorrectly!\n")
        elif guess in preconditionGuess:
            print("You have already guessed that letter, please try again.\n")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("You may only type in a letter.\n")
        else:
            return guess


def playAgain():
    userInput = input("Would you like to play again? (y/n): ").lower().strip()
    if userInput == 'y':
        return True
    else:
        return False


words = ['science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'recursive', 'objects', 'functions', 'dictionaries', 'tuples', 'hangman']


# Preparing game for fresh start
introduction()
incorrectLetters = ""
correctLetters = ""
answer = random.choice(words)
gameFinished = False

while not gameFinished:
    while True:
        # Prints game-board after every guess
        gameBoard(pictures, incorrectLetters, correctLetters, answer)

        # Keeps track of user guesses
        guess = userGuess(incorrectLetters + correctLetters)

        if guess in answer:
            correctLetters += guess
            foundLetters = True
            for n in range(len(answer)):
                if answer[n] not in correctLetters:
                    foundLetters = False
                    break
            if foundLetters:
                print(f"You won! The word was {answer}!\n")
                gameFinished = True
                break
        else:
            incorrectLetters += guess
            if len(incorrectLetters) > 5:
                print(f"You have lost! The correct word was {answer}!\n")
                gameFinished = True
                break

    if gameFinished:
        if playAgain():
            # Reset game settings
            correctLetters = ""
            incorrectLetters = ""
            answer = random.choice(words)
            gameFinished = False
        else:
            print("Thank you for playing Hangman!")
            gameFinished = True

