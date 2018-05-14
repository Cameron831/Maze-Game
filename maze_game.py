import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+"/./../")
from my_utils import make_visited
from colorama import Fore, Style

# room imports
import adventure_game.rooms.room_1 as r1
import adventure_game.rooms.room_2 as r2
import adventure_game.rooms.room_3 as r3
import adventure_game.rooms.room_4 as r4
import adventure_game.rooms.room_5 as r5
import adventure_game.rooms.room_6 as r6
import adventure_game.rooms.room_7 as r7
import adventure_game.rooms.room_8 as r8
import adventure_game.rooms.room_9 as r9
import adventure_game.rooms.room_10 as r10
import adventure_game.rooms.room_11 as r11
import adventure_game.rooms.room_12 as r12
# Default the player to the first room
room_number = 1

# Player Inventory
player_inventory = {
    'torch': 1
}
rooms_visited = []

print("Welcome to the maze game...\n")



should_continue = True
while should_continue:
    if room_number == 0:
        print(Fore.RED + Style.BRIGHT + "\tGame Over, you lost" + Style.RESET_ALL)
        break
    elif room_number == 1:
        room_number = r1.run_room(player_inventory, rooms_visited)
        make_visited(rooms_visited, 1)
    elif room_number == 2:
        room_number = r2.run_room(player_inventory, rooms_visited)
        make_visited(rooms_visited, 2)
    elif room_number == 3:
        room_number = r3.run_room(player_inventory, rooms_visited)
        make_visited(rooms_visited, 3)
    elif room_number == 4:
        room_number = r4.run_room(player_inventory, rooms_visited)
        make_visited(rooms_visited, 4)
    elif room_number == 5:
        room_number = r5.run_room(player_inventory, rooms_visited)
        make_visited(rooms_visited, 5)
    elif room_number == 6:
        room_number = r6.run_room(player_inventory, rooms_visited)
        make_visited(rooms_visited, 6)
    elif room_number == 7:
        room_number = r7.run_room(player_inventory, rooms_visited)
        make_visited(rooms_visited, 7)
    elif room_number == 8:
        room_number = r8.run_room(player_inventory, rooms_visited)
        make_visited(rooms_visited, 8)
    elif room_number == 9:
        room_number = r9.run_room(player_inventory, rooms_visited)
        make_visited(rooms_visited, 9)
    elif room_number == 10:
        room_number = r10.run_room(player_inventory, rooms_visited)
        make_visited(rooms_visited, 10)
    elif room_number == 11:
        room_number = r11.run_room(player_inventory, rooms_visited)
        make_visited(rooms_visited, 11)
    elif room_number == 12:
        room_number = r12.run_room(player_inventory, rooms_visited)
        make_visited(rooms_visited, 12)
    elif room_number == 'win':
        print(Fore.YELLOW + Style.BRIGHT + '\tCongratulations you made it to safety!', '\n\t\t Game Over, You Won!' + Style.RESET_ALL)
        break
    else:
        print("Ack I don't know room number:", room_number)
        break