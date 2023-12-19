import re
from datetime import datetime


phone_pattern = re.compile(r'^\+?\d{10,15}$') # Valid format: +380123456789 or 0123456789
email_pattern = re.compile(r'^\S+@\S+\.\S+$') # Valid format: example@email.com
date_format_default = '%d.%m.%Y'

# Birthday validation
def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, date_format_default)
        return True
    except ValueError:
        return False

# Phone number validation
def is_valid_phone(phone):
    return bool(phone_pattern.match(phone))

# Email validation
def is_valid_email(email):
    return bool(email_pattern.match(email))
