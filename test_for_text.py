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
part_three = '''fvb'''



def starting_text():
    print("To get to the next dialouge click enter")
    print(f"\n {part_one}")
    skip = input("")
    if skip == '':
        utils.clear()
        print(part_two)
        skip_count += 1
    if skip_count == 1 and skip == '':
        print(part_three)

    
starting_text()