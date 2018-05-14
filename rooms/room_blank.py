import adventure_game.my_utils_old as utils

# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms
room3_description = '''
    . . .  3rd room ... 
    You are in a room that feels very familiar. To the NORTH there is a door
    that says exit.'''

def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room3_description)

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
            print("Now we need to process go for Room 3")
            done_with_room = True
            # END of WHILE LOOP
            # TODO return next room