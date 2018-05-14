import adventure_game.my_utils as utils
from colorama import Fore, Style

# # # # #
# ROOM 4
#
# Serves as a good template for blank rooms
room5_description = '''
    . . .  
    You entered the cave. In the cave is a shark. There is a room to the SOUTH. You can either confront the shark or go 
    to the room.
    '''


def run_room(player_inventory, rooms_visited):
    # Let the user know what the room looks like
    print(Fore.BLUE + Style.BRIGHT + room5_description + Style.RESET_ALL)

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
            if go_where == 'south':
                next_room = 8
                done_with_room = True
            else:
                print(go_where, 'is not a valid direction')
                # END of WHILE LOOP
        elif the_command == 'confront':
            confront = '''
    The shark tells you of a top secret room to the NORTH that can take you to safety.
            '''
            print(Fore.BLUE + Style.BRIGHT + confront + Style.RESET_ALL)
            answer_shark = False
            while not answer_shark:
                trust_shark = input("Do you trust the shark and go to the secret room?")
                if trust_shark.lower() == 'yes':
                    next_room = 6
                    answer_shark = True
                elif trust_shark.lower() == 'no':
                    next_room = 8
                    answer_shark = True
                else:
                    print("Response not valid")
            done_with_room = True
        else:
            print('the command', the_command, 'has not been implemented')
    return next_room
