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
# Classes ---------------------------------------------------------------------------------------------------------
class Puzzles:
   def __init__(self):
      pass
   def rock_paper_scissors(self):
      pass
   def match_des(self):
      pass
   def riddle(self,rid_list):
     # Exam One
      num = 0
      for i in range(3):
         print("\n")
         print(str(i + 1)+ ". " + rid_list[i])
      answer_one = input("\n What is the answer to the first riddle? ").lower()
      answer_two = input("\n What is the answer to the second riddle? ").lower()
      answer_three = input("\n What is the answer to the third riddle? ").lower()
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
      elif correct_answers_count == 2:
         print("\nYou got 67%" )    
      elif correct_answers_count == 1:
         print("\nYou got 33%" )   
      elif correct_answers_count == 0:
         print("\nYou failed" )     
      print(f"\nYou got {correct_answers_count} out of 3 right ")


   
   def scramble(self):
      pass
   def multi_choice(self):
      pass
puzzles = Puzzles()  
# Main --------------------------------------------------------------------------------------------------------------
puzzles.riddle(rid_list)