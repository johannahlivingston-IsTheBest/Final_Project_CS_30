###############################################################################
# Title: Main code
# Class: CS30
# Assignment: Final project
# Name:Johannah, Aditi, Atticus
# Version: 5
# Date: 01/14/2026
###############################################################################
'''This is the main code that runs the entire game by importing and executing
the different acts in sequence. It's also were you would just press run to start
the game.
'''
###############################################################################
# Imports and Global Variables-------------------------------------------------
import act_one
import act_two
import act_three
import act_four_plus_five
import act_six
import act_seven
import act_eight
from player_class import Player

player = Player()


# Main--------------------------------------------------------------------------
# ACT 1
act_one.starting_text(player)
act_one.tutorial_intro(player)
# ACT 2
act_two.act_two_tutorial(player)
# ACT 3
act_three.act_three(player)
# ACT 4
act_four_plus_five.act_four(player)
# ACT 5
act_four_plus_five.act_five(player)
# ACT 6
act_six.act_six(player)
# ACT 7
act_seven.act_seven(player)
# ACT 8
act_eight.act_eight(player)
