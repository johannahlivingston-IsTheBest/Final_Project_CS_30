##############################################################################
# Title: player class
# Date: 12/17/2025
##############################################################################
"""Module for player class."""
##############################################################################
# Imports and Global Variables -----------------------------------------------


# Functions and Classes ------------------------------------------------------
class Player:
    """General player class for most of the text portion of the game."""
    def __init__(self):
        self.name = None
        self.level = 1
        self.stats = {
            "title": "Commoner",
            "partner": None,
            "exams_completed": 0,
            "lives": 1
        }
        self.love_points = {
            "Crown Heir": 5,
            "Grand Duke Heir": 5,
            "Magic Tower Master/ Assassin": 5     
        }

    def display_info(self):
        """Displays player info."""
        print(f"\nLoading Player... {self.name}")
        print(f"""
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
              
Name: {self.name}
Title: {self.stats['title']}
Lives: {self.stats['lives']}
Partner: {self.stats['partner']}
""")
        print("\nCurrent Affection Levels: ")
        for k, v in self.love_points.items():
            print(f"• {k}: {v}")
        print("\n━━━━━━━━━━━━━━━━━━━━━━")
