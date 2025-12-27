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
hand_choices = ['rock', 'paper', 'scissors']
# Classes ---------------------------------------------------------------------------------------------------------
class Puzzles:
   def __init__(self):
      self.puzzle_types = ['match_des', 'rock_paper_scissors', 'riddle', 'scramble', 'multi_choice']
   def rock_paper_scissors(self):
      wins = 0
      for round in range(3):
         user_choice = input("Please choose rock, paper, or scissors: ").lower()
         if user_choice not in hand_choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
         dragon_choice = random.choice(hand_choices)
         print(f"The dragon chose: {dragon_choice}")
         if user_choice == dragon_choice:
            print("It's a tie!")
         elif user_choice == 'rock' and dragon_choice == 'scissors':
            print("You win! Rock crushes scissors.")
            wins += 1
         elif user_choice == 'paper' and dragon_choice == 'rock':
            print("You win! Paper covers rock.")
            wins += 1
         elif user_choice == 'scissors' and dragon_choice == 'paper':
            print("You win! Scissors cut paper.")
            wins += 1
         else:
            print("You lose! Better luck next time.")
      print(f"You won {wins} out of 3 rounds.")
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
   # Exam Two
      riddle_answer_one = input("\n 1. Unscramble this word DHISEL: ").lower()
      riddle_answer_two = input("\n 2. Unscramble this word BRO: ").lower()
      riddle_answer_three = input("\n 3. Unscramble this word FTASF: ").lower()
      riddle_answer_four = input("\n 4. Unscramble this word LAEMR: ").lower()
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
         print("\nYou got 75%" )    
      elif riddle_answers_count == 2:
         print("\nYou got 50%" )    
      elif riddle_answers_count == 1:
         print("\nYou got 25%" )   
      elif riddle_answers_count == 0:
         print("\nYou failed" )     
      print(f"\nYou got {riddle_answers_count} out of 4 right ")

   def wordle(self):
      print("This is your fifth exam. The wordle exam.")
      print("You have to guess the correct word in 6 tries.")
      print("The word is a five letter word.")
      print("If you need help, type 'help' to get a hint. You can only use the hint once.")
      wordle_answer = "flame"
      attempts = 6
      hint_used = False
      # Create the result display
      letter1 = "_"
      letter2 = "_"
      letter3 = "_"
      letter4 = "_"
      letter5 = "_"
      print("\n ___ ___ ___ ___ ___")
      for attempt in range(attempts):
         guess = input(f"\nAttempt {attempt + 1}: Enter your 5-letter guess: ").lower()
         if guess == "help" and not hint_used:
            hint_used = True
            print("Hint: It's something that burns and gives light.")
            attempt -= 1  # Do not count this as an attempt
            continue
         if len(guess) != 5:
            print("Please enter a 5-letter word.")
            attempt -= 1  # Do not count this as an attempt
            continue
         for letter in guess:
            if letter in wordle_answer:
               print(f"The letter {letter} is in the word.")
            else:
               print(f"The letter {letter} is not in the word.")
         if guess[0] == wordle_answer[0]:#f
            print("\nThe first letter is correct.")
            letter1 = guess[0].upper()
            print(f"\n {letter1} ___ ___ ___ ___")
         if guess[1] == wordle_answer[1]:#l
            print("\nThe second letter is correct.")
            letter2 = guess[1].upper()
            print(f"\n {letter1} {letter2} ___ ___ ___")
         if guess[2] == wordle_answer[2]:#a
            print("\nThe third letter is correct.")
            letter3 = guess[2].upper()
            print(f"\n {letter1} {letter2} {letter3} ___ ___")
         if guess[3] == wordle_answer[3]:#m
            print("\nThe fourth letter is correct.")
            letter4 = guess[3].upper()
            print(f"\n {letter1} {letter2} {letter3} {letter4} ___")
         if guess[4] == wordle_answer[4]:#e
            print("\nThe fifth letter is correct.")
            letter5 = guess[4].upper()
            print(f"\n {letter1} {letter2} {letter3} {letter4} {letter5}")
         if guess == wordle_answer:
            print("Congratulations! You've guessed the correct word!")
            break
         if attempt == attempts - 1:
            print(f"Sorry, you've used all your attempts. The correct word was '{wordle_answer}'.")
puzzles = Puzzles()  
# Main --------------------------------------------------------------------------------------------------------------
puzzles.wordle()