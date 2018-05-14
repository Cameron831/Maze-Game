import adventure_game.my_utils as utils
from colorama import Fore, Style


# # # # # # # # # # # # # # #
#  This is the main room you will start in.
#   ROOM 1
#
#
description = '''
    . . . Main Room . . .
    You open your eyes. The room you see is unfamiliar. You see a brightly lit
    doorway to the SOUTH. To the EAST you see a closed door. 
    
'''

description_visited = '''
    You arrive back in the starting room. You see a brightly lit
    doorway to the SOUTH. To the EAST you see a closed door. 
    
'''
def run_room(player_inventory, rooms_visited):
    room_visited = utils.room_visited_check(rooms_visited, 1)
    if room_visited == True:
        print(Fore.BLUE + Style.BRIGHT + description_visited + Style.RESET_ALL)
    else:
        print(Fore.BLUE + Style.BRIGHT + description + Style.RESET_ALL)
    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help", "dev"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'dev':
            next_room = int(response[1])
            done_with_room = True
        elif the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'south':
                next_room = 2
                done_with_room = True
            elif direction == 'east':
                next_room = 3
                done_with_room = True
                print("You open the door to the east.")
            elif direction == 'west' and utils.room_visited_check(rooms_visited, 1):
                next_room = 6
                done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            print("There is nothing to take here.")
        elif the_command == 'drop':
            drop_what = response[1]
            if drop_what in inventory.keys():
                del inventory[drop_what]
                print("You no longer possess,", drop_what)

    # end of while loop
    return next_room


