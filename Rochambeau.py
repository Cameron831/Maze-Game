import random
user_choices = {
    'R' : 'rock',
    'P' : 'paper',
    'S' : 'scissors',
    'Q' : 'quit'
}
computer_choices = ['rock', 'paper', 'scissors']
computer_wins = 0
user_wins = 0

def comp():
    random_num = random.randint(0,2)
    computer_choice = computer_choices[random_num]
    return computer_choice

def user():
    user_choice = input('Enter your choice, R = Rock, P = Paper, S = Scissors').upper()
    if user_choice not in user_choices:
        print('Invalid Response')
        return user()
    if user_choice in user_choices:
        return user_choices[user_choice]

# def main():
#     global computer_wins
#     global user_wins
#     comp_choice = comp()
#     print("The computer has made its choice. Now it is your turn!")
#     user_choice = user()
#     if user_choice == 'quit':
#         print('-= = = = = = = = = = = = = ==-')
#         print('Thanks for playing!')
#         print('Computer wins:', computer_wins)
#         print('User Wins:', user_wins)
#         if computer_wins > user_wins:
#             print('The COMPUTER is Superior! You Lose!')
#         if computer_wins < user_wins:
#             print('You are Superior! You win!')
#         if computer_wins == 0 and user_wins == 0:
#             print("Play again soon!")
#         if computer_wins == user_wins and computer_wins != 0:
#             print("It's a draw!")
#     if comp_choice == user_choice:
#         print('\tComputer chose', comp_choice, ', Draw! Go again!')
#         main()
#     if comp_choice == 'rock' and user_choice == 'scissors':
#         print('\tComputer chose', comp_choice, ', Bow to your superior overloard, LOSER!')
#         computer_wins = computer_wins + 1
#         main()
#     if comp_choice == 'rock' and user_choice == 'paper':
#         print('\tComputer chose', comp_choice, ', You win!')
#         user_wins = user_wins + 1
#         main()
#     if comp_choice == 'paper' and user_choice == 'rock':
#         print('\tComputer chose', comp_choice, ', Bow to your superior overloard, LOSER!')
#         computer_wins = computer_wins + 1
#         main()
#     if comp_choice == 'paper' and user_choice == 'scissors':
#         print('\tComputer chose', comp_choice, ', You win!')
#         user_wins = user_wins + 1
#         main()
#     if comp_choice == 'scissors' and user_choice == 'paper':
#         print('\tComputer chose', comp_choice, ', Bow to your superior overloard, LOSER!')
#         computer_wins = computer_wins + 1
#         main()
#     if comp_choice == 'scissors' and user_choice == 'rock':
#         print('\tComputer chose', comp_choice, ', You win!')
#         user_wins = user_wins + 1
#         main()
# main()

def user_dungeon():
    user_choice = input('Enter your choice, R = Rock, P = Paper, S = Scissors').upper()
    if user_choice not in user_choices:
        print('Invalid Response')
        return user()
    if user_choice in user_choices:
        return user_choices[user_choice]


def dungeon_main():
    computer_wins = 0
    user_wins = 0
    comp_choice = comp()
    print("The master has made his choice. Now it is your turn!")
    user_choice = user_dungeon()
    if comp_choice == user_choice:
        print('\tMaster chose', comp_choice, ', Draw! Go again!')
    if comp_choice == 'rock' and user_choice == 'scissors':
        print('\tMaster chose', comp_choice, ', Bow to your superior overlord, LOSER!')
        computer_wins = computer_wins + 1
    if comp_choice == 'rock' and user_choice == 'paper':
        print('\tMaster chose', comp_choice, ', You win!')
        user_wins = user_wins + 1
    if comp_choice == 'paper' and user_choice == 'rock':
        print('\tMaster chose', comp_choice, ', Bow to your superior overlord, LOSER!')
        computer_wins = computer_wins + 1
    if comp_choice == 'paper' and user_choice == 'scissors':
        print('\tMaster chose', comp_choice, ', You win!')
        user_wins = user_wins + 1
    if comp_choice == 'scissors' and user_choice == 'paper':
        print('\tMaster chose', comp_choice, ', Bow to your superior overlord, LOSER!')
        computer_wins = computer_wins + 1
    if comp_choice == 'scissors' and user_choice == 'rock':
        print('\tMaster chose', comp_choice, ', You win!')
        user_wins = user_wins + 1