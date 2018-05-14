import adventure_game.my_utils as utils
from colorama import Fore, Style

# # # # #
# ROOM 10
#
# Serves as a good template for blank rooms
room_description = '''
    There is a door to the north, in the room is nothing but a sign with "Don't go north" written in blood.'''
room_description_visited = '''
    The sign now says "Now you've wasted your time." There is a door to the south and the north
'''

def run_room(player_inventory, rooms_visited):
    room_visited = utils.room_visited_check(rooms_visited, 10)
    if room_visited == True:
        print(Fore.BLUE + Style.BRIGHT + room_description_visited + Style.RESET_ALL)
    else:
        print(Fore.BLUE + Style.BRIGHT + room_description + Style.RESET_ALL)
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
        response = utils.ask_command("Which direction do you want to go?", commands, no_args)
        the_command = response[0]
        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == 'north':
                next_room = 11
                done_with_room = True
            if go_where == 'south':
                next_room = 6
                done_with_room = True
            else:
                print(go_where, 'is not a valid direction')
                # END of WHILE LOOP
        else:
            print('the command', the_command, 'has not been implemented')
    return next_room