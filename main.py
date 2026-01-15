###############################################################################
# Title: Main code
# Class: CS30
# Assignment: Final project
# Name:Johannah, Aditi, Atticus
# Version: 5
# Date: 01/14/2026
###############################################################################
'''
This program has a bunch of different games inside a game class. They games
include match character description, rock - paper - scissors, riddles, 
unscramble scrambled word, and multiple choice/ termanology.
'''
###############################################################################
# Imports and Global Variables------------------------------------------------- 

import act_one
import act_two
import act_three
import act_four
import act_five
import act_six
import act_seven
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
act_four.act_four_part_one(player)
act_four.act_four_part_two(player)

# ACT 5
act_five.act_six(player)

#ACT 6
act_six.act_seven(player)

#ACT 7
act_seven.act_eight(player)

