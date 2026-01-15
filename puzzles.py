###############################################################################
# Title: Puzzles for game
# Class: CS30
# Assignment: Final project
# Name: Johannah Livingston
# Version: 1.0
# Date: 12/17/2025
###############################################################################
"""
This program has a bunch of different games inside a game class. They games
include match character description, rock - paper - scissors, riddles,
unscramble scrambled word, and multiple choice/ termanology.
"""
###############################################################################
# Imports and Global Variables-------------------------------------------------
import random

rid_list = [
    """I'm sharp and shiny,
held in a fight,
A hero swings me with all their might.
What am I?""",
    """ I have wings but I do not fly like a bird,
I breathe fire and guard gold unheard.
What am I?""",
    """I wear a robe and carry a staff,
I cast spells but never laugh.
Who am I?"""
]

desc_list = [
    "insert character one description here",
    "insert character two description here",
    "insert character three description here"
]

hand_choices = ["rock", "paper", "scissors"]


# Classes----------------------------------------------------------------------
class Puzzles:
    '''
      This class contains various puzzle games including match character
      description, rock-paper-scissors, riddles, and unscramble scrambled
      words. For each puzzle type, there are methods to execute the game logic
      and return the results. This code is then used in different acts of the
      main game.
    '''

    def __init__(self):
        # i dint use this ever
        self.puzzle_types = [
            "match_des",
            "rock_paper_scissors",
            "riddle",
            "scramble",
            "multi_choice"
        ]
        self.rid_complete = False
        self.char_des = {
            "Crown Prince": {
                "name": "Alexander Aurelion",
                "nickname": "Alex",
                "personality": (
                    "Charismatic, playful, impulsive, deeply protective.\n"
                    "Hides pressure beneath charm."
                )
            },
            "Grand Duke": {
                "name": "Serene Valemont",
                "nickname": "Ren",
                "personality": (
                    "Calm, analytical, reserved, strategic.\n"
                    "Soft humor revealed in private."
                )
            },
            "Tower Master": {
                "name": "Theron Ravenhart ",
                "nickname": "Nyx",
                "personality": (
                    "Intelligent, intimidating, secretive.\n"
                    "Deadly competence paired with quiet protectiveness."
                )
            }
        }

    def rock_paper_scissors(self):
        '''
         allows the player to play rock-paper-scissors against
         a divine orb. It returns the number of rounds won by the player.
         wins: int - The number of rounds won by the player.
         hand_choices: list - The possible hand choices. user and orb can pick
         round_num: int - The current round number.
         vaild_choice: bool - Indicates if the player's choice is valid.   
         user_choice: str - The player's chosen hand.
         orb_choice: str - The Divine Orb's chosen hand.
        '''
        print("Remember: If you tie that's zero wins ")
        wins = 0
        hand_choices = ["rock", "paper", "scissors"]

        for round_num in range(3):
            vaild_choice = False
            while not vaild_choice:
                user_choice = input(
                    "\nPlease type rock, paper, or scissors: "
                ).lower()

                if user_choice not in hand_choices:
                    print(
                        "\nInvalid choice. Please choose rock, paper, "
                        "or scissors."
                    )
                else:
                    vaild_choice = True
                    orb_choice = random.choice(hand_choices)
                    print(f"\nThe Divine Orb chose: {orb_choice}")

                    if user_choice == orb_choice:
                        print("It's a tie!")
                    elif user_choice == "rock" and orb_choice == "scissors":
                        print("You win! Rock crushes scissors.")
                        wins += 1
                    elif user_choice == "paper" and orb_choice == "rock":
                        print("You win! Paper covers rock.")
                        wins += 1
                    elif user_choice == "scissors" and orb_choice == "paper":
                        print("You win! Scissors cut paper.")
                        wins += 1
                    else:
                        print("You lose! Better luck next time.")

        print(f"\nYou won {wins} out of 3 rounds.")
        return wins

    def match_des(self):
        '''
        presents the player with three character descriptions to
        match to the correct character. It returns the number of correctly
        answered matches.
        correct_matches: int - The number of correctly matched descriptions.
        user_match: str - The player's match for the first description.
        user_match_two: str - The player's match for the second description.
         user_match_three: str - The player's match for the third description.
        '''
        print("You will be given three character descriptions.")
        print("Your task is to match each description to the correct character.")
        correct_matches = 0

        print("\nWhich character has this personality: ")
        print(f"\n{self.char_des['Crown Prince']['personality']}")
        print("____________________________________________")

        options = ["1. Crown Prince", "2. Grand Duke", "3. Tower Master"]
        for option in options:
            print(f"\n{option}")

        user_match = input(
            "\nEnter the number of the character that matches "
            "the description: "
        )

        if user_match == "1":
            correct_matches += 1
            print("Correct.")
        else:
            print("Incrorrect")

        for option in options:
            print(f"\n{option}")

        print("\nWhich character has this name: ")
        print(f"\n{self.char_des['Grand Duke']['name']}")
        print("____________________________________________")

        user_match_two = input(
            "\nEnter the number of the character that matches "
            "the description: "
        )

        if user_match_two == "2":
            correct_matches += 1
            print("Correct! One more to go!")
        else:
            print("Incrorrect")

        print("True of False?")
        print(
            f"{self.char_des['Tower Master']['name']} personality is "
            f"{self.char_des['Tower Master']['personality']} "
        )
        print("____________________________________________")

        options = ["1.True", "2.False"]
        for option in options:
            print(f"\n{option}")

        user_match_three = input(
            "\nEnter the number 1 for true and 2 for false: "
        )

        if user_match_three == "1":
            print("Wow.... Correct")
            correct_matches += 1
        else:
            print(".....Incorrect")

        return correct_matches

    def riddle(self):
        '''presents the player with three riddles to solve.
        It returns the number of correctly answered riddles.
        num: int - The number of correctly answered riddles.
        answer_one: str - The player's answer to the first riddle.
        answer_two: str - The player's answer to the second riddle.
        answer_three: str - The player's answer to the third riddle.
        correct_answers_count: int - The count of correctly answered riddles.
        rid_complete: bool - Indicates if the player completed the riddle puzzle.'''
        print("\nYou will be given three riddles to solve.")

        num = 0
        for i in range(3):
            print("\n")
            print(str(i + 1) + ". " + rid_list[i])

        answer_one = input(
            "\nWhat is the answer to the first riddle? "
        ).lower()
        answer_two = input(
            "\nWhat is the answer to the second riddle? "
        ).lower()
        answer_three = input(
            "\nWhat is the answer to the third riddle? "
        ).lower()

        correct_answers_count = 0

        if answer_one == "sword":
            correct_answers_count += 1
        if answer_two == "dragon":
            correct_answers_count += 1
        if answer_three == "wizard":
            correct_answers_count += 1

        print(correct_answers_count)

        if correct_answers_count == 3:
            print("\nYou got 100%")
            self.rid_complete = True
        elif correct_answers_count == 2:
            print("\nYou got 67%")
            self.rid_complete = True
        elif correct_answers_count == 1:
            print("\nYou got 33%")
            self.rid_complete = False
        elif correct_answers_count == 0:
            print("\nYou got 0%")
            self.rid_complete = False

        print(
            f"\nYou got {correct_answers_count} out of 3 right "
        )
        return correct_answers_count

    def scramble(self):
        '''
        This method presents the player with four scrambled words to
        unscramble.returns the number of correctly unscrambled words.

        riddle_answer_one: str - The player's answer to the first scrambled
                                word.
        riddle_answer_two: str - The player's answer to the second scrambled
                                word.
         riddle_answer_three: str - The player's answer to the third scrambled
                                word.
         riddle_answer_four: str - The player's answer to the fourth scrambled
                                word.
         riddle_answers_count: int - The count of correctly unscrambled words.
        '''
        riddle_answer_one = input(
            "\n 1. Unscramble this word DHISEL: "
        ).lower()
        riddle_answer_two = input(
            "\n 2. Unscramble this word BRO: "
        ).lower()
        riddle_answer_three = input(
            "\n 3. Unscramble this word FTASF: "
        ).lower()
        riddle_answer_four = input(
            "\n 4. Unscramble this word LAEMR: "
        ).lower()

        riddle_answers_count = 0

        if riddle_answer_one == "shield":
            riddle_answers_count += 1
        if riddle_answer_two == "orb":
            riddle_answers_count += 1
        if riddle_answer_three == "staff":
            riddle_answers_count += 1
        if riddle_answer_four == "realm":
            riddle_answers_count += 1

        if riddle_answers_count == 4:
            print("\nYou got 100%")
        elif riddle_answers_count == 3:
            print("\nYou got 75%")
        elif riddle_answers_count == 2:
            print("\nYou got 50%")
        elif riddle_answers_count == 1:
            print("\nYou got 25%")
        elif riddle_answers_count == 0:
            print("\nYou failed")

        print(
            f"\nYou got {riddle_answers_count} out of 4 right "
        )
        return riddle_answers_count

    def wordle(self):
        print("You have to guess the correct word in 6 tries.")
        print("The word is a five letter word.")
        print("If you need help, type 'help' to get a hint. "
              "You can only use the hint once."
              )

        wordle_answer = "water"
        attempts = 6
        hint_used = False
        win = True

        # Create the result display
        letter1 = "_"
        letter2 = "_"
        letter3 = "_"
        letter4 = "_"
        letter5 = "_"

        print("\n ___ ___ ___ ___ ___")

        attempt = 0
        while attempt < attempts:
            guess = input(
                f"\nAttempt {attempt + 1}: Enter your 5-letter guess: "
            ).lower()

            if guess == "help" and not hint_used:
                hint_used = True
                print(
                    "Hint: It's something that is blue "
                    "and you can drink it"
                )
                continue

            if len(guess) != 5:
                print("Please enter a 5-letter word.")
                continue

            attempt += 1

            for letter in guess:
                if letter in wordle_answer:
                    print(f"The letter {letter} is in the word.")
                else:
                    print(f"The letter {letter} is not in the word.")

            if guess[0] == wordle_answer[0]:
                letter1 = guess[0].upper()
            if guess[1] == wordle_answer[1]:
                letter2 = guess[1].upper()
            if guess[2] == wordle_answer[2]:
                letter3 = guess[2].upper()
            if guess[3] == wordle_answer[3]:
                letter4 = guess[3].upper()
            if guess[4] == wordle_answer[4]:
                letter5 = guess[4].upper()

            print(f"\n {letter1} {letter2} {letter3} {letter4} {letter5}")

            if guess == wordle_answer:
                print("Congratulations! You've guessed the correct word!")
                return win

        print(
            "Sorry, you've used all your attempts. "
            f"The correct word was '{wordle_answer}'."
        )
        return False


puzzles = Puzzles()


# Main-------------------------------------------------------------------------

# puzzles.match_des()
