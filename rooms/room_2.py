import adventure_game.my_utils as utils
from colorama import Fore, Style

#
#  ROOM 2
#

room_inventory = {
    'gun': 1
}

def run_room(player_inventory, rooms_visited):
    description = '''
    . . .
    You are in a brightly lit room. The room appears to be an office. There is a desk. There is a door to the SOUTH
    
'''
    #
    #
    # if room_inventory['key'] > 0:
    #     description = description + '\nYou notice a key on the desk'
    # else:
    #     description = description + '\nThe desk surface is empty'
    #
    print(Fore.BLUE + Style.BRIGHT + description + Style.RESET_ALL)


    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                next_room = 1
                done_with_room = True
            if direction == 'south':
                next_room = 4
                done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print(" There is no way to go,", direction)
        elif the_command == 'take':
            take_what = response[1]
            # What are they trying to take?
            if take_what == "gun":
                if utils.has_a(room_inventory, 'gun'):
                    utils.take_item(player_inventory, room_inventory, 'gun')
                    gun_prompt = "  In the desk is a gun. You feel powerful"
                    print(Fore.BLUE + Style.BRIGHT + gun_prompt + Style.RESET_ALL)
                else:
                    gun_taken = '   You already took the gun'
                    print(Fore.BLUE + Style.BRIGHT + gun_taken + Style.RESET_ALL)

            else:
                print("You can not take,", take_what)
    # end of main while loop
    return next_room