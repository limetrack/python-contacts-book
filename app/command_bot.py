from utils.error_handlers import input_error
from utils.prompt_handlers import is_yes_prompt
from constants.messages import error_messages
from app.AddressBook import AddressBook
from utils.commands import handle_command

@input_error(error_messages["no_command"])
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error(error_messages["no_command"])
def address_book_bot():
    contacts = AddressBook()

    print("Welcome to the assistant bot!") # TODO change msg
    
    handle_command('help', None, contacts) # TODO if need to show help before start bot, simply remove it
    
    while True:
        user_input = input("Enter a command: ") # TODO change msg
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!") # TODO change msg
            break
        else:
            handle_command(command, args, contacts)

