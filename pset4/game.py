import random

import re

r = random

def main():
    target = level_choice()
    guesses(target)


def level_choice():
    while True:
        level = input("Level: ")
        if re.fullmatch(r"[1-9]\d*", level):
            target = random.randint(1, int(level))
            return target


def guesses(t):
    while True:
        guess = input("Guess: ")
        if re.fullmatch(r"[1-9]\d*", guess):
            guess = int(guess)
            if guess > t:
                print("Too large!")
            elif guess < t:
                print("Too small!")
            else:
                print("Just right!")
                break


if __name__ == "__main__":
    main()

