##############################################################################
# Title: clear
# Date: 12/17/2025
##############################################################################
"""Module for utilities"""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import os
import subprocess

RULES_TEXT = ''' Loading Rules...

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Rules of the World:

1. Love Points determine survival.
2. If any Love Points reach zero, the player dies.
3. Choices that displease a character may result in death.
4. Graduation from Academia Fortunae is mandatory.
5. Failing challenges or exams results in death.
6. Forming bonds unlocks endings.
7. Higher beings observe the player for entertainment,
   and may occasionally intervene.

━━━━━━━━━━━━━━━━━━━━━━
'''


# Functions and Classes ------------------------------------------------------
class ClearError(Exception):
    """Error when terminal fails to clear."""
    def __init__(self, msg):
        self.msg = msg


def clear():
    """Clear the terminal."""
    command = "cls" if os.name == "nt" else "clear"  # Cross-platform
    # Handle exceptions
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        # raise ClearError("Failed to clear terminal.")
        print("\n[Terminal failed to clear]\n")


def wait_for_continue(player):
    while True:
        user_input = input("").lower().strip()

        if user_input == "":
            return  # continue story

        elif user_input == "stats":
            clear()
            player.display_info()
            input("\nPress Enter twice to return to the story...")
            #clear()

        elif user_input == "rules":
            clear()
            print(RULES_TEXT)
            input("\nPress Enter twice to return to the story...")
            #clear()

        else:
            print("Press Enter to continue, or type 'stats' to view player info.")


def print_story(text, player):
    print(text.format(name=player.name))
    wait_for_continue(player)
    clear()


# Main -----------------------------------------------------------------------
if __name__ == "__main__":
    # Testing
    print("Hello")
    name = input("Type your name: ")
    clear()
    print("Thank you")
