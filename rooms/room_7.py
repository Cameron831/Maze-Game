import adventure_game.my_utils as utils
import adventure_game.Rochambeau as r
from colorama import Fore, Style
import time

# # # # #
# ROOM 7
#
# Serves as a good template for blank rooms
room7_description = '''
    . . .  
    You enter the room and see an old japanese man sitting in th middle of the room. He is the world rochambeau champion.
    If you want to make it out of the room you must beat him in a best of 5 match
    '''

room_description_intimidated = '''
    ...
    You enter the room and see an old japanese man sitting in th middle of the room. He is the world rochambeau champion.
    Your armor and gun intimidate him, he offers you a key and tells you to to head east to go to safety in exchange for
    his life.
'''

room_inventory = {
    'key' : 1
}

def run_room(player_inventory, rooms_visited):
    # Let the user know what the room looks like
    if utils.has_a(player_inventory, 'gun') and utils.has_a(player_inventory, 'armor'):
        print(Fore.BLUE + Style.BRIGHT + room_description_intimidated + Style.RESET_ALL)
    else:
        print(Fore.BLUE + Style.BRIGHT + room7_description + Style.RESET_ALL)

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
        computer_wins = 0
        user_wins = 0
        games = 0
        r_done = False
        while r_done == False:
            comp_choice = r.comp()
            print(Fore.BLUE + Style.BRIGHT + "The master has made his choice. Now it is your turn!" + Style.RESET_ALL)
            user_choice = r.user_dungeon()
            if comp_choice == user_choice:
                print(Fore.RED + Style.BRIGHT + '\tMaster chose', comp_choice, ', Draw! Go again!' + Style.RESET_ALL)
            if comp_choice == 'rock' and user_choice == 'scissors':
                print(Fore.RED + Style.BRIGHT + '\tMaster chose', comp_choice, ', Bow to your superior overlord, LOSER!' + Style.RESET_ALL)
                computer_wins = computer_wins + 1
                games += 1
            if comp_choice == 'rock' and user_choice == 'paper':
                print(Fore.RED + Style.BRIGHT + '\tMaster chose', comp_choice, ', You win!' + Style.RESET_ALL)
                user_wins = user_wins + 1
                games += 1
            if comp_choice == 'paper' and user_choice == 'rock':
                print(Fore.RED + Style.BRIGHT + '\tMaster chose', comp_choice, ', Bow to your superior overlord, LOSER!' + Style.RESET_ALL)
                computer_wins = computer_wins + 1
                games += 1
            if comp_choice == 'paper' and user_choice == 'scissors':
                print(Fore.RED + Style.BRIGHT + '\tMaster chose', comp_choice, ', You win!' + Style.RESET_ALL)
                user_wins = user_wins + 1
                games += 1
            if comp_choice == 'scissors' and user_choice == 'paper':
                print(Fore.RED + Style.BRIGHT + '\tMaster chose', comp_choice, ', Bow to your superior overlord, LOSER!' + Style.RESET_ALL)
                computer_wins = computer_wins + 1
                games += 1
            if comp_choice == 'scissors' and user_choice == 'rock':
                print(Fore.RED + Style.BRIGHT + '\tMaster chose', comp_choice, ', You win!' + Style.RESET_ALL)
                user_wins = user_wins + 1
                games += 1
            if games == 5:
                r_done = True
        if user_wins == 3:
            print(Fore.BLUE + Style.BRIGHT + 'You defeated the master, he gives you a key' + Style.RESET_ALL)
            utils.take_item(player_inventory, room_inventory, 'key')
            print(Fore.BLUE + Style.BRIGHT + 'You head back to the last room' + Style.RESET_ALL)
            time.sleep(2)
            next_room = 6
            done_with_room = True
        if user_wins < 3:
            print(Fore.BLUE + Style.BRIGHT + 'The master defeated you, you are now his slave forever' + Style.RESET_ALL)
            next_room = 0
            done_with_room = True
    return next_room