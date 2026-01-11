##############################################################################
# Title: Act Four
# Date: 1/7/2026
##############################################################################
"""this contains all dialouge and options for act four"""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import utils
# put text varibles and list for options here

# Act 4 story segments

act4_intro = '''CHAPTER 4 - Divine Object Quest: Rock, Paper, Scissors of Fate!

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

UPDATE: BEINGS OF HIGHER POWER COMMENTARY UNLOCKED!

After surviving your first challenge, 
the Beings of Higher Power suggest you lay 
low and adjust to school life. 
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

[MAP PLACEHOLDER]
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

[MAP PLACEHOLDER] 
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
Excellent entrance, Player.

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

[MAP PLACEHOLDER]  
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

# Functions and Classes ------------------------------------------------------


def print_story(text, player):
    print(text.format(name=player.name))
    utils.wait_for_continue(player)
    utils.clear()

def act_four(player):
    utils.wait_for_continue(player)
    utils.clear()

    # Step through all story segments
    story_segments = [
        act4_intro,
        act4_month_summary,
        act4_hint,
        act4_hint2,
        act4_forest_intro,
        act4_divine_object,
        act4_rps_intro,
        act4_rps_intro2
    ]

    for segment in story_segments:
        utils.print_story(segment, player)

    while True:
        wins = 2
        if wins >= 1 : 
            # success path
            utils.clear()
            story_segments_success = [
            success_one,
            success_two,
            success_three,
            success_four
            ]
            for segment in story_segments_success:
                utils.print_story(segment, player)
        else:
            # Failure path
            utils.clear()
            story_segments_fail = [
                fail_one,
                fail_two,
                fail_three,
                fail_four,
                fail_five
            ]
            for segment in story_segments_fail:
                utils.print_story(segment, player)
            exit()