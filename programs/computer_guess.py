#!/usr/bin/env python3

def _user_said_yes():
    while True:
        user_input = raw_input("y/n")

        if user_input in ["y", "Y", "yes", "Yes"]:
            return True
        elif user_input in ["n", "N", "no", "No"]:
            return False
        else:
            print "type 'y' or 'n'"


