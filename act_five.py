##############################################################################
# Title: Act Five
# Date: 1/7/2026
##############################################################################
"""this contains all dialouge and options for act five"""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import utils,puzzles
# put text varibles and list for options here
act6_intro = '''CHAPTER 6 - A Shadow's Invitation: Please don't kill me, Mr. Assassin

As you leave and head back to the dormitory from the ball, 
you feel a presence behind you.
You turn.

A tall figure stands half in shadow.
Dark attire. Controlled posture.
Eyes like cold steel observing a battlefield.

You feel he is dangerous somehow.
'''
act6_route_detected = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

New route interest detected.
Magic Tower / Assassin Guild Heir:
Theron Ravenhart (Codename: Nyx)

Warning:
Interest does not equal safety.
━━━━━━━━━━━━━━━━━━━━━━
'''
act6_invitation = '''
━━━━━━━━━━━━━━━━━━━━━━
THERON RAVENHART:
“…You’re quite interesting.”
━━━━━━━━━━━━━━━━━━━━━━

His gaze flicks briefly to the Crown Prince.
Then to the Grand Duke.
'''
act6_invitation2 = '''
━━━━━━━━━━━━━━━━━━━━━━
THERON:
“Meet me in the library. 
Three nights from now.”

A pause.

“Don’t worry.
I don’t bite… yet.”
━━━━━━━━━━━━━━━━━━━━━━

Before you can respond, he’s gone.
The night fades...
'''
act6_timeskip = '''
TIME SKIP — THREE DAYS LATER

Academia Fortunae continues as if nothing happened.
Classes. Whispers. Side glances.

You feel watched.
Always watched.

On the third night, 
an urgent system message pops up
'''
act6_library_notice = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Destination unlocked: Academy Library
Attendance: Mandatory

Reason:
You were invited by a highly dangerous individual.

Refusal:
Strongly discouraged (for survival reasons).
━━━━━━━━━━━━━━━━━━━━━━

You sigh.

translucent map snaps open.
Then you go.
(Of course you do.)
[ADD MAP HERE] 
'''
act6_library_intro = '''

The library is dark.
Too dark.

Candles flicker along towering shelves.
Shadows stretch where they shouldn’t.

Theron stands at the center.
Back turned.
'''
act6_library_intro2 = '''
━━━━━━━━━━━━━━━━━━━━━━
THERON:
“You came.”
━━━━━━━━━━━━━━━━━━━━━━

He turns slowly.

━━━━━━━━━━━━━━━━━━━━━━
THERON:
 “Good.”
━━━━━━━━━━━━━━━━━━━━━━

He raises a hand.
The doors slam shut.
Books shudder.
Letters tear themselves from pages, 
swirling violently through the air.

'''
act6_test_intro = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

WARNING.
Hostile magic detected.

This is not a lesson.
This is a test.
━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━━━━━━━━━━
THERON:
“You caught the attention of the Crown Prince.”
“And the future Grand Duke.”
His eyes narrow.
“That makes you suspicious.”
━━━━━━━━━━━━━━━━━━━━━━
'''
act6_test_intro2 = '''
A pause.

━━━━━━━━━━━━━━━━━━━━━━
 THERON:
“…I needed to know if you’re merely 
manipulative or used a trick to lure 
the Crown Prince and the Future Duke.”

“…Or genuinely interesting.”
━━━━━━━━━━━━━━━━━━━━━━

The magic surges—out of control.
A spell misfires.
The Fire spirals toward him.

'''
act6_wordle_prompt = '''
━━━━━━━━━━━━━━━━━━━━━━
 SYSTEM MESSAGE:

 CRITICAL EVENT.

 Theron Ravenhart is in danger from the fire.
 Your response will be evaluated.
━━━━━━━━━━━━━━━━━━━━━━

 A glowing panel slams into your vision.

'''
act6_wordle_prompt2 = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
Emergency Test Initiated: WORDLE

Solve the word.
Five letters.
Theme: The spell destabilizing the room.

Failure results in…
unfortunate conclusions.
━━━━━━━━━━━━━━━━━━━━━━

'''
act6_success = '''
You think fast.
Letters rearrange.
They lock into place.

“H2O.”

The magic collapses inward.
You run—

You slam into Theron, 
arms wrapping around him as the 
fire extinguishes itself in a burst of light.

Silence.
Your breathing is the loudest sound in the room.
'''
act6_success_followup = '''
Theron freezes.
Then—slowly—his hand rests against your back.

━━━━━━━━━━━━━━━━━━━━━━
THERON (quietly):
“…You didn’t hesitate.”

“You ran into a fire to save me.”
━━━━━━━━━━━━━━━━━━━━━━
'''
act6_fail = '''
You hesitate.
The letters refuse to settle.
The magic stutters—then fractures.

The flames collapse incorrectly.

Theron moves instantly—
a blur of motion, a flash of sigils—
he lands several steps away, unharmed.

You are thrown back by the backlash, hitting the floor hard.
The fire dies out in a violent hiss.

Silence.
'''
act6_fail_followup = '''
Theron looks at you.
Not angry.
Not impressed.
Disappointed.

━━━━━━━━━━━━━━━━━━━━━━
 THERON (cold):
 “…I see.”
━━━━━━━━━━━━━━━━━━━━━━
'''
act6_fail_followup2 = '''
He studies you carefully now, 
as if reassessing every moment since the ballroom.

━━━━━━━━━━━━━━━━━━━━━━
THERON:
 “So you are not quick under pressure.”
 “And yet…”
 “…you drew the attention of the Crown Prince 
 and the future Grand Duke.”
━━━━━━━━━━━━━━━━━━━━━━

'''
act6_fail_followup3 = '''
His eyes sharpen.

━━━━━━━━━━━━━━━━━━━━━━
THERON:
 “That suggests manipulation.”
 “Or luck.”
 “Neither makes you safe.”
 ━━━━━━━━━━━━━━━━━━━━━━
'''
act6_fail_followup4 = '''
 Theron turns away, shadows curling around him.

━━━━━━━━━━━━━━━━━━━━━━
 THERON:
“I won’t kill you.”
“Not yet.”
━━━━━━━━━━━━━━━━━━━━━━

A pause.

━━━━━━━━━━━━━━━━━━━━━━
THERON:
“But if I discover you’ve endangered 
 the kingdom through deceit…”

“…I won’t hesitate next time.”
━━━━━━━━━━━━━━━━━━━━━━
'''
act6_fail_followup5 = '''
The doors unlock with a heavy thud.
The library settles.
The candles stop flickering.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Event Complete.
Player survived.
Trust not earned.
Suspicion increased.

Recommendation:
 Be more interesting next time.
━━━━━━━━━━━━━━━━━━━━━━

"Yea thanks for the great advice system," 
you remark sarcastically
'''
puzzle = puzzles.Puzzles()


# Functions and Classes ------------------------------------------------------

def act_six(player):
    utils.wait_for_continue(player)
    utils.clear()

    story_segments = [
        act6_intro,
        act6_route_detected,
        act6_invitation,
        act6_invitation2,
        act6_timeskip,
        act6_library_notice,
        act6_library_intro,
        act6_test_intro,
        act6_test_intro2,
        act6_wordle_prompt,
        act6_wordle_prompt2
    ]

    for segment in story_segments:
        utils.print_story(segment, player)

    # WORDLE PLACEHOLDER RESULT
     # change later when game is added
    win = puzzle.wordle()
           
    if win == True:
        # Story outcome
        utils.clear()
        print(act6_success)
        utils.wait_for_continue(player)
        utils.clear()

        print(act6_success_followup)
        utils.wait_for_continue(player)
        utils.clear()

        # Update love points
        player.love_points["Magic Tower Master/ Assassin"] += 2

        

        print(f'''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Affection Update:
• Magic Tower Master / Assassin: +2
• Crown Heir: No Change
• Grand Duke Heir: No Change
━━━━━━━━━━━━━━━━━━━━━━
        ''')

        utils.wait_for_continue(player)
        utils.clear()

        print(f'''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Current Affection Levels:
• Crown Heir: {player.love_points["Crown Heir"]}
• Grand Duke Heir: {player.love_points["Grand Duke Heir"]}
• Magic Tower Master / Assassin: {player.love_points["Magic Tower Master/ Assassin"]}

Threat Assessment:
{player.name} deemed interesting.
Execution cancelled.

The Beings of Higher Power mutter:
“Well. That ruins the assassination.”
━━━━━━━━━━━━━━━━━━━━━━
        ''')
        utils.wait_for_continue(player)
        utils.clear()
        print(f'''
Theron steps back, gaze still guarded—but changed.

━━━━━━━━━━━━━━━━━━━━━━             
THERON:
 “You live.”
“…For now.”
━━━━━━━━━━━━━━━━━━━━━━
        ''')

    else:
        # Story outcome
        utils.clear()
        print(act6_fail)
        utils.wait_for_continue(player)
        utils.clear()

        print(act6_fail_followup)
        utils.wait_for_continue(player)
        utils.clear()

        print(act6_fail_followup2)
        utils.wait_for_continue(player)
        utils.clear()

        print(act6_fail_followup3)
        utils.wait_for_continue(player)
        utils.clear()

        # Update love points
        player.love_points["Magic Tower Master/ Assassin"] -= 4

        print(f'''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Affection Update:
• Magic Tower Master / Assassin: -4
• Crown Heir: No Change
• Grand Duke Heir: No Change
━━━━━━━━━━━━━━━━━━━━━━
        ''')

        utils.wait_for_continue(player)
        utils.clear()

        print(f'''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Current Affection Levels:
• Crown Heir: {player.love_points["Crown Heir"]}
• Grand Duke Heir: {player.love_points["Grand Duke Heir"]}
• Magic Tower Master / Assassin: {player.love_points["Magic Tower Master/ Assassin"]}

Threat Assessment:
{player.name} deemed suspicious.
Interest significantly reduced.

The Beings of Higher Power whisper:
“Oof. LOL"
━━━━━━━━━━━━━━━━━━━━━━
        ''')

        utils.wait_for_continue(player)
        utils.clear()

        print(act6_fail_followup4)
        utils.wait_for_continue(player)
        utils.clear()

        print(act6_fail_followup5)
        utils.wait_for_continue(player)
        utils.clear()
