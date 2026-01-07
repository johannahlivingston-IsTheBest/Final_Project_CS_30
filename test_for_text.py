import utils


part_one = '''You were reading an otome game synopsis on your phone.

Ooooh a new version of my favorite otome game!
I should check it out when I get home
A fantasy academy.
Love points.
Multiple endings.

You are lost in thought when you step off the curb.
You never saw the truck.'''

#[SCREEN FADES TO BLACK]

part_two = '''AT THE HOSPITAL: “Congratulations! You’re Dying.”

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

Before you can process anything, a translucent window snaps open in front of your face.

'''
part_three = '''
━━━━━━━━━━━━━━━━━━━━━━
WELCOME, PLAYER!

Current Location:
Hospital — Emergency Ward
Status:
CRITICALLY INJURED

━━━━━━━━━━━━━━━━━━━━━━
You blink.

“…Okay,” you say weakly. “This is either a dream or I’m concussed.”

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
first_choices = ['1. What is happening right now?','2. “Beings of higher power…?”']
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
You were hit by a truck, your body is failing, and you have caught the attention of some very bored entities called beings of higher power.

They have decided that if you manage to survive a game, you can survive the truck accident
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
Hence they have decided that if you manage to survive a game, you can survive the truck accident
━━━━━━━━━━━━━━━━━━━━━━
'''
part_four = '''
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
━━━━━━━━━━━━━━━━━━━━━━
'''
part_five = '''
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

def starting_text():
    print("To get to the next dialouge click enter")
    skip_count = 0
    skip = input("")
    if skip == '' and skip_count == 0:
        utils.clear()
        print(part_one)
    skip_count += 1
    skip = input("")
    if skip == '' and skip_count == 1:
        utils.clear()
        print(part_two)
    skip_count += 1
    skip = input("")
    if skip_count == 2 and skip == '':
        utils.clear()
        print(part_three)
    skip_count += 1
    skip = input("")
    if skip_count == 3 and skip == '':
        utils.clear()
        print(part_four)
    skip_count += 1
    skip = input("")
    if skip_count == 4 and skip == '':
        utils.clear()
        print("How would you like to respond?")
        print(first_choices)
        user_option = input("Enter your choice: ")
        if user_option == '1':
            print('\n you picked option 1')
            print(f"\n{reaction_one}")
        elif user_option == '2':
            print('\n you picked option 2')
    skip_count += 1
    skip = input("")
    if skip_count == 5 and skip == '':
        utils.clear()
        print(part_four)
    skip_count += 1
    skip = input("")
    if skip_count == 6 and skip == '':
        utils.clear()
        print(part_five)

starting_text()