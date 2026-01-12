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
desc_list = ["insert character one description here", 
             "insert character two description here", 
             "insert character three description here"]

hand_choices = ['rock', 'paper', 'scissors']
# Classes ---------------------------------------------------------------------------------------------------------
class Puzzles:
   def __init__(self):
      self.puzzle_types = ['match_des', 'rock_paper_scissors', 'riddle', 'scramble', 'multi_choice']
      self.rid_complete = False
      self.char_des = {'Crown Prince':{'name':'Alexander Aurelion', 
                                       'nickname': 'Alex',
                                       'personality':'''Charismatic, playful, impulsive, deeply protective.
                                       \nHides pressure beneath charm.'''},
                        'Grand Duke':{'name':'Serene Valemont', 
                                      'nickname': 'Ren',
                                      'personality':'''Calm, analytical, reserved, strategic.
                                       \nSoft humor revealed in private.'''},
                        'Tower Master':{'name':'Theron Ravenhart ', 
                                      'nickname': 'Nyx',
                                      'personality':'''Intelligent, intimidating, secretive.
                                       \nDeadly competence paired with quiet protectiveness.'''}}
   def rock_paper_scissors(self):
    print('''Remeber: If you tie that's zero wins ''')
    wins = 0
    
    for round in range(3):
        in_vaild_choice = False 
        while not in_vaild_choice:
            user_choice = input("Please choose rock, paper, or scissors: ").lower()
            if user_choice not in hand_choices:
                print("Invalid choice. Please choose rock, paper, or scissors.") 
            else:
                in_vaild_choice = True
                orb_choice = random.choice(hand_choices)
                print(f"The Divine Orb chose: {orb_choice}")
                if user_choice == orb_choice:
                    print("It's a tie!")
                elif user_choice == 'rock' and orb_choice == 'scissors':
                    print("You win! Rock crushes scissors.")
                    wins += 1
                elif user_choice == 'paper' and orb_choice == 'rock':
                    print("You win! Paper covers rock.")
                    wins += 1
                elif user_choice == 'scissors' and orb_choice == 'paper':
                    print("You win! Scissors cut paper.")
                    wins += 1
                else:
                    print("You lose! Better luck next time.")
    
    print(f"You won {wins} out of 3 rounds.")

   def match_des(self):
      print("You will be given three character descriptions.")
      print("Your task is to match each description to the correct character.")
      correct_matches = 0
      print('\nWhich character has this personality: ')
      print(f"\n{self.char_des['Crown Prince']['personality']}")
      # switch out the Characetr with the character names
      
      user_match = int(input("\nEnter the number of the character that matches the description: "))
      if user_match == 1:
         correct_matches += 1
         print('Correct.')
      else:
         print("Incrorrect")
      options = ['1. Crown Prince', '2. Grand Duke', '3. Tower Master']
      for option in options:
         print(f"\n{option}")
      print('\nWhich character has this name: ')
      print(f"\n{self.char_des['Grand Duke']['name']}")
      user_match_two = int(input("\nEnter the number of the character that matches the description: "))
      if user_match_two == 3:
         correct_matches += 1
         print("Correct! One more to go!")
      else:
         print("Incrorrect")
      print('True of False?')
      print(f"{self.char_des['Tower Master']['name']} personality is {self.char_des['Tower Master']['personality']} ")
      options = ['1.True', '2.False']
      for option in options:
         print(f"\n{option}")
      user_match_three = int(input("\nEnter the number 1 for true and 2 for false: "))
      if user_match_three == 1:
         print('Wow.... Correct')
         correct_matches += 1
      else:
         print('.....Incorrect')
      
      print(correct_matches)



         
   def riddle(self):
      print("\nYou will be given three riddles to solve.")
     # Exam One
      num = 0
      for i in range(3):
         print("\n")
         print(str(i + 1)+ ". " + rid_list[i])
      answer_one = input("\nWhat is the answer to the first riddle? ").lower()
      answer_two = input("\nWhat is the answer to the second riddle? ").lower()
      answer_three = input("\nWhat is the answer to the third riddle? ").lower()
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
         print("\nYou got 67%" )   
         self.rid_complete = True 
      elif correct_answers_count == 1:
         print("\nYou got 33%" )  
         self.rid_complete = False 
      elif correct_answers_count == 0:
         print("\nYou got 0%" ) 
         self.rid_complete = False 

      print(f"\nYou got {correct_answers_count} out of 3 right ")
      return correct_answers_count

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
      return riddle_answers_count

   def wordle(self):
      print("You have to guess the correct word in 6 tries.")
      print("The word is a five letter word.")
      print("If you need help, type 'help' to get a hint. You can only use the hint once.")
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
      for attempt in range(attempts):
         guess = input(f"\nAttempt {attempt + 1}: Enter your 5-letter guess: ").lower()
         attempt = 0
      while attempt < attempts:
         guess = input(f"\nAttempt {attempt + 1}: ").lower()

         if guess == "help" and not hint_used:
            hint_used = True
            print("Hint: It's something that is blue and you can drink it")
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
            return win
            break
         if attempt == attempts - 1:
            print(f"Sorry, you've used all your attempts. The correct word was '{wordle_answer}'.")
puzzles = Puzzles()  
# Main --------------------------------------------------------------------------------------------------------------
#print(f"{puzzles.char_des['Crown Prince']['nickname']}")

#puzzles.match_des()