##############################################################################
# Title: Act Six
# Date: 1/7/2026
##############################################################################
"""this contains all dialouge and options for act six"""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import utils
# put text varibles and list for options here




# Functions and Classes ------------------------------------------------------
def starting_text():
    print("\nTo get to the next dialouge click enter")
    print("\nEach time you click enter, scroll to the top")
    print("\nEnjoy!")
    print("\nEXTRA CREDIT: SURVIVE")
    print("Edition 1: You Should’ve Been Worth More Love Points")

    skip_count = 0
    skip = input("")
    if skip == '' and skip_count == 0:
        utils.clear()
        print(part_one)
    skip_count += 1
    skip = input("")
    if skip == '' and skip_count == 1:
        utils.clear()
        print(part_two)
    skip_count += 1
    skip = input("")
    if skip_count == 2 and skip == '':
        utils.clear()
        print(part_three) 
    skip_count += 1
    skip = input("")
    if skip_count == 3 and skip == '':
        utils.clear()
        print(part_four)
    skip_count += 1
    skip = input("")
    if skip_count == 4 and skip == '':
        utils.clear()
        print("How would you like to respond?")
        for option in first_choices:
            print(option)
        user_option = input("Enter your choice(number): ")
        if user_option == '1':
            print('\n you picked option 1')
            print(f"\n{reaction_one}")
        elif user_option == '2':
            print('\n you picked option 2')
    skip_count += 1
    skip = input("")
    if skip_count == 5 and skip == '':
        utils.clear()
        print(part_four)
    skip_count += 1
    skip = input("")
    if skip_count == 6 and skip == '':
        utils.clear()
        print(part_five)


def tutorial():
    utils.clear()
    print(tutorial_text)
    tut_count = 0
    skip = input("")
    if skip == '' and tut_count == 0:
        utils.clear()
        print(tut_one)
    tut_count += 1
    skip = input("")
    if tut_count == 1 and skip == '':
        utils.clear()
        print("How would you like to respond?")
        for option in second_choices:
            print(option)
        while True:
            user_option = input("Enter your choice(number): ")
            if user_option == '1':
                print('\n you picked Felix')
                name = "Felix"
                break
            elif user_option == '2':
                print('\n you picked Amelia')
                name = "Amelia"
                break
            else:
                print("Invalid input. Please enter '1' or '2'.")
    tut_count += 1
    skip = input("")
    if skip == '' and tut_count == 2:
        utils.clear()
        print(tut_two)

