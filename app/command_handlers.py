from utils.error_handlers import input_error
from utils.prompt_handlers import is_yes_prompt
from constants.messages import error_messages
from app.AddressBook import AddressBook
from app.Fields import Note

def bot_hello(args, book:AddressBook):
    print("Hello,\nHow can I help you?")

def add_contact(args, book: AddressBook):
    if len(args) < 5:
        print("Not enough information. Please provide name, phone, birthday, email, and address.")
        return

    name, phone, birthday, email, address = args
    book.add_contact(name, phone, birthday, email, address)

def add_phone(args, book: AddressBook):
    if len(args) < 2:
        print("Not enough information. Please provide name and new phone number.")
        return

    name, phone = args
    book.update_phone(name, phone)

def show_phones(args, book: AddressBook):
    if len(args) < 1:
        print("Please provide a contact name.")
        return

    name = args[0]
    contact = book.data.get(name)

    if contact is None:
        print("Contact not found.")
        return

    phone = contact.phone.value if contact.phone else "No phone number"
    print(f"{name}'s phone number: {phone}")

    
def show_all(args, book: AddressBook):
    if not book.data:
        print("There are no contacts in your address book.")
        return

    header = "| {0:15} | {1:15} | {2:20} | {3:25} | {4:10} | {5:30} |".format(
        "Name", "Phone", "Email", "Address", "Birthday", "Note"
    )
    print(header)
    print("-" * len(header))

    for name, contact in book.data.items():
        contact_info = "| {0:15} | {1:15} | {2:20} | {3:25} | {4:10} | {5:30} |".format(
            contact.name.value, 
            contact.phone.value if contact.phone else 'N/A',
            contact.email.value if contact.email else 'N/A',
            contact.address.value if contact.address else 'N/A',
            contact.birthday.value if contact.birthday else 'N/A',
            contact.note.value if contact.note else 'N/A'
        )
        print(contact_info)

def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        print("Not enough information. Please provide name and new birthday.")
        return

    name, birthday = args
    book.update_birthday(name, birthday)


def show_birthday(args, book: AddressBook):
    if len(args) < 1:
        print("Please provide a contact name.")
        return

    name = args[0]
    contact = book.data.get(name)

    if contact is None:
        print("Contact not found.")
        return

    birthday = contact.birthday.value if contact.birthday else "Birthday not set"
    print(f"{name}'s birthday: {birthday}")


def show_birthdays(args, book: AddressBook):
    if not book.data:
        print("There are no contacts in your address book.")
        return

    header = "| {0:15} | {1:10} |".format("Name", "Birthday")
    print(header)
    print("-" * len(header))

    for name, contact in book.data.items():
        birthday = contact.birthday.value if contact.birthday else "N/A"
        print("| {0:15} | {1:10} |".format(contact.name.value, birthday))



def find_birthdays(args, book: AddressBook):
    if len(args) < 1:
        print("Please specify the number of days.")
        return

    try:
        days = int(args[0])
    except ValueError:
        print("Please provide a valid number of days.")
        return

    upcoming_birthdays = book.find_birthdays_in_days(days)
    if not upcoming_birthdays:
        print(f"No birthdays in the next {days} days.")
        return

    for name, contact in upcoming_birthdays.items():
        birthday_str = contact.birthday.value if contact.birthday else "N/A"
        print(f"{name}: {birthday_str}")



def find_contact(args, book: AddressBook):
    if len(args) < 1:
        print("Please provide a search term.")
        return

    search_term = ' '.join(args)
    found_contacts = book.find_contacts(search_term)

    if not found_contacts:
        print("No contacts found.")
        return

    header = "| {0:15} | {1:15} | {2:20} | {3:25} | {4:10} | {5:30} |".format(
        "Name", "Phone", "Email", "Address", "Birthday", "Note"
    )
    print(header)
    print("-" * len(header))

    for name, contact in found_contacts.items():
        contact_info = "| {0:15} | {1:15} | {2:20} | {3:25} | {4:10} | {5:30} |".format(
            contact.name.value, 
            contact.phone.value if contact.phone else 'N/A',
            contact.email.value if contact.email else 'N/A',
            contact.address.value if contact.address else 'N/A',
            contact.birthday.value if contact.birthday else 'N/A',
            contact.note.value if contact.note else 'N/A'
        )
        print(contact_info)

def add_note(args, book: AddressBook):
    if len(args) < 2:
        print("Please provide the contact name and the note.")
        return

    name = args[0]
    note = ' '.join(args[1:])

    contact = book.data.get(name)
    if not contact:
        print(f"Contact {name} not found.")
        return

    contact.note = Note(note)
    book.save_data()
    print(f"Note added to {name}: {note}")

def update_contact(args, book: AddressBook):
    if len(args) < 5:
        print("Not enough information. Please provide the name and at least one field to update.")
        return

    name, phone, birthday, email, address = args
    book.update_contact(name, phone, birthday, email, address)

def delete_contact(args, book: AddressBook):
    if len(args) < 1:
        print("Please provide the name of the contact to delete.")
        return

    name = args[0]
    book.delete_contact(name)

