from app.command_handlers import *

def bot_help(args, book):
    print("\nAvailable commands:")
    print("|{:_^15}|{:_^45}|{:_^60}|".format("Command", "Example with arguments", "Description"))
    for command, info in command_info.items():
        description = info['description']
        example = info['example']
        print("|{:<15}|{:<45}|{:<60}|".format(command, (' ' if example is None else f'example: {example}'), description))
    print("\n")

command_info = {
    'help': {
        'function': bot_help,
        'example': None,
        'description': 'Shows a list of available commands with descriptions.',
    },
    'hello': {
        'function': bot_hello,
        'example': None,
        'description': 'Greets the user.',
    },
    'exit, close': {
        'function': None,  # No function associated with exit, it will be handled separately
        'example': None,
        'description': 'Exits the program.',
    },
    'all': {
        'function': show_all,
        'example': None,
        'description': 'Show all contacts, ordered by name',
    },
    'add-contact': {
        'function': add_contact,
        'example': "add-contact 'John Doe' '123-456-7890' '01-01-1990' 'john@example.com' '123 Main St'",
        'description': 'Add a new contact with name, phone, birthday, email, and address.',
    },
    'find': {
        'function': find_contact,
        'example': "find-contact 'John'",
        'description': 'Find contacts by various criteria such as name, phone, email, address, or birthday.',
    },
    'add-phone': {
        'function': add_phone,
        'example': "add-phone 'John Doe' '987-654-3210'",
        'description': 'Update the phone number for an existing contact.',
    },
    'show-phone': {
        'function': show_phones,
        'example': "show-phone 'name'",
        'description': 'Show phone for contact by name',
    },
    'add-birthday': {
        'function': add_birthday,
        'example': "add-birthday 'John Doe' '01-01-1990'",
        'description': 'Update the birthday for an existing contact.',
    },
    'show-birthday': {
        'function': show_birthday,
        'example': "show-birthday 'John Doe'",
        'description': 'Show the birthday of a specific contact.',
    },
    'show-birthdays': {
        'function': show_birthdays,
        'example': "show-birthdays",
        'description': 'Show names and birthdays of all contacts.',
    },
    'find-birthdays': {
        'function': find_birthdays,
        'example': "find-birthdays 5",
        'description': 'Find contacts whose birthdays occur in a specified number of days.',
    },
    'update-contact': {
        'function': update_contact,
        'example': "update-contact 'John Doe' '123-456-7890' '01-01-1990' 'john@example.com' '123 Main St'",
        'description': 'Update the details of an existing contact.',
    },
    'delete-contact': {
        'function': delete_contact,
        'example': "delete-contact 'John Doe'",
        'description': 'Delete a contact by name.',
    },
    'add-note': {
        'function': add_note,
        'example': "add-note 'John Doe' 'Meeting at 5 PM'",
        'description': 'Add a note to a specific contact.',
    },
    'edit-note': {
        'function': add_note,
        'example': "edit-note 'John Doe' 0 'Updated meeting at 6 PM'",
        'description': 'Edit a specific note of a contact.',
    },
}

def handle_command(command, args, book):
    if command in command_info:
        command_function = command_info[command]['function']
        if command_function:
            return command_function(args, book)
        else:
            return print("Invalid command. Use 'help' command for Help!")
    else:
        return print("Invalid command. Use 'help' command for Help!")
