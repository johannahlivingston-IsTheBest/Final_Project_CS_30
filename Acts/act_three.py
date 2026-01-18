##############################################################################
# Title: Act Three
# Date: 1/7/2026
##############################################################################
"""This contains all the dialogue and options for act three."""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import utils
import puzzles
from world import game_loop

# put text variables and list for options here
act3_intro = '''CHAPTER 3 - Scrabble Challenge: “Who messed with my books?!"

You step through the academy gates, 
marble floors gleaming beneath your boots.
A translucent map snaps open in front of you, 
floating cheerfully despite your growing dread.
'''

act3_intro2 = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Navigation initialized!
Use the map to move around the academy.

First stop: Administration Office.
Objective: Collect your textbooks.
Side note: Someone scrambled them.
Whoops.
'''

act3_scrambled_books = '''
Inside the office, a stack of books waits for you on a desk.
You pick one up.

The text inside is completely scrambled.
Letters refuse to make sense.
Sentences twist into nonsense.

Your stomach sinks.
'''

act3_scrambled_books2 = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Important reminder!
Understanding the written language of this world is… 
kind of necessary to survive.

Good news!
This is your first test.

Bad news!
Failing it results in death.

Have fun!
━━━━━━━━━━━━━━━━━━━━━━
'''

act3_choice_prompt = '''How do you handle the situation?

1. Focus carefully and try to unscramble the words.
2. Ask a passing student for help.
3. Complain loudly to the system.
'''

puzzles = puzzles.Puzzles()


# Functions and Classes ------------------------------------------------------

def act_three(player):
    """Print act 3.

    Parameters:
        player (Player): the player object
    """
    utils.wait_for_continue(player)
    utils.clear()

    story_segments = [
        act3_intro,
        act3_intro2,
        (game_loop, ("gate", "administration office")),
        act3_scrambled_books,
        act3_scrambled_books2
    ]

    # print each segment
    for segment in story_segments:
        try:
            segment[0](*segment[1])
        except TypeError:
            utils.print_story(segment, player)

    print(act3_choice_prompt)

    # first choice
    while True:
        choice = input("\nEnter your choice (number): ")

        # PATH 1 — Focus carefully
        if choice == "1":
            utils.clear()
            print('''
You take a deep breath and focus.
You block out the noise of the office, the whispers of other students,
the crushing awareness that your life depends on this.

You begin the challenge.
''')
            # TEMP RESULT
            riddle_answers_count = puzzles.scramble()

            if riddle_answers_count >= 2:
                utils.wait_for_continue(player)
                utils.clear()
                print('''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

CONGRATULATIONS!
You successfully deciphered the language of the game world!

Honestly? We’re impressed.

You may now read signs, books, warnings,
and passive-aggressive noble notes.

Books acquired.
First challenge cleared.
Survival probability: slightly improved.
━━━━━━━━━━━━━━━━━━━━━━
''')
                utils.wait_for_continue(player)
                utils.clear()
                break
            else:
                utils.wait_for_continue(player)
                utils.clear()
                print('''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Oh.
This is awkward.

You have failed the test.
Judgment passed.

GAME OVER.
You die.
━━━━━━━━━━━━━━━━━━━━━━
''')
                exit()

        # PATH 2 — Ask for help
        elif choice == "2":
            utils.clear()
            print('''
You turn to a nearby student.
"Hey, could you help me read this?"

They glance at your uniform, then at you.
"Ugh. A commoner?"
"Figure it out yourself."

They walk away laughing.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

HAHAHAHA.
Oh Player… did you really think they’d help?

Social hierarchy exists for a reason.
Nice try, though.

Now. Figure it out yourself.
━━━━━━━━━━━━━━━━━━━━━━
''')
            riddle_answers_count = puzzles.scramble()

            if riddle_answers_count >= 2:
                utils.wait_for_continue(player)
                utils.clear()
                print('''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Well done!
Spite-fueled learning is still learning.

Language comprehension unlocked.
Books acquired.
━━━━━━━━━━━━━━━━━━━━━━
''')
                utils.wait_for_continue(player)
                utils.clear()
                break
            else:
                utils.wait_for_continue(player)
                utils.clear()
                print('''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Tragic.

GAME OVER.
You die.
━━━━━━━━━━━━━━━━━━━━━━
''')
                exit()

        # PATH 3 — Complain
        elif choice == "3":
            utils.clear()
            print('''
"This is ridiculous!" you snap.
"The Beings of Higher Power are STUPID!"

The air around you goes very, very cold.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Disrespect detected.
Mercy denied.

GAME OVER.
You die.
━━━━━━━━━━━━━━━━━━━━━━
''')
            exit()

        else:
            print("Invalid input. Please enter 1, 2, or 3.")


# Main -----------------------------------------------------------------------
if __name__ == "__main__":
    from player_class import Player
    test_player = Player()
    act_three(test_player)
