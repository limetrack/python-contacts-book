from utils.error_handlers import input_error, validation_error, ValidationError
from constants.messages import error_messages, validation_messages
from utils.validators import is_valid_phone, is_valid_date, is_valid_email

class Name:
    def __init__(self, name):
        self.value = name

class Phone:
    def __init__(self, phone):
        if not is_valid_phone(phone):
            raise ValueError(error_messages["invalid_phone_format"])
        self.value = phone

class Email:
    def __init__(self, email):
        if not is_valid_email(email):
            raise ValueError(error_messages["invalid_email_format"])
        self.value = email

class Address:
    def __init__(self, address):
        self.value = address

class Birthday:
    def __init__(self, birthday):
        if not is_valid_date(birthday):
            raise ValueError(error_messages["invalid_birthday_format"])
        self.value = birthday

class Note:
    def __init__(self, note):
        self.value = note

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

