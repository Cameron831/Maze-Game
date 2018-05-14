import adventure_game.my_utils as utils
from colorama import Fore, Style

# # # # #
# ROOM 9
#
# Serves as a good template for blank rooms
room9_description = '''
    You walk through the door, falling into a pit of fresh punji sticks. Your screams drown in the screams of the other 
    dying adventurers. A long and gruesome death awaits'''

def run_room(player_inventory, rooms_visited):
    # Let the user know what the room looks like
    print(Fore.BLUE + Style.BRIGHT + room9_description + Style.RESET_ALL)
    next_room = 0
    return next_room