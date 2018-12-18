import random

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
