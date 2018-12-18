#!/usr/bin/env python3

import util


MAX_GUESS_COUNT = 3


def main():
    print("welcome to Guess That Number!")
    print("your job is to guess the number that i pick.")
    print("you will enter the lower and upper bounds for the number that i will pick.")
    print("you will have %d guesses to pick the right number" % MAX_GUESS_COUNT)

    while True:
        lower_bound = util.get_int_from_user("please enter the lower bound")
        upper_bound = util.get_int_from_user("please enter the upper bound")

        secret_number = util.pick_number(lower_bound, upper_bound)

        for _ in range(MAX_GUESS_COUNT):
            human_guess = util.get_int_from_user("what is your guess?")
        
            if human_guess == secret_number:
                print("you got it!")
                break
            elif human_guess < secret_number:
                print("too low!")
            elif human_guess > secret_number:
                print("too high!")

        print("game over!")
                
        if util.user_said_yes("play again?"):
            continue
        else:
            print("goodbye!")
            break
        

if __name__ == "__main__":
    main()


