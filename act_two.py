
##############################################################################
# Title: Act_two
# Date: 1/7/2026
##############################################################################
"""This code contains all the dialouge and choices for act two of our game."""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import utils
# Get all text varibles here
act2_intro = '''CHAPTER 2 - Tutorial: “A COMMONER?!”

The world tilts.
The hospital room dissolves into light, 
the beeping of machines stretching into a long, distorted whine until—
Silence.

You gasp and stumble forward, boots scraping against stone.
Stone?
You steady yourself and look up.

Towering iron gates stretch endlessly into the sky, 
engraved with glowing runes. Beyond them lies a massive academy 
built from pale marble and gold, its spires piercing drifting clouds.
A translucent window snaps into existence in front of you, 
far too cheerful for the situation.
'''
act2_transfer = '''

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Transfer complete!
Welcome to your new reality, Player.
━━━━━━━━━━━━━━━━━━━━━━

You stare at the screen.
“…What?”

'''
act2_enrollment = '''

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

You are now enrolled in:
ACADEMIA FORTUNAE
Royal Academy of Magic, Nobility, and Emotional Suffering
━━━━━━━━━━━━━━━━━━━━━━

“…You’re joking,” you mutter.

“Wait, is this the otome game I was looking at 
right before I got hit by a truck?!”

“Am I inside of the game?!!!”

'''
act2_reality_check1 = '''

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

You are correct!
━━━━━━━━━━━━━━━━━━━━━━

“This is just a world in a game then, 
this institution is probably not even real,” you say.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

We assure you, this institution is very real.
And very expensive.
You are here on a scholarship.
Not to mention your life depends on it
━━━━━━━━━━━━━━━━━━━━━━
'''
act2_reality_check2 = '''

Another window slides open before you can protest.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

PLAYER STATUS:
Origin: Commoner
Year: Final Year
Magic Type: Healing (Recently Awakened)
Social Standing: Questionable
━━━━━━━━━━━━━━━━━━━━━━
'''
act2_reflection1 = '''

You glance down at your hands.

They look normal.
Too normal, considering you were supposed to be dying moments ago.
Your reflection catches in the polished stone nearby.
'''
act2_reflection2 = '''

Curly red hair, slightly wild, like it refuses to behave no matter 
how much effort you put in. Forest-green eyes—alert, sharp, 
and very aware of how out of place you are. Your uniform fits properly, 
tailored neatly, but the fabric is plain compared to 
the ornate designs worn by students passing through the gates.

You look… ordinary.

And yet, people glance at you anyway.
'''
act2_identity_reminder = '''

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Ah—before you ask.
Yes, you are still the same person.
Thirty years lived.
Zero successful romances.
Plenty of emotional baggage.
However, in the body of a commoner {name}
━━━━━━━━━━━━━━━━━━━━━━
'''
act2_confirmation = '''

Your chest tightens.
“So this really is my life now,” you whisper.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Correct.
And whether it continues—
depends entirely on you.
━━━━━━━━━━━━━━━━━━━━━━
'''
act2_tutorial_intro1 = '''

Before you can demand answers, the gates creak open.
Students stream past you.

Nobles.
Royals.
People who move like they belong here.

You don’t.
Whispers trail behind you as you step forward.

“A commoner?”
“They let someone like that in?”
“How embarrassing…”

'''
act2_tutorial_intro2 = '''

Your grip tightens at your side.
Someone slams into your shoulder.
Hard.
You stumble back, barely keeping your footing.

A noble student turns, scoffing openly.

“Watch where you’re going,” they sneer. 
“This academy isn’t meant for people like you.”

The surrounding students slow, 
pretending not to stare while very clearly staring.

A faint shimmer appears at the edge of your vision.

'''
act2_tutorial_intro3 = '''

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

TUTORIAL SCENARIO INITIATED.
This scenario will demonstrate how 
your actions influence your future.
No permanent negative consequences will occur. 
(This time.)
━━━━━━━━━━━━━━━━━━━━━━
'''
act2_player_notice = '''
You glance around
From the corner of your eye, 
you notice three people who look… wrong.

Not dangerous.
Not hostile.
Important.
Your breath catches.
You’ve seen them before.

Not here—
but on a glowing screen, late at night, 
half-asleep, tapping dialogue options and wondering 
why fictional men had better communication skills than real ones.

You remember them from the otome game you saw in the real world—
the one that flashed through your mind right before the truck hit.
'''
act2_characters1 = '''

— A young man stands on the academy steps in royal colors, 
gold embroidery catching the light and a crest pinned to his chest. 
His silver-blond hair is tied back loosely, and his crimson eyes sparkle 
with amusement, as if he already knows exactly what you’re going to do.

— Another figure leans casually against a marble pillar, arms crossed. 
His dark obsidian hair is neatly styled, framing icy blue eyes that 
assess you with unsettling precision. Everything about him speaks of 
restraint: a perfectly tailored noble uniform, immaculate posture, 
and an expression that reveals nothing beyond quiet judgment. 
He isn’t watching out of curiosity—he’s measuring your worth.

'''
act2_characters2 = '''

— And then there’s the third.
At first, you can’t see him at all.
The air ripples. Light bends where it shouldn’t.
You feel his presence more than you see it—tall, composed, 
draped in dark fabrics that seem to absorb illumination. 
When his gray gaze briefly finds you, a chill runs down your spine, 
followed by the unsettling realization that he finds this entire situation… 
ENTERTAINING
Your heart slams against your ribs.

“…Oh my god,” you whisper.

Your mind races.

“Are those—”
You swallow.
“—the future Crown Prince, the future Grand Duke, 
and the Magic Tower Master heir? Wasn't he also an assassin?!”

A familiar window pops into existence.
'''
act2_assign_lp = '''

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Correct.
Primary Routes Confirmed.

• Crown Heir
 Alexander Aurelion 
• Grand Duke Heir
Serene Valemont 
• Magic Tower Master/ Assassin
Theron Ravenhart 

Affection values (love points) initialized.
• Crown Heir: 5
• Grand Duke Heir: 5
• Magic Tower Master/ Assassin: 5
━━━━━━━━━━━━━━━━━━━━━━
'''
act2_instruction1 = '''

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
They are now aware of you.
The three figures shift almost imperceptibly.

The Crown Prince’s smile deepens.
The Duke’s gaze sharpens.
The distortion tilts its head—interested.

Your response will affect how others perceive you.
Including them. 
Your heart pounds. 
You take a breath.
━━━━━━━━━━━━━━━━━━━━━━
'''
act2_instruction2 = '''

How do you respond to the noble who shoved you? 

1. Apologize calmly and step aside.
2. Meet their gaze and respond firmly.
3. Ignore them and walk past.
'''


# Functions and Classes ------------------------------------------------------
def print_story(text, player):
    print(text.format(name=player.name))
    utils.wait_for_continue(player)
    utils.clear()

def act_two_tutorial(player):
    utils.wait_for_continue(player)
    utils.clear()
    
    # Step through all story segments
    story_segments = [
        act2_intro,
        act2_transfer,
        act2_enrollment,
        act2_reality_check1,
        act2_reality_check2,
        act2_reflection1,
        act2_reflection2,
        act2_identity_reminder,
        act2_confirmation,
        act2_tutorial_intro1,
        act2_tutorial_intro2,
        act2_tutorial_intro3,
        act2_player_notice, 
        act2_characters1,
        act2_characters2,
        act2_assign_lp,
        act2_instruction1,
    ]
    for segment in story_segments:
        if '{name}' in segment:
            print_story(segment, player)
        else:
            print(segment)
            utils.wait_for_continue(player)  
            utils.clear()
    print(act2_instruction2)
    # Player choice
    while True:
        choice = input("\nEnter your choice (number): ")
        #utils.clear()
        if choice == '1':
            print('''
You lower your head slightly and step back.
"I’m sorry," you say evenly. "That was my fault."

The noble blinks, clearly expecting anger—or tears.
"Tch," they mutter, turning away.
A quiet murmur ripples through the crowd.

You sense approval. Not admiration—yet—but acknowledgment.
''')
            player.love_points["Crown Heir"] += 1
            player.love_points["Grand Duke Heir"] += 1
            break
        elif choice == '2':
            print('''
You straighten your posture and meet their gaze head-on.
"I was walking where I was allowed," you say. "Just like you."

The noble stiffens, face flushing.
The crowd goes silent.
Someone laughs softly from above.
Someone else narrows their eyes in interest.
''')
            player.love_points["Crown Heir"] += 2
            player.love_points["Magic Tower Master/ Assassin"] += 1
            break
        elif choice == '3':
            print('''
You don’t respond.

You simply walk past them, shoulders squared, gaze forward.

The noble splutters behind you, offended more by the lack 
of acknowledgment than anything else.
                  
The whispers return—different now.
''')
            player.love_points["Grand Duke Heir"] += 2
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")
    # End of tutorial summary
    utils.wait_for_continue(player)
    utils.clear()
    print(f'''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
          
Tutorial Complete.

Current Affection Levels:
• Crown Heir: {player.love_points["Crown Heir"]}
• Grand Duke Heir: {player.love_points["Grand Duke Heir"]}
• Magic Tower Master/ Assassin: {player.love_points["Magic Tower Master/ Assassin"]}
━━━━━━━━━━━━━━━━━━━━━━

You blink.
“…Those changed because of what I just did?”

''')

    utils.wait_for_continue(player)
    utils.clear()
    print('''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Correct
If you want to see these again type “rules”

Rules of the World:
1. Love Points determine survival.
2. If any Love Points reach zero, the player dies.
3. If player makes choices that displease a character, the player dies
4. Graduation from Academia Fortunae is mandatory.
5. If you fail to pass the challenges or college exam, player dies
6. Forming bonds unlocks endings.
7. Higher beings observe the player for entertainment purposes, 
   and may occasionally help!
━━━━━━━━━━━━━━━━━━━━━━
''')
    utils.wait_for_continue(player) 
    utils.clear()
    print('''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
The massive doors of Academia Fortunae loom ahead.
Welcome to your final year, Player.
Try not to die.
━━━━━━━━━━━━━━━━━━━━━━
''')

    return player.love_points


# Main -----------------------------------------------------------------------
