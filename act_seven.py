##############################################################################
# Title: Act Seven
# Date: 1/7/2026
##############################################################################
"""this contains all dialouge and options for act seven"""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import utils
import puzzles
from world import game_loop
# put text varibles and list for options here


# SCENE: AFTERMATH — “YOU FORGOT SOMETHING”
act8_aftermath_intro = '''
CHAPTER 8 - Final Challenge: Academia Fortunae 
"The System Demands a Diploma"

You return to the academy battered, singed, and very much alive.

The forest fades behind you.
The dragon is gone.
Sir Valemont is alive.
You are—miraculously—not dragon food.

Students whisper louder now.
Faculty watches you with concern.
Someone actually bows.

You limp into your dorm, 
collapse onto your bed, 
and let out a long breath.

“…I survived,” you mumble.
“Again.”

For the first time in weeks, 
nothing immediately tries to kill you.
The silence feels… wrong.
Then—
A translucent window snaps open above your face.
'''
act8_aftermath_intro2 = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Oops.
━━━━━━━━━━━━━━━━━━━━━━

You squint at it.
“…Oops?”

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

We may have forgotten to 
remind you of something.

Very minor.
Very small.
Practically insignificant.
━━━━━━━━━━━━━━━━━━━━━━
'''
act8_aftermath_intro3 = '''
Your stomach drops.
“What,” you ask slowly, “did you forget?”

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Your final exam.
━━━━━━━━━━━━━━━━━━━━━━

You sit straight up.
“…My what.”

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

You are, technically, a student.
At an academy.
With a graduation requirement.
Strange how nearly dying multiple times 
makes one forget academic responsibilities.
━━━━━━━━━━━━━━━━━━━━━━
'''
act8_aftermath_intro4 = '''
“You let me fight a dragon,” you hiss.
“And NOW you remember school?!”

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

In our defense,
You were very entertaining.
━━━━━━━━━━━━━━━━━━━━━━

A pause.
'''
act8_aftermath_intro5 = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Final Challenge Unlocked.
Objective: Graduate from Academia Fortunae.
Failure Consequence: Death.
Naturally.
━━━━━━━━━━━━━━━━━━━━━━

You stare at the ceiling.
“…Of course.”
'''
# TIME SKIP — ONE WEEK LATER
act8_final_exam_intro = '''TIME SKIP — ONE WEEK LATER

The week crawls by.
Cramming.
Whispers.
Stolen glances.

The Crown Prince finds excuses to sit near you.

The Duke watches you carefully now, 
pride wounded but respect earned.

The Magician remains distant—present, 
but unreadable.
'''
act8_final_exam_intro2 = '''
The Beings of Higher Power hum with anticipation.
On the seventh day—
The map appears again along with a system message.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Navigation Initialized.

Final Location: Final Exam Hall.
Attendance: Mandatory.
This is it, Player.
━━━━━━━━━━━━━━━━━━━━━━
'''
act8_final_exam_intro3 = '''
Your chest tightens.
“…This decides everything, doesn’t it?”

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Correct.
Head to the Main Building
for the exam!
━━━━━━━━━━━━━━━━━━━━━━

You step forward.
'''
# SCENE: FINAL EXAM HALL — “THE ENDING AWAITS”
act8_final_exam_hall = '''
The hall is vast.
Marble floors.
Floating sigils.
Ancient magic humming in the air.
Students sit in rows.

The faculty observes from above.
And at the far edges of the room—

The three men who changed everything.
The Crown Prince.
The Duke Heir.
The Magic Tower Master/Assassin.

They are watching you.
'''
act8_final_exam_hall2 = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Final Evaluation Commencing.

Criteria:
 • Intelligence
 • Resolve
 • Emotional growth
 • Survival Instincts
 • Love Points Accumulated

Pass to graduate.
Fail to perish.
━━━━━━━━━━━━━━━━━━━━━━

You swallow.
“…No pressure.”
The exam begins.

[add exam game match des here]
'''
# FINAL EXAM FAIL
act8_final_exam_fail = '''
━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Final Evaluation Complete.

Result: FAILED.

Knowledge: Insufficient.
Emotional Awareness: Questionable.
Survival Probability: Unacceptable.
━━━━━━━━━━━━━━━━━━━━━━

The sigils above you flicker—then shatter.

The room goes cold.
Students vanish.
Faculty turns away.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

You were entertaining.
But not enough.

Thank you for playing.
━━━━━━━━━━━━━━━━━━━━━━
'''
# FINAL EXAM PASS
act8_final_exam_pass = '''
— YOU PASS —

The sigils flare.
Then fade.
Silence.
Then—

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Congratulations, Player.
You have passed the final exam.
Academia Fortunae Graduate Status: CONFIRMED.
━━━━━━━━━━━━━━━━━━━━━━
'''
act8_final_exam_pass2 = '''
Applause erupts.
Faculty nods in approval.
The Beings of Higher Power cheer shamelessly.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Current Love Points Summary:
(Highest Affection Will Determine Ending)
━━━━━━━━━━━━━━━━━━━━━━
'''
act8_final_exam_pass3 = '''
The system pauses.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

However—
As a special reward, 
you may choose.
━━━━━━━━━━━━━━━━━━━━━━
'''
act8_endings = '''
FINAL PLAYER CHOICE
1. Accept your highest Love Point ending.
2. Accept the Elixir of Life and return to your original world.
'''
# ALL LOVE-POINT ENDINGS
act8_end_crown_prince = '''
CROWN PRINCE ENDING
“QUEEN OF THE REALM”

The exam hall dissolves into light.
When your vision clears, 
you’re standing on a balcony
overlooking the capital—golden spires, 
banners fluttering, 
the sound of the city breathing beneath you.

A familiar presence stands beside you.
Alexander Aurelion.
He turns, crimson eyes soft instead of calculating.
'''
act8_end_crown_prince2 = '''
━━━━━━━━━━━━━━━━━━━━━━
ALEX:
“So… you really did it.”
━━━━━━━━━━━━━━━━━━━━━━

You laugh weakly.
“I think I blacked out halfway through.”
He steps closer, removing his gloves.
'''
act8_end_crown_prince3 = '''
━━━━━━━━━━━━━━━━━━━━━━
ALEX:
“You faced assassins, dragons, 
and divine nonsense.”
A pause.
“…An exam was never going to stop you.”
━━━━━━━━━━━━━━━━━━━━━━

He hesitates—then kneels.
The world stops.
'''
act8_end_crown_prince4 = '''
━━━━━━━━━━━━━━━━━━━━━━
ALEX:
“I was born into duty.”

“I was taught love was a weakness.”
His gaze lifts to yours.

“And then you survived everything 
I couldn’t protect you from.”
━━━━━━━━━━━━━━━━━━━━━━

A small smile.
'''
act8_end_crown_prince5 = '''
━━━━━━━━━━━━━━━━━━━━━━
ALEX:
“Rule with me.”
━━━━━━━━━━━━━━━━━━━━━━

Your answer doesn’t need words.
When he kisses you, it’s not royal.
It’s real.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Ending Unlocked: Queen of the Realm
Status: Married
Survival: Permanent
━━━━━━━━━━━━━━━━━━━━━━
'''
act8_end_Duke = '''
DUKE ENDING
“DUCHESS OF STEEL”

The exam hall empties.
Rain falls outside the academy walls.

You find him waiting beneath an 
old oak—armor half-removed, posture stiff.

Sir Valemont or as you have come to call him,
Ren.

He doesn’t look at you at first.
'''
act8_end_Duke2 = '''
━━━━━━━━━━━━━━━━━━━━━━
DUKE:
“…I was wrong about you.”
━━━━━━━━━━━━━━━━━━━━━━

You raise a brow.
“That’s your big confession?”
A huff of laughter escapes him—short, surprised.
'''
act8_end_Duke3 = '''
━━━━━━━━━━━━━━━━━━━━━━
DUKE:
“I thought you were a threat.”
“Then you became a liability.”
He finally meets your eyes.
“…Then you saved my life.”
━━━━━━━━━━━━━━━━━━━━━━

He steps closer.
'''
act8_end_Duke4 = '''
━━━━━━━━━━━━━━━━━━━━━━
DUKE:
“I don’t know how to be gentle.”
“But I will be loyal. To the end.”
━━━━━━━━━━━━━━━━━━━━━━

You reach out first.
The kiss is fierce. Certain. Earned.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Ending Unlocked: Duchess of Steel
Status: Married
Survival: Permanent
━━━━━━━━━━━━━━━━━━━━━━
'''
act8_end_tower_master = '''
MAGIC TOWER MASTER/ ASSASSIN ENDING
“SHADOW AND FLAME”

No throne.
No audience.

Just the two of you standing at the edge of 
the Magic Tower as dawn breaks.
Theron doesn’t face you.
'''
act8_end_tower_master2 = '''
━━━━━━━━━━━━━━━━━━━━━━
THERON:
“You could have chosen safety.”
━━━━━━━━━━━━━━━━━━━━━━

You shrug.
“I got bored.”
A quiet breath—almost a laugh.

━━━━━━━━━━━━━━━━━━━━━━
THERON:
“I have killed for less interesting reasons.”
━━━━━━━━━━━━━━━━━━━━━━

He turns.
For once, his eyes aren’t guarded.
'''
act8_end_tower_master3 = '''
━━━━━━━━━━━━━━━━━━━━━━
THERON:
“I don’t know how to live quietly.”
“…But I want to try. With you.”
━━━━━━━━━━━━━━━━━━━━━━

You pull him into a kiss before he can retreat.
He freezes—
Then melts.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

Ending Unlocked: Shadow and Flame
Status: Married/ Partners
Lifestyle: Dangerously Profitable
━━━━━━━━━━━━━━━━━━━━━━
'''
# REAL WORLD ENDING
act8_end_return_real_world = '''
RETURN ENDING
“AWAKE”

Light floods everything.

Pain.
Then warmth.

You wake to sobbing.
Your mother’s hand grips yours 
like she’s afraid you’ll vanish.

Your father’s voice cracks.
Your sister laughs through tears.
'''
act8_end_return_real_world2 = '''
━━━━━━━━━━━━━━━━━━━━━━
MOTHER:
“She’s awake—she’s awake—”
━━━━━━━━━━━━━━━━━━━━━━

The machines beep steadily.

No system.
No map.
No love points.

Just life.

As your eyes close again—safe this time.
However, you swear you hear distant voices arguing.
'''
# POST-CREDITS SCENE
act8_post_credits = '''
POST-CREDITS SCENE
“THE BEINGS DEBRIEF”

A dark void.
Three glowing entities sit around a table.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

EXTRA CREDIT: SURVIVE
Edition 1: You Should’ve Been Worth More Love Points
Status: Complete
Would you like to play again?
━━━━━━━━━━━━━━━━━━━━━━
'''
act8_post_credits2 = '''
BEING #1:
“Well?”

BEING #2:
“She survived.”

BEING #3:
“…And flawlessly”

A pause.

BEING #1:
“Should we reset the world?”

Silence.

BEING #2:
“…No.”

BEING #3:
“She was fun.”
'''
act8_post_credits3 = '''
A new screen flickers to life.
The Beings smile.

━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:

EXTRA CREDIT: SURVIVE
Edition 2: ???
Status: ???
━━━━━━━━━━━━━━━━━━━━━━

Everything Fades to Black.
'''


puzzles = puzzles.Puzzles()

# Functions and Classes ------------------------------------------------------
def get_highest_love_interest(player):
    return max(player.love_points, key=player.love_points.get)

#winner = get_highest_love_interest(player)

def act_eight(player):

    # AFTERMATH SEQUENCE
    utils.print_story(act8_aftermath_intro, player)
    utils.print_story(act8_aftermath_intro2, player)
    utils.print_story(act8_aftermath_intro3, player)
    utils.print_story(act8_aftermath_intro4, player)
    utils.print_story(act8_aftermath_intro5, player)

    # TIME SKIP
    utils.print_story(act8_final_exam_intro, player)
    utils.print_story(act8_final_exam_intro2, player)
    utils.print_story(act8_final_exam_intro3, player)
    game_loop("main building")

    # FINAL EXAM HALL
    utils.print_story(act8_final_exam_hall, player)
    utils.print_story(act8_final_exam_hall2, player)

    # FINAL EXAM — MATCH GAME
    #score = puzzles.match_des()

    # FAIL CONDITION
    ##if score < 2:
     #   utils.clear()
     #   utils.print_story(act8_final_exam_fail, player)
     #   exit()

    # PASS CONDITION
    utils.clear()
    utils.print_story(act8_final_exam_pass, player)
    utils.print_story(act8_final_exam_pass2, player)

    # SHOW CURRENT LOVE POINTS
    print(f'''━━━━━━━━━━━━━━━━━━━━━━
SYSTEM MESSAGE:
          
Tutorial Complete.

Current Affection Levels:
• Crown Heir: {player.love_points["Crown Heir"]}
• Grand Duke Heir: {player.love_points["Grand Duke Heir"]}
• Magic Tower Master/ Assassin: {player.love_points["Magic Tower Master/ Assassin"]}
━━━━━━━━━━━━━━━━━━━━━━''')

    utils.print_story(act8_final_exam_pass3, player)
    utils.print_story(act8_endings, player)

    # PLAYER CHOICE
    choice = input("\nChoose 1 or 2: ")

    # RETURN TO REAL WORLD
    if choice == '2':
        utils.clear()
        utils.print_story(act8_end_return_real_world, player)
        utils.print_story(act8_end_return_real_world2, player)
        utils.print_story(act8_post_credits, player)
        utils.print_story(act8_post_credits2, player)
        exit()

    # LOVE POINT ENDING
    winner = get_highest_love_interest(player)
    player.stats['partner'] = winner

    utils.clear()

    if winner == "Crown Heir":
        utils.print_story(act8_end_crown_prince, player)
        utils.print_story(act8_end_crown_prince2, player)
        utils.print_story(act8_end_crown_prince3, player)
        utils.print_story(act8_end_crown_prince4, player)
        utils.print_story(act8_end_crown_prince5, player)

    elif winner == "Grand Duke Heir":
        utils.print_story(act8_end_Duke, player)
        utils.print_story(act8_end_Duke2, player)
        utils.print_story(act8_end_Duke3, player)
        utils.print_story(act8_end_Duke4, player)

    else:
        utils.print_story(act8_end_tower_master, player)
        utils.print_story(act8_end_tower_master2, player)
        utils.print_story(act8_end_tower_master3, player)

    utils.wait_for_continue(player)
    utils.clear()

    # POST-CREDITS
    utils.print_story(act8_post_credits, player)
    utils.print_story(act8_post_credits2, player)
    utils.print_story(act8_post_credits3, player)


if __name__ == "__main__":
    from player_class import Player
    test_player = Player()
    act_eight(test_player)
