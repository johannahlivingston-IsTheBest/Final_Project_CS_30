###############################################################################
# Title: Puzzles for game
# Class: CS30
# Assignment: Final project
# Name:Johannah Livingston
# Version: 1.0
# Date: 12/17/2025
###############################################################################
'''
This program has a bunch of different games inside a game class. They games
include match character description, rock - paper - scissors, riddles, 
unscramble scrambled word, and multiple choice/ termanology.
'''
###############################################################################
# Imports and Global Variables------------------------------------------------- 
import random 
rid_list = [
   """I'm sharp and shiny, held in a fight, A hero swings me with all their might. What am I?""", 
    """ I have wings but I do not fly like a bird,I breathe fire and guard gold unheard. What am I?""",
    """I wear a robe and carry a staff,I cast spells but never laugh. Who am I?"""
]
# Classes -------------------------------------------------------------------
class Puzzles:
   def __init__(self):
      pass
   def rock_paper_scissors(self):
      pass
   def match_des(self):
      pass
   def riddle(self,rid_list):
      num = 0
      for i in range(3):
         print("\n")
         print(str(i + 1)+ ". " + rid_list[i])
      answer_one = input("\n What is the answer to the first riddle? ").lower
      if answer_one == " sword":
         print("Correct!")
      else: 
         print("wrong")
         

        
   def scramble(self):
      pass
   def multi_choice(self):
      pass
puzzles = Puzzles()  
# Main ------------------------------------------------------------------------
puzzles.riddle(rid_list)