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

scram_list = ['DHISEL', 'BRO', 'FTASF', 'LAEMR']

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
      correct_answers_riddle = 0
      if answer_one == "sword":
         correct_answers_riddle += 1
      if answer_two == "dragon":
         correct_answers_riddle += 1
      if answer_three == "wizard":
         correct_answers_riddle += 1
      print(correct_answers_riddle)
      if correct_answers_riddle == 3:
         print("\nYou got 100%")
      elif correct_answers_riddle == 2:
         print("\nYou got 67%" )    
      elif correct_answers_riddle == 1:
         print("\nYou got 33%" )   
      elif correct_answers_riddle == 0:
         print("\nYou failed" )     
      print(f"\nYou got {correct_answers_riddle} out of 3 right ")

   def scramble(self,scram_list):
      # exam gisgdi
      scram_des = """put something here about what this exam is about and how to play fvhdivuhivuh"""
      print(scram_des)
      play = input("Are you ready?").lower()
      if ((play == "yes") or (play == "y")):
         print("Your time starts now.")
      else:
         print("To bad! Your times starts now!")

      for word in range(4):
         print(str(word + 1) + ". " + scram_list[word])
         print("\n")
      answer_one = input("What is the answer to the first scrambled word?").lower()
      answer_two = input("\nWhat is the answer to the second scrambled word?").lower()
      answer_three = input("\nWhat is the answer to the third scrambled word?").lower()
      answer_four = input("\nWhat is the answer to the fourth scrambled word?").lower()
      correct_answers_scram = 0
      if answer_one == "shield":
         correct_answers_scram += 1

      if answer_two == "orb":
         correct_answers_scram += 1

      if answer_three == "staff":
         correct_answers_scram += 1

      if answer_four == "realm":
         correct_answers_scram += 1  

      if correct_answers_scram == 4:
         print("\nYou got 100%")

      elif correct_answers_scram == 3:
         print("\nYou got 75%" )   

      elif correct_answers_scram == 2:
         print("\nYou got 50%" ) 

      elif correct_answers_scram == 1:
         print("\nYou got 25%" ) 

      elif correct_answers_scram == 0:
         print("\nYou failed" )  

      print(f"\nYou got {correct_answers_scram} out of 4 right ")
      
    
   def multi_choice(self):
      pass
puzzles = Puzzles()  
# Main --------------------------------------------------------------------------------------------------------------
puzzles.scramble(scram_list)