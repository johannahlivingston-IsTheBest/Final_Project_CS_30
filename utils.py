##############################################################################
# Title: clear
# Date: 12/17/2025
##############################################################################
"""Module for utilities"""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import os
import subprocess
from exceptions import ClearError


# Functions and Classes ------------------------------------------------------
def clear():
    """Clear the terminal."""
    if os.name == "nt":
        command = "cls"
    else:
        command = "clear"
    # Handle exceptions
    try:
        subprocess.run([command], shell=True)
    except:
        raise ClearError("Failed to clear terminal.")


# Main -----------------------------------------------------------------------
if __name__ == "__main__":
    # Testing
    print("Hello")
    name = input("Type your name: ")
    clear()
    print("Thank you")
