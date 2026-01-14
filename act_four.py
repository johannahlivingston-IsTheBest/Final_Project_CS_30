##############################################################################
# Title: Act Four
# Date: 1/7/2026
##############################################################################
"""this contains all dialouge and options for act four"""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import utils
import puzzles
from world import game_loop
# put text varibles and list for options here

# Act 4 story segments

act4_intro = '''CHAPTER 4 - Divine Object Quest: Rock, Paper, Scissors of Fate!

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

UPDATE: BEINGS OF HIGHER POWER COMMENTARY UNLOCKED!

After surviving your first challenge, 
the Beings of Higher Power suggest you lay 
low and adjust to school life for a month. 
Sadly this means the bullying continues.

Also, they want to enjoy watching you struggle.
Translation: Try not to die you puny human,
and entertain us!
━━━━━━━━━━━━━━━━━━━━━━
'''
act4_month_summary = '''

A month passes.
You’ve barely survived.
Your backpack is missing one notebook.
Someone snickered at your lunch.
And yet… you’re alive.
'''
act4_hint = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Congratulations! 
You survived the month!

The first main affection event is approaching… 
You’ve heard whispers of it… the School Ball!
━━━━━━━━━━━━━━━━━━━━━━

"A school ball...how cliche," you remark.
'''
act4_hint2 = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

A major social event where connections are made, 
prospects are assessed, and nobles flaunt their influence.

Lucky for you… the Beings of Higher Power enjoyed your 
suffering over the past month and decide to take pity.

They leave a hint about a divine object in the forest.
It may help you acquire a dress.
━━━━━━━━━━━━━━━━━━━━━━

A translucent map snaps open in front of you, floating cheerfully!
Glowing lights mark your destination: The Forest.
'''
act4_forest_intro = '''

You follow the glowing lights from the map.
Branches sway, leaves crunch underfoot.

The forest is… slightly less scary than last week’s cafeteria, 
but only slightly. Suddenly, a glimmering object hovers in 
the clearing ahead. It sparkles almost smugly, 
like it knows you’re about to make a fool of yourself.
'''
act4_divine_object = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Ah, there it is.
The divine object.
Touch it. Don’t overthink it.
━━━━━━━━━━━━━━━━━━━━━━
'''
act4_rps_intro = '''
You reach out.
The moment your fingers brush it, 
a bubble of light expands around you, 
and the system chimes again.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

This is your first “human-world inspired” test: 
A game called Rock Paper Scissors.

Everything depends… entirely on your luck.

Win → You obtain a beautiful dress.
Lose → You obtain an ugly dress.
━━━━━━━━━━━━━━━━━━━━━━
'''
act4_rps_intro2 = '''

PLAYER ({name}):
“You’ve got to be kidding me… Rock Paper Scissors?”
“…Fine. Let’s get this over with.”

[ADD ROCK PAPER SCISSORS MINI-GAME HERE]
'''
success_one = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

PATH — Win:
You hold up the divine object and it transforms 
into a stunning, gorgeous ball dress.

Some Beings of Higher Power sigh.
“Well… you actually won. 
How disappointing,” they say
━━━━━━━━━━━━━━━━━━━━━━

You snicker at the beings of higher power.
'''
success_two = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Destination unlocked: School Ballroom
Head to the Ballroom.
━━━━━━━━━━━━━━━━━━━━━━

A translucent map snaps open in front of you
'''
success_three = '''
You follow it and head to the ballroom.
The ballroom doors swing open.

Conversation dies mid-sentence.
Crystal chandeliers bathe the room in gold. 
Music slows. 
Heads turn.

Your curly red hair catches the light, glowing like embers.
Your emerald-green dress flows perfectly, 
the color matching your forest-green eyes 
as if fate finally decided to be nice to you.

Whispers ripple through the crowd.
'''
success_four = '''
The Crown Prince pauses mid-conversation, 
crimson eyes locked on you, visibly stunned.

The Grand Duke Heir lowers his drink glass, 
gaze sharp, unreadable… but unmistakably fixed on you.

Neither looks away.
Your heart skips.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Affection Event Triggered.
Excellent entrance, {name}.

The Beings of Higher Power are… 
reluctantly impressed.
━━━━━━━━━━━━━━━━━━━━━━
'''
fail_one = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

PATH — Lose:
The divine object sputters and shimmers… 
then becomes an ugly, awkward dress.

The Beings of Higher Power snicker.
“You will look like a clown,” they say
━━━━━━━━━━━━━━━━━━━━━━

You sigh
'''
fail_two = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Destination unlocked: School Ballroom
Confidence not included.
Head to the Ballroom.
━━━━━━━━━━━━━━━━━━━━━━

The map pops open anyway.
No mercy. No rerolls.  
'''
fail_three = '''
You magically change into the dress, 
once you reach the Ballroom.

Your curly red hair is forced into a tragic, 
lopsided updo that defies physics.
The neon-pink fabric screams for help—and clashes 
violently with your eyes.

You step into the ballroom.

Silence.
Not the good kind.

A few nobles choke on their drinks.
Someone gasps.
Someone else laughs.
'''
fail_four = '''
At the corner of the room—

The Crown Prince freezes, eyes wide.
The Grand Duke stares.
Both look… stunned.
Not impressed.
Just then—

THWIP.

A sharp pain explodes in your chest.
You look down.
“…You have got to be kidding me,” you wheeze.

Then you collapse in a pool of blood.
'''
fail_five = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Ah. Unfortunate.
Just like your luck with the divine object,
your luck remains… impressively terrible.

You embarrassed yourself.
You looked like a clown.
And now you’ve been struck by a flying arrow at a formal ball.

However—
The Beings of Higher Power are extremely entertained.
You will be missed. Briefly.

GAME OVER.
━━━━━━━━━━━━━━━━━━━━━━
'''
act5_intro = ''' CHAPTER 5 - School Ball: The Crown Prince or the Duke Heir?

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Oh dear.
It appears your entrance was too… effective.
━━━━━━━━━━━━━━━━━━━━━━
'''
act5_scene_setup = '''

Both the Crown Prince and the Duke are visibly 
affected by your appearance.
Both feel compelled to approach you.
Both request the honor of the first dance.

They stop in front of you.

Two hands extend.
Two futures diverge.
'''
act5_system_message = '''

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Choose wisely, {name}.

These are powerful people.
Offending the wrong one may result in…
"death."
━━━━━━━━━━━━━━━━━━━━━━
'''

puzzles = puzzles.Puzzles()
# Functions and Classes ------------------------------------------------------


def print_story(text, player):
    print(text.format(name=player.name))
    utils.wait_for_continue(player)
    utils.clear()


def act_four_part_two(player):

    # Step through intro story segments before choice
    story_segments = [
        act5_intro,
        act5_scene_setup,
        act5_system_message
    ]

    for segment in story_segments:
        try:
            segment[0](segment[1])
        except TypeError:
            utils.print_story(segment, player)

    # Player choice
    while True:
        print("\nWho do you dance with?")
        print("1. Dance with the Crown Prince")
        print("2. Dance with the Duke")
        print("3. Ignore both")
        choice = input("\nEnter your choice (number): ")

        if choice == "1":
            # Dance with Crown Prince
            utils.clear()
            print('''
You take the Crown Prince’s hand.
A murmur ripples through the ballroom.
The Duke stiffens. His expression tightens — just for a moment.
You are led onto the dance floor.

━━━━━━━━━━━━━━━━━━━━━━
CROWN PRINCE:
"I do have a name, you know."
He smiles, softer now.
"My friends call me Alex."
"...You may, too."
━━━━━━━━━━━━━━━━━━━━━━
                  
Your heart does something inconvenient.
''')
            # Update love points
            player.love_points["Crown Heir"] += 2
            player.love_points["Grand Duke Heir"] -= 3
            player.love_points["Magic Tower Master/ Assassin"] += 1

            utils.wait_for_continue(player)
            utils.clear()
            print(f'''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
          
Affection Update:
• Crown Heir: +2
• Grand Duke Heir: -3
• Magic Tower Master/ Assassin: +1
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
• Magic Tower Master/ Assassin: {player.love_points["Magic Tower Master/ Assassin"]}

The Magician watches from the shadows.
Interest detected.

The Beings of Higher Power whisper:
“Ah. A politically sound choice. How dull.”
━━━━━━━━━━━━━━━━━━━━━━
''')
            utils.wait_for_continue(player)
            utils.clear()
            print('''
The dance ends.
You survive.
Then you discover the buffet.
And absolutely destroy it.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
                  
Observation:
The Player is indulging excessively.
                  
The Beings of Higher Power comment that you resemble
"a creature of considerable mass enjoying earthly pleasures."
━━━━━━━━━━━━━━━━━━━━━━
''')
            break  # end choice loop

        elif choice == "2":
            # Dance with Duke — GAME OVER
            utils.clear()
            print('''
You take the Duke’s hand.
The ballroom goes quiet.
Too quiet.
You feel it immediately.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
                  
Critical Social Error Detected.
Status Check:
Crown Prince Authority > Duke Authority

You have publicly humiliated the Crown Prince.
━━━━━━━━━━━━━━━━━━━━━━
''')
            utils.wait_for_continue(player)
            utils.clear()
            print('''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
                  
The Crown Prince is displeased.
And when royalty is displeased—
People die.
                  
The Beings of Higher Power shake their heads.
"So close. So stupid."

GAME OVER.
You die.
━━━━━━━━━━━━━━━━━━━━━━
''')
            exit()

        elif choice == "3":
            # Ignore both
            utils.clear()
            print('''
You smile politely.
Then… walk past them.
Straight to the refreshments.
The Crown Prince blinks.
The Duke exhales slowly.
From the shadows, someone watches with interest.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
                  
Affection Update:
• Crown Heir: +1
• Duke: +1
• Magician/Assassin: +2
━━━━━━━━━━━━━━━━━━━━━━
''')
            # Update love points
            player.love_points["Crown Heir"] += 1
            player.love_points["Grand Duke Heir"] += 1
            player.love_points["Magic Tower Master/ Assassin"] += 2

            utils.wait_for_continue(player)
            utils.clear()
            print(f'''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
                  
Current Affection Levels:      
• Crown Heir: {player.love_points["Crown Heir"]}
• Grand Duke Heir: {player.love_points["Grand Duke Heir"]}
• Magic Tower Master/ Assassin: {player.love_points["Magic Tower Master/ Assassin"]}

The Magician watches from the shadows.
Interest detected.

The Beings of Higher Power giggle.
“Oh. Bold. Socially reckless. We like this one.”
━━━━━━━━━━━━━━━━━━━━━━
''')
            utils.wait_for_continue(player)
            utils.clear()
            print(f'''

You eat.
And eat.
And eat some more.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
                  
The Player once again displays
"a remarkable commitment to indulgence."
━━━━━━━━━━━━━━━━━━━━━━

PLAYER ({player.name}):
"Nothing is going to stop me from having fun."
The night ends.
Alive.
Fed.
Judged.
                  
You leave, satisfied with the Buffet.
''')
            
            break  # end choice loop

        else:
            print("Invalid input. Please enter 1, 2, or 3.")


def act_four_part_one(player):

    # Step through all story segments
    story_segments = [
        act4_intro,
        act4_month_summary,
        act4_hint,
        act4_hint2,
        (game_loop, "forest"),
        act4_forest_intro,
        act4_divine_object,
        act4_rps_intro,
        act4_rps_intro2
    ]

    for segment in story_segments:
        try:
            segment[0](segment[1])
        except TypeError:
            utils.print_story(segment, player)

    wins = puzzles.rock_paper_scissors()
    if wins > 1 : 
        # success path
        utils.wait_for_continue(player)
        utils.clear()
        story_segments_success = [
            success_one,
            success_two,
            (game_loop, "ballroom"),
            success_three,
            success_four
        ]
        for segment in story_segments_success:
            try:
                segment[0](segment[1])
            except TypeError:
                utils.print_story(segment, player)
        
    else:
        # Failure path
        utils.wait_for_continue(player)
        utils.clear()
        story_segments_fail = [
            fail_one,
            fail_two,
            (game_loop, "ballroom"),
            fail_three,
            fail_four,
            fail_five
        ]
        for segment in story_segments_fail:
            try:
                segment[0](segment[1])
            except TypeError:
                utils.print_story(segment, player)
        exit()


