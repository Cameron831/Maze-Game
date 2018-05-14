# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# prompt_question:
#   Ask a question of your user. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("Would you like cheese on your pizza?", ['yes', 'no'])
def prompt_question(prompt, valid_options):
    response = input(prompt)
    while not response.lower() in valid_options:
        print("Sorry, I did not understand your choice.")
        response = input(prompt)
    return response.lower()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ask_command:
#   Ask your user for a command. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("What do you want to do?", ['go', 'take', 'drop'])
def ask_command(prompt, valid_commands, no_arguments = ['status', 'help']):
    ask_again = True
    result = []
    while ask_again:
        # Get a response from the user and split the response into words
        response = input(prompt)
        words = response.split()

        # be safe against user accidents of just hitting the ENTER key
        if len(words) > 0:

            #check if the command is the list of valid commands
            if words[0].lower() not in valid_commands:
                print('\tSorry, I don\'t understand:"', response, '"')
                print('\t\t Your choices are:', valid_commands, "\n")
            else:
                #if the command is valid, but they forgot an argument, try again.
                if len(words) < 2:
                    # but check first if it was in the no argument list
                    if words[0].lower() not in no_arguments:
                        print('\tThe command: "', words[0], '" requires an argument.\n' )
                else:
                    # Otherwise we at least have two arguments! Now programmer gets to choose what to do.
                    ask_again = False
                    result = words
    # END WHILE LOOP

    #Return the command back to the user as a list (command will be index 0)
    # If the command was required then it will be in position 1
    return result

9