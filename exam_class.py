##############################################################################
# Title: Exams
# Date: 12/17/2025
##############################################################################
"""Exam class module."""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import puzzles


# Functions and Classes ------------------------------------------------------
class Exam:
    """Create an exam game."""
    def __init__(self, player):
        self.player = player
        self.exam_completed = 0
        self.puzzles = puzzles.Puzzles() 

    def start_exam_one(self):
        """Start an exam."""
        print("\nYou are about to take Exam One!")
        ready = input("\nAre you ready to begin the exam? (yes/no) ").lower()
        print("\nIt doesn't matter if your ready or not!")
        print("\nStarting the exam...")
        self.puzzles.riddle()

    def check_exam_completion(self):
        """Check if exam is complete."""
        if self.puzzles.rid_complete:
            self.exam_completed += 1
            self.player.stats["exams_completed"] = self.exam_completed
            print("\nCongratulations! You have passed Exam One.")
        else:
            print("\nYou failed Exam One.")
