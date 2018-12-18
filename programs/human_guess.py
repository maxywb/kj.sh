#!/usr/bin/env python3

import random

MAX_GUESS_COUNT = 3

def pick_number(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)


def get_int_from_user(prompt_message):
    while True:
        user_input = input(prompt_message + ": ")

        try:
            return int(user_input)
        except ValueError:
            print("'%s' is not an integer" % user_input)


def user_said_yes(prompt_message):
    while True:
        user_input = input(prompt_message + ": ")

        if user_input in ["y", "Y", "yes", "Yes"]:
            return True
        elif user_input in ["n", "N", "no", "No"]:
            return False
        else:
            print("please type 'y' or 'n'")


def main():
    print("welcome to Guess That Number!")
    print("your job is to guess the number that i pick.")
    print("you will enter the lower and upper bounds for the number that i will pick.")
    print("you will have %d guesses to pick the right number" % MAX_GUESS_COUNT)

    while True:
        lower_bound = get_int_from_user("please enter the lower bound")
        upper_bound = get_int_from_user("please enter the upper bound")

        secret_number = pick_number(lower_bound, upper_bound)

        for _ in range(MAX_GUESS_COUNT):
            human_guess = get_int_from_user("what is your guess?")
        
            if human_guess == secret_number:
                print("you got it!")
                break
            elif human_guess < secret_number:
                print("too low!")
            elif human_guess > secret_number:
                print("too high!")

        print("game over!")
                
        if user_said_yes("play again?"):
            continue
        else:
            print("goodbye!")
            break
        

if __name__ == "__main__":
    main()


