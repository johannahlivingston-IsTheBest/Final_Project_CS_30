##############################################################################
# Title: Act Seven
# Date: 1/7/2026
##############################################################################
"""This contains all the dialogue and options for act seven."""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import utils
import puzzles
from world import game_loop

# put text varibles and list for options here
act7_intro = '''CHAPTER 7 - An unfortunate encounter: The Duke and The Dragon

You stand there for a moment longer than necessary…
then release a very long, very dramatic sigh.

You’re alive.
Still breathing.
Unburned.
Unstabbed.
Uncursed.

A win, frankly.

The library feels quieter around you now.
Not safer.
Just… less interested in killing you.

The academy, unfortunately, continues as normal.

Classes resume.
Assignments pile up.
Footsteps slow when you pass.

Whispers follow you.
Some people stare.
Some people very deliberately pretend you don’t exist.

You suspect rumors are spreading.
'''

act7_status_update = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Status Update:
Player has survived multiple 
statistically fatal encounters.

Social Response:
• Awe
• Fear
• Jealousy
• Mild resentment

Recommendation:
Lay low.
━━━━━━━━━━━━━━━━━━━━━━
'''

act7_silence = '''“Wow,” you mutter. 
“That’s the first good advice you’ve given me.”

The Beings of Higher Power do not respond.
Which is deeply suspicious.
'''

act7_silence_warning = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Silence detected.
Hence probability of impending chaos: High.
Have a pleasant day!
━━━━━━━━━━━━━━━━━━━━━━

"UGH"
…You hate it here.
'''

act7_relationships = '''You choose to ignore the system for now, 
enjoying the rare peace of not having 
the Beings of Higher Power make snarky remarks. 

To survive, you decide it’s best to remain invisible, 
pulling back and quietly assessing the state of your relationships.
'''

act7_relationships2 = '''RELATIONSHIP STATUS 

Crown Prince Alex
  Openly smitten
  Appears “casually” wherever you are
  Finds excuses to talk to you about nothing
  Is absolutely trying to win you over
You are one compliment away from being proposed to.
'''

act7_relationships3 = '''RELATIONSHIP STATUS 

Magician / Assassin Theron (Theo)
  Disappeared
  No messages
  No sightings
  No ominous lurking
You are unsure whether you passed a test…
Or are simply being watched from several rooftops away.
'''

act7_relationships4 = '''RELATIONSHIP STATUS 

Grand Duke Heir — Serene Valemont 
  Still holding a grudge over the dance
  Makes your academic life inconvenient
  Never crosses a line
His sharp looks linger longer than necessary.
And once—just once—you swear his gaze softened before he looked away.

You do speak.
 Briefly.
 Tensely.
 Like two people pretending nothing is wrong when everything is.
'''

act7_tension_notice = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Romantic Tension Detected.

Recommendation:
Proceed carefully.
Or dramatically.
Both options are acceptable.
━━━━━━━━━━━━━━━━━━━━━━
'''

act7_timeskip = '''You decide to lay low.
Focus on classes.
Keep your head down.
Avoid royal drama.
Ignore ominous systems.
It almost works.

TIME SKIP — ONE MONTH LATER
'''

act7_map_trigger = '''One month passes.
You survive it.
Mostly.

Lectures blur together.
Assignments pile up.

No assassination attempts. 
No cursed books. 
No magical emergencies.

You make the fatal mistake of thinking:
Maybe it’s calming down.
That’s when it happens.

A familiar translucent map snaps open in front of your vision.
It pulses.
Red.
Too red.
'''

act7_navigation = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Navigation Initialized.

New Event Detected.
Location: Forest
Mandatory Participation: Yes
Survival Probability: Unknown

Side note:
You really should have enjoyed the peace while it lasted.
━━━━━━━━━━━━━━━━━━━━━━
'''

act7_navigation2 = '''Before you can complain, the air shifts.
The silence breaks.
Not with words—but with presence.

You feel it.

A familiar pressure settles over your thoughts, 
heavy and intrusive, like an audience taking their seats.

The Beings of Higher Power are back.

Watching.
Hovering.
Far too pleased.

You stiffen.

“Where were you?” you mutter under your breath.
“And what was with the silence?”

The air hums faintly, amused.
“…And why,” you add, eyeing the pulsing map, 
“are you all suddenly so happy?”
'''

act7_navigation3 = '''For a moment, there is no response.
Then—

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Ah.
You noticed.

The previous silence was… intentional.
Narrative buildup is important.

As for our excitement—
It is directly related to your next destination.
━━━━━━━━━━━━━━━━━━━━━━

Your stomach drops.
“That’s not an answer,” you say flatly.
'''

act7_navigation4 = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Correct.
It is a warning.
━━━━━━━━━━━━━━━━━━━━━━

The whispers return, buzzing with anticipation.

Something is wrong.
Very wrong.

And whatever awaits you in the forest—
They are really looking forward to it.

The academy fades behind you.
One month of relative peace has done 
nothing to prepare you for this.

'''

act7_duke_intro = '''The forest air is thick.

Too warm.
Too still.

Leaves crunch beneath your boots as you push 
deeper between towering trees.

Then—
Steel flashes.
A familiar figure steps into view, sword already drawn.
Sir Serene Valemont (Duke Heir).
'''

act7_duke_intro2 = '''
━━━━━━━━━━━━━━━━━━━━━━
Serene Valemont:
“…Of course it’s you.”

He exhales sharply.

“I was ordered to investigate unusual 
magical readings.”
A pause.
“You shouldn’t be here.”

His gaze flicks over you—sharp, a
ssessing—then softens despite himself.

“…But I suppose it’s too late for that.”
━━━━━━━━━━━━━━━━━━━━━━
'''

act7_party_join = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

 Party Member Joined:
 • Grand Duke Heir — Sir Serene Valemont

Affection level:
 • Neutral (grudging)
━━━━━━━━━━━━━━━━━━━━━━
'''

act7_dragon_intro = '''Before you can respond—
The ground trembles.
Birds scatter.

The trees scream as something 
massive moves through them.

Heat slams into you like a wall.
From between the trees, 
scales gleam crimson and gold.

A DRAGON.
'''

act7_dragon_intro2 = '''Not sleeping.
Not ancient and sluggish.

Awake.
Hungry.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

WARNING.
Boss Encounter Detected.

Enemy: Forest Dragon
Combat Option:  Unavailable
Reason: You will die instantly.
━━━━━━━━━━━━━━━━━━━━━━
'''

act7_dragon_intro3 = '''Sir Valemont swears under his breath.
He steps in front of you without thinking, 
sword raised.

“Stay behind me.”

The dragon lowers its massive head, 
molten eyes locking onto the two of you.
Smoke curls from its nostrils.
Then—it speaks.

━━━━━━━━━━━━━━━━━━━━━━
DRAGON:
“Those who enter my forest must prove wisdom…
Or burn.”
The fire in its throat glows brighter.
━━━━━━━━━━━━━━━━━━━━━━
'''

act7_riddle_prompt = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Non-Combat Resolution Detected.
Initiating RIDDLE CHALLENGE.

Failure Result:
• Dragon incineration
• Sir Valemont dies
• You die shortly after

Success Reward:
• Dragon retreats
• Duke survives
• Affection Gain: +2
━━━━━━━━━━━━━━━━━━━━━━
'''

success_one = '''Your mind snaps into focus.
You step forward.
“It’s a sword, dragon, and a wizard,” you say clearly.
Silence.

Then—
The fire dims.

The dragon studies you for a long, heavy moment.
Finally, it huffs, smoke curling upward.
“Correct.”

With a thunderous beat of its wings, 
the creature retreats deeper into the forest, heat fading with it.
The ground stills.

You exhale shakily.
Sir Valemont lowers his sword.
Then looks at you.
Really looks.
'''

success_two = '''
━━━━━━━━━━━━━━━━━━━━━━
SIR VALENMONT:

“…You saved my life.”

A pause.
“…Thank you.”

His expression softens—just a little.
"And you can call me Ren <3 "
━━━━━━━━━━━━━━━━━━━━━━
'''

puzzles = puzzles.Puzzles()


# Functions and Classes ------------------------------------------------------
def act_seven(player):
    """Print act seven.

    Parameters:
        player (Player): the player object
    """
    utils.wait_for_continue(player)
    utils.clear()

    story_segments = [
        act7_intro,
        act7_status_update,
        act7_silence,
        act7_silence_warning,
        act7_relationships,
        act7_relationships2,
        act7_relationships3,
        act7_relationships4,
        act7_tension_notice,
        act7_timeskip,
        act7_map_trigger,
        act7_navigation,
        act7_navigation2,
        act7_navigation3,
        act7_navigation4,
        (game_loop, ("main building", "forest")),
        act7_duke_intro,
        act7_duke_intro2,
        act7_party_join,
        act7_dragon_intro,
        act7_dragon_intro2,
        act7_dragon_intro3,
        act7_riddle_prompt
    ]

    for segment in story_segments:
        try:
            segment[0](*segment[1])
        except TypeError:
            utils.print_story(segment, player)

    # RIDDLE
    correct_answers_count = puzzles.riddle()
    if correct_answers_count >= 2:
        utils.wait_for_continue(player)
        utils.clear()
        print(success_one)
        utils.wait_for_continue(player)
        utils.clear()
        print(success_two)

        player.love_points["Grand Duke Heir"] += 2
        utils.wait_for_continue(player)
        utils.clear()
        print(f'''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
              
 Affection Update:
 • Grand Duke Heir: +2
 • Crown Prince: No Change
 • Magician / Assassin: No Change
              
Threat Neutralized.
Survival Achieved.
━━━━━━━━━━━━━━━━━━━━━━
        ''')

        utils.wait_for_continue(player)
        utils.clear()

        print("""
You leave the forest alive.
Burned by tension.
Not by fire.
""")

    else:
        utils.wait_for_continue(player)
        utils.clear()
        print('''
The dragon’s eyes narrow.
“Wrong.”
Fire erupts.
              
Sir Valemont shoves you backward instinctively, 
blade flashing—
But it’s useless.
              
Flames consume the clearing.
''')
        utils.wait_for_continue(player)
        utils.clear()
        print('''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
              
Critical Failure.
              
Serene Valemont has fallen.
You follow moments later.
              
The Beings of Higher Power sigh.
“Such a promising run.”
              
GAME OVER.
You die.
━━━━━━━━━━━━━━━━━━━━━━
        ''')
        exit()


if __name__ == "__main__":
    from player_class import Player
    test_player = Player()
    act_seven(test_player)
