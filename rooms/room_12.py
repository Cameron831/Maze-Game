import adventure_game.my_utils as utils
import random
import time
from colorama import Fore, Style


# # # # #
# ROOM 11
#
# Serves as a good template for blank rooms
room12_description = '''
    The room is a trap. There are 8 doors and only one of them will take you back to the last room. After every guess 
    the room rotates and the doors scramble. 
    '''
def run_room(player_inventory, rooms_visited):
    # Let the user know what the room looks like
    print(Fore.BLUE + Style.BRIGHT + room12_description + Style.RESET_ALL)
    # valid commands for this room
    # nonsense room number,
    next_room = -1
    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = input("Choose a door 1-8")
        # now deal with the command
        correct_door = random.randint(1, 8)
        try:
            response = int(response)
            if response > 8:
                print('Not a valid number')
        except:
            print('Not a valid input')
        if response == correct_door:
            print("You guessed correctly, you may go back to the last room")
            next_room = 11
            done_with_room = True
            time.sleep(1)
        else:
            print('Incorrect guess, try again')
    return next_room