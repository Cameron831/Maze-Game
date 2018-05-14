import adventure_game.my_utils as utils
from colorama import Fore, Style

# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms
room3_description = '''
    . . . 
    You are in a room that feels very familiar. To the NORTH there is a door
    that says exit.'''


def run_room(player_inventory, rooms_visited):
    # Let the user know what the room looks like
    print(Fore.BLUE + Style.BRIGHT + room3_description + Style.RESET_ALL)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

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
            if go_where == 'west':
                next_room = 1
                done_with_room = True
            if go_where == 'north':
                if utils.has_a(player_inventory, 'key') == True:
                    next_room = 'win'
                    done_with_room = True
                else:
                    print('The door is locked')
            else:
                print(go_where, 'is not a valid direction')
                # END of WHILE LOOP
        else:
            print('the command', the_command, 'has not been implemented')
    return next_room
