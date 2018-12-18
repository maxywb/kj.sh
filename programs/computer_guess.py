#!/usr/bin/env python3

import util

MAX_GUESS_COUNT = 3

def main():
    print("welcome to Guess That Number!")
    print("your job is to pick the number that i gues.")
    print("you will enter the lower and upper bounds for the number that you will pick.")
    print("i will have %d guesses to pick the right number" % MAX_GUESS_COUNT)

    while True:
        lower_bound = util.get_int_from_user("please enter the lower bound")
        upper_bound = util.get_int_from_user("please enter the upper bound")

        for _ in range(MAX_GUESS_COUNT):
            guess = (upper_bound + lower_bound) / 2
        
            if util.user_said_yes("is %d your number?" % guess):
                print("i win!")
                break
            elif util.user_said_yes("is %d less than your number?" % guess):
                lower_bound = guess
            else:
                print("%d must be greater than your number" % guess)
                upper_bound = guess

            continue

        print("game over!")

        if util.user_said_yes("play again?"):
            continue
        else:
            print("goodbye!")
            break



if __name__ == "__main__":
    main()
