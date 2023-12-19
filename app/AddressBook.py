from collections import UserDict
from app.Contact import Contact
from app.Fields import Name, Phone, Email, Address, Birthday, Note
from utils.error_handlers import input_error
from utils.prompt_handlers import is_yes_prompt
from constants.messages import error_messages
from datetime import datetime, timedelta
import json
import re

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.load_data()

    def add_contact(self, name, phone=None, birthday=None, email=None, address=None, note=None):
        if name in self.data:
            print("Contact already exists.")
            return
        
        try:
            self.data[name] = Contact(name, phone, birthday, email, address, note)
            self.save_data()
            print(f"Contact {name} added.")
        except ValueError as e:
            print(e)

    def update_contact(self, name, phone=None, birthday=None, email=None, address=None, note=None):
        if name not in self.data:
            print("Contact not found.")
            return
        
        try:
            contact = self.data.get(name)

            if contact:
                contact.phone = Phone(phone) if phone else contact.phone
                contact.birthday = Birthday(birthday) if birthday else contact.birthday
                contact.email = Email(email) if email else contact.email
                contact.address = Address(address) if address else contact.address
                contact.note = Note(note) if note else contact.note
                self.save_data()
                print(f"Contact {name} has been updated.")
        except ValueError as e:
            print(e)

    def delete_contact(self, name):
        try:
            if name in self.data:
                del self.data[name]
                self.save_data()
                print(f"Contact {name} has been deleted.")
            else:
                print("Contact not found.")
        except ValueError as e:
            print(e)

    def update_phone(self, name, new_phone):
        contact = self.data.get(name)
        if contact:
            # Оновлюємо телефонний номер контакту
            contact.phone = Phone(new_phone)  # Використовуємо клас Phone для валідації
            self.save_data()
            print(f"Phone number updated for {name}.")
        else:
            print("Contact not found.")

    def update_birthday(self, name, new_birthday):
        contact = self.data.get(name)
        if contact:
            # Оновлюємо день народження контакту
            contact.birthday = Birthday(new_birthday)  # Використовуємо клас Birthday для валідації
            self.save_data()
            print(f"Birthday updated for {name}.")
        else:
            print("Contact not found.")

    def list_birthdays(self, days):
        upcoming_birthdays = {}
        today = datetime.now().date()
        for name, info in self.data.items():
            if 'birthday' in info and info['birthday']:
                birthday = datetime.strptime(info['birthday'], "%d-%m-%Y").date()
                if today <= birthday <= today + timedelta(days=days):
                    upcoming_birthdays[name] = info['birthday']
        return upcoming_birthdays

    def find_contacts(self, search_term):
        found_contacts = {}
        for name, contact in self.data.items():
            # Перевірка, чи пошуковий термін міститься в будь-якому з атрибутів контакту
            if (search_term.lower() in contact.name.value.lower() or
                (contact.phone and search_term.lower() in contact.phone.value.lower()) or
                (contact.email and search_term.lower() in contact.email.value.lower()) or
                (contact.address and search_term.lower() in contact.address.value.lower()) or
                (contact.birthday and search_term.lower() in contact.birthday.value.lower()) or
                (contact.note and search_term.lower() in contact.note.value.lower())):
                found_contacts[name] = contact
        return found_contacts

    def find_birthdays_in_days(self, days):
        upcoming_birthdays = {}
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)

        for name, contact in self.data.items():
            birthday_str = contact.birthday.value if contact.birthday else None
            if birthday_str:
                try:
                    birthday = datetime.strptime(birthday_str, '%d.%m.%Y')
                    birthday_this_year = birthday.replace(year=current_date.year)
                    birthday_next_year = birthday.replace(year=current_date.year + 1)

                    if current_date <= birthday_this_year <= future_date or current_date <= birthday_next_year <= future_date:
                        upcoming_birthdays[name] = contact
                except ValueError:
                    print(f"Invalid date format for {name}: {birthday_str}. Expected format: DD.MM.YYYY")
                    continue

        return upcoming_birthdays

    def add_note_to_contact(self, name, note):
        if name in self.data:
            self.data[name].add_note(note)
            self.save_data()
            print(f"Note added to {name}.")
        else:
            print("Contact not found.")

    def edit_contact_note(self, name, note_index, new_note):
        if name in self.data:
            success = self.data[name].edit_note(note_index, new_note)
            if success:
                self.save_data()
                print(f"Note updated for {name}.")
            else:
                print("Invalid note index.")
        else:
            print("Contact not found.")

    def save_data(self):
        with open('contacts.json', 'w') as file:
            json_data = {}
            for name, contact in self.data.items():
                json_data[name] = {
                    "name": contact.name.value,
                    "phone": contact.phone.value if contact.phone else None,
                    "email": contact.email.value if contact.email else None,
                    "address": contact.address.value if contact.address else None,
                    "birthday": contact.birthday.value if contact.birthday else None,
                    "note": contact.note.value if contact.note else None
                }
            json.dump(json_data, file)

    def load_data(self):
        try:
            with open('contacts.json', 'r') as file:
                json_data = json.load(file)
                for name, contact_data in json_data.items():
                    self.data[name] = Contact(
                        name=contact_data['name'],
                        phone=contact_data['phone'],
                        email=contact_data['email'],
                        address=contact_data['address'],
                        birthday=contact_data['birthday'],
                        note=contact_data['note']
                    )
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {}
