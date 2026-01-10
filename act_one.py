##############################################################################
# Title: Act_one
# Date: 1/6/2026
##############################################################################
"""This contains all the dialouge and options for ALL OF ACT one."""
##############################################################################
# Imports and Global Variables -----------------------------------------------

import utils

# text for the intro
part_one = '''You were reading an otome game synopsis on your phone.

"Ooooh a new version of my favorite otome game!"
"I should check it out when I get home"
A fantasy academy.
Love points.
Multiple endings.

You are lost in thought when you step off the curb.
You never saw the TRUCK.'''
part_two = '''CHAPTER 1 - At the Hospital: “Congratulations! You’re Dying.”

Darkness.
Then—

Beep.
Beep.
Beeeeeeep.

Your eyes crack open.

White ceiling.
Bright lights.
The distinct smell of disinfectant and regret.
You try to move.
Your body does not agree.
“…Am I… alive?” you mutter.

Before you can process anything, 
a translucent window snaps open in front of your face.

'''
part_three = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

WELCOME, PLAYER!

Current Location:
Hospital — Emergency Ward
Status:
CRITICALLY INJURED
━━━━━━━━━━━━━━━━━━━━━━

You blink.

“…Okay,” you say weakly. “This is either a dream or I’m concussed.”
'''
part_four = '''
The window cheerfully updates.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Bad news!
You were hit by a truck.
Like, REALLY hit.

Good news!
 You have been chosen by beings of higher power!
━━━━━━━━━━━━━━━━━━━━━━
'''
first_choices = ['1. What is happening right now?','\n2. “Beings of higher power…?”']
reaction_one = '''
The system pauses.
As if thinking...
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Ah.
Straight to the point.

In short?
You are dying.

In long?
You were hit by a truck, your body is failing, and you have caught the 
attention of some very bored entities called beings of higher power.

They have decided that if you manage to survive a game, 
you can survive the truck accident!
━━━━━━━━━━━━━━━━━━━━━━

'''
reaction_two = '''
The system brightens, almost excited.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Yes!
You noticed that part quickly.
Excellent.

They are ancient.
Powerful.
And extremely, painfully bored.

And you?
You are interesting.
Hence they have decided that if you manage to survive a game, 
you can survive the truck accident!
━━━━━━━━━━━━━━━━━━━━━━
'''
part_five = '''
The window expands, filling more of your vision.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Allow us to explain.

The beings observing you exist far beyond your understanding.
They have watched countless worlds.
Countless lives.

And frankly?
They are running out of things to do.

So they made a game, the one you have been playing and the one
that led you to be distracted and caused the accident with the truck.
━━━━━━━━━━━━━━━━━━━━━━
'''
part_six = '''

You have a bad feeling about this.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
They wanted entertainment.
Drama.
Romance.
Desperation.
They wanted to watch someone fight for their life using love
━━━━━━━━━━━━━━━━━━━━━━

The word “LOVE” sparkles obnoxiously.
'''
part_seven = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
And then they found you.

• 30 years old
• Never experienced romantic love
• Emotionally inexperienced
• Highly likely to panic

A perfect candidate
━━━━━━━━━━━━━━━━━━━━━━

“…Candidate?” you whisper.
'''
# text for the tutorial
tut_one = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
Yes! A candidate to have a chance to fall in love, 
have an adventure and survive death!

Don’t worry.
We’ll explain everything properly.

Including:
• The rules
• The stakes
• And how you can survive
━━━━━━━━━━━━━━━━━━━━━━


'''
second_choices = ['1. Felix','2. Amelia']
tut_two = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Excellent choice!

Preparing transfer…
Loading world…
Initializing Love Points…

Good luck, Player.
You’re going to need it.
━━━━━━━━━━━━━━━━━━━━━━
'''
# Functions and Classes ------------------------------------------------------
def starting_text():
    # Instructions for the player
    print("""
    To get to the next dialogue, press Enter.
    Each time you click enter, scroll to the top

    Note:
    - Each action you take is permanent and cannot be undone.
    - Once you advance the story, you cannot go back to reread 
      previous sections.

    Enjoy the game!

    EXTRA CREDIT: SURVIVE
    Edition 1: You Should’ve Been Worth More Love Points
    """)
    # Display the first part of the story
    input("")
    utils.clear()
    print(part_one)
    # Display the second part of the story
    input("")
    utils.clear()
    print(part_two)
    # Display the third part of the story
    input("")
    utils.clear()
    print(part_three) 
    # Display the fourth part of the story
    input("")
    utils.clear()
    print(part_four)
    # Present the first choice to the player
    input("")
    utils.clear() 
    print("How would you like to respond?")
    for option in first_choices:
        print(option)
    # Loop until the player enters a valid choice
    while True:
        user_option = input("Enter your choice(number): ")
        if user_option == '1':
            print('\nYou picked option 1')
            print(f"\n{reaction_one}")
            break
        elif user_option == '2':    
            print('\nYou picked option 2')
            print(f"\n{reaction_two}")
            break
        else:
            print("\nInvalid input. Please enter '1' or '2'.")
    # Display the fifth part of the story
    input("")
    utils.clear()
    print(part_five)
    # Display the sixth part of the story
    input("")
    utils.clear()
    print(part_six)
    # Display the seventh part of the story
    input("")
    utils.clear()
    print(part_seven)


def tutorial_intro(player):

    input("")
    utils.clear()
    print(tut_one)

    input("")
    utils.clear()
    print("For now pick your character identity/name")

    for option in second_choices:
        print(option)
    while True:
        user_option = input("Enter your choice(number): ")
        if user_option == '1':
            print('\nYou picked Felix')
            player.name = "Felix"
            break
        elif user_option == '2':
            print('\nYou picked Amelia')
            player.name = "Amelia"
            break
        else:
            print("\nInvalid input. Please enter '1' or '2'.")
    print(tut_two)
    

# Main -----------------------------------------------------------------------

