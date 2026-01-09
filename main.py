import act_one
import act_two
from player_class import Player

player = Player()

# ACT 1
act_one.starting_text()
player.name = act_one.tutorial_intro()

# ACT 2
act_two.act_two_tutorial(player)

player.display_info()
