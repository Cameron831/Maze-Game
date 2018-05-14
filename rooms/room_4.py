import adventure_game.my_utils as utils
import random
import time
from colorama import Fore, Style

# # # # #
# ROOM 4
#
# Serves as a good template for blank rooms
room4_description = '''
    . . .  
    You fall through a trap door into a cave. In the cave is a bear, you can either confront the bear or go EAST through
    the cave entrance.
    '''
room_inventory = {
    'armor': 1
}


def run_room(player_inventory, rooms_visited):
    # Let the user know what the room looks like
    print(Fore.BLUE + Style.BRIGHT + room4_description + Style.RESET_ALL)

    # valid commands for this room
    commands = ["go", "confront", "help"]
    no_args = ["help"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]

        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == 'east':
                next_room = 5
                done_with_room = True
            else:
                print(go_where, 'is not a valid direction')
                # END of WHILE LOOP
        elif the_command == 'confront':
            if utils.has_a(player_inventory, 'gun') == True:
                chance = random.randint(1, 10)
                if chance < 7:
                    print("You shoot and kill the bear. In the bear's nest is a suit of armor. You feel even more powerful")
                    utils.take_item(player_inventory, room_inventory, 'armor')
                    print("You head east")
                    time.sleep(2)
                    next_room = 5
                    done_with_room = True
                else:
                    print('You shoot at the bear, but miss. The bear rips your body into ribbons of flesh')
                    next_room = 0
                    done_with_room = True
            else:
                print("The bear is angry, it rips your body into ribbons of flesh")
                next_room = 0
                done_with_room = True
        else:
            print('the command', the_command, 'has not been implemented')
    return next_room
